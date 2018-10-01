from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Board, Comment, Category, Like


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Board)
class BoardAdmin(SummernoteModelAdmin):
    list_per_page = 15
    list_display = ('id','category','author', 'title','short_content', 'notice','created',)
    list_editable = ('notice',)    
    list_filter = ('author','created','notice','category')
    list_display_links= ('title',)
    search_fields = ('title', 'content')
    # slug는 title로 자동 입력되도록 설정
    # prepopulated_fields = {'slug': ('title',)}
    actions = ['make_notice', 'make_none_notice']
    inlines = [CommentInline]

    fieldsets = (
        ('기본 정보', {
            'fields': (('author', 'category','notice',), )
        }),
        ('제목 및 내용', {
            'fields': ('title', 'content',)
        }),
    )

    def make_notice(self, request, queryset):
        
        updated_count = queryset.update(notice=True)
        self.message_user(request, '{}건의 게시물을 공지사항으로 변경'.format(updated_count))
    make_notice.short_description = "선택된 게시판을 공지사항으로 변경합니다"

    def make_none_notice(self, request, queryset):
        
        updated_count = queryset.update(notice=False)
        self.message_user(request, '{}건의 게시물을 일반 게시물로 변경'.format(updated_count))
    make_none_notice.short_description = "선택된 게시판을 일반 게시물로 변경합니다"

    def short_content(self, board):
        return board.content[:20]

    # 금지어 적용
    # def clean_content(self): #clean_{field_name}
    #     content = self.cleaned_data['content']
    #     words = ['심심하다', '관리자', '금지어', ]
    #     error_message = '[{0}] {1}'.format(', '.join(words), '와 같은 단어들은 입력 하실 수 없습니다.')

    #     if any(word in content for word in words):
    #         raise forms.ValidationError(error_message)

    #     return content


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'message')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass






