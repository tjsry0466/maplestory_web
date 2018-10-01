try:
    from django.utils import simplejson as json
except ImportError:
    import json

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404,  render
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from hitcount.views import HitCountDetailView

from .models import Board, Category, Comment
from .forms import BoardForm, CommentForm

class Index(TemplateView):
    
    template_name  = "board/index.html"

    def get_context_data(self, **kwargs):

        data = super(Index, self).get_context_data(**kwargs)
        data['notice'] = Board.objects.filter(category__slug='notice').order_by('-created')[:7]
        data['update'] = Board.objects.filter(category__slug='update').order_by('-created')[:7]
        data['event'] = Board.objects.filter(category__slug='event').order_by('-created')[:7]
        data['question'] = Board.objects.filter(category__slug='question').order_by('-created')[:5]
        data['free'] = Board.objects.filter(category__slug='free').order_by('-created')[:7]

        return data


class BoardLV(ListView):
    model = Board
    # template_name = 'board/notice_board_list.html'
    context_object_name = 'board_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        data = super(BoardLV, self).get_context_data(**kwargs)
        data['category'] = Category.objects.get(slug=self.kwargs['slug'])
        data['top_board'] = super().get_queryset().filter(
                category__slug=self.kwargs['slug'], notice=True)
        # data['board'] = super().get_queryset().filter(
        #         category__slug=self.kwargs['slug']).order_by('-created')
        
        return data
    
    def get_queryset(self):
        query = self.request.GET.get('q') 
        searchtype = self.request.GET.get('searchType')
        board = Board.objects.filter(notice=False, category__slug=self.kwargs['slug'])
        
        if query:
            if searchtype == '0':
                return board.filter(author__username__icontains=query)
            if searchtype == '1':
                return board.filter( Q(title__icontains=query) | Q(content__icontains=query)).distinct()
                
        return board
        
    def get_template_names(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        if not category.sub == '새소식':
            return ['board/commu_board_list.html']
        return ['board/notice_board_list.html']

    
class BoardDetail(HitCountDetailView):
    model = Board
    count_hit = True

    def get_object(self):
        category = self.kwargs.get('category')
        slug = self.kwargs.get('slug')
        queryset = Board.objects.filter(category__slug=category)
        return get_object_or_404(queryset, slug=slug)

    def get_template_names(self):
        category = Category.objects.get(slug=self.kwargs['category'])
        if not category.sub == '새소식':
            return ['board/commu_board_detail.html']
        return ['board/notice_board_detail.html']

    def get_context_data(self, **kwargs):
        context = super(BoardDetail, self).get_context_data(**kwargs)
        user = Board.objects.get(slug=self.kwargs.get('slug'))
        context['recent_board'] = Board.objects.filter(author=user.author)[:3]
        
        return context


    
@login_required
def BoardNew(request, categorySlug):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            # board.slug =  slugify(board.title, allow_unicode=True)
            board.category = Category.objects.filter(slug=categorySlug).get()
            board.save()
            return HttpResponseRedirect(reverse('board:detail', kwargs={'category': board.category.slug, 'slug':board.slug}))
    else:
        form = BoardForm()
    
    return render(request, 'board/board_new.html', {'form': form, 'category': Category.objects.get(slug=categorySlug)})

@login_required
@require_POST # 해당 뷰는 POST method 만 받는다.
def Board_like(request):
    pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    board = get_object_or_404(Board, pk=pk)
    board_like, board_like_created = board.like_set.get_or_create(user=request.user)

    if not board_like_created:
        # board_like.delete()
        message = "이미 추천한 게시물 입니다."
    else:
        message = "추천 했습니다."

    context = {'like_count': board.like_count,
               'message': message,
              }
               # 'username': request.user.username }

    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
def CommentNew(request, boardslug):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # board.slug =  slugify(board.title, allow_unicode=True)
            comment.board = Board.objects.filter(slug=boardslug).get()
            comment.save()
            return HttpResponseRedirect(reverse('board:detail', kwargs={'category': comment.board.category.slug, 'slug':boardslug}))
    return 


class Commentdelete(DeleteView):
    model = Comment

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        queryset = Comment.objects.get(id=pk)
        board = Board.objects.get(comment=queryset)
        if not queryset.author == self.request.user:
            raise Http404
        queryset.delete()

        return HttpResponseRedirect(board.get_absolute_url())

    # template 안불러오게!
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class Boarddelete(DeleteView):
    model = Board

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        queryset = get_object_or_404(Board, id=pk)
        if not queryset.author == self.request.user:
            raise Http404
        queryset.delete()

        return HttpResponseRedirect(reverse('board:list', kwargs= {'slug':queryset.category.slug}))

    # template 안불러오게!
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

@login_required
def Boardupdate(request, pk):
    if request.method == "POST":
        board = Board.objects.get(pk=pk)
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return HttpResponseRedirect(board.get_absolute_url())
    else:
        board = Board.objects.get(pk=pk)
        form = BoardForm(instance = board)
    
    return render(request, 'board/board_update.html', {'form': form, 'board':board})
