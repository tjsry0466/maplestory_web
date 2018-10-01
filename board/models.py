from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django_summernote import fields as summer_fields
from django.utils.text import slugify

from slugger import AutoSlugField
from model_utils.models import TimeStampedModel
from hitcount.models import HitCount, HitCountMixin

# 게시판 ㅎㄹㅇㄹ
class Board(TimeStampedModel, HitCountMixin):
    class Meta:
        verbose_name = u'게시판'
        verbose_name_plural = u'게시판'
        ordering = ['-created']
        
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    title = models.CharField(
        verbose_name=u'제목',
        max_length=256)
    content = summer_fields.SummernoteTextField(
        verbose_name=u'내용',
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='카테고리',
        on_delete=models.CASCADE,
    )
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_user_set',
        through='Like')
    notice = models.BooleanField(default=False)
    slug = AutoSlugField(
        unique=True,
        populate_from='title',
        allow_unicode=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:detail', kwargs={'category':str(self.category.slug), 'slug':str(self.slug)})

    def get_previous_post(self):
        try:
            previous_post = Board.objects.filter(created__gt=self.created).filter(category__title=self.category.title).last()
        except IndexError:
            return None
        return previous_post

    def get_next_post(self):
        try:
            next_post = Board.objects.filter(created__lt=self.created).filter(category__title=self.category.title).first()
        except IndexError:
            return None
        return next_post 
    
    def save(self, *args, **kwargs):
        super(Board, self).save(*args, **kwargs) 
        self.slug = '%s--%s' %(
            self.id,
            slugify(self.title, allow_unicode=True)
        ) 
        super(Board, self).save(*args, **kwargs) 
        
    @property
    def like_count(self):
        return self.like_user_set.count()
        
# 코멘트
class Comment(TimeStampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=u'작성자'
    )
    board = models.ForeignKey(
        'Board',
        on_delete=models.CASCADE,
        verbose_name=u'게시글'
    )
    message = models.TextField(verbose_name='내용')

    class Meta:
        verbose_name = u'댓글'
        verbose_name_plural = u'댓글'
        ordering = ['-id']

    def __str__(self):
        return self.message


class Category(models.Model):
    title = models.CharField(
        max_length=90,
        default='카테고리를 선택해 주세요',
        verbose_name=u'이름',
    )
    slug = models.SlugField(max_length=200, unique=True)
    descripttion = models.TextField(null=True, blank=True)
    sub = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = u'카테고리'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/board/%s/" % self.slug
    
class Like(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'좋아요'
        verbose_name_plural = u'좋아요'
        unique_together = (
            ('user', 'board')
)



