# # board/filters.py    
# import datetime
# from django.contrib import admin
# from .models import Board

# class CreatedDateFilter(admin.SimpleListFilter):
#     title = '작성일'
#     parameter_name = 'created'

#     # 커스텀 리스트 필터
#     def lookups(self, request, model_admin):
#         results = []
#         for i in range(-3, 6):
#             date = datetime.date.today() + datetime.timedelta(days=i)
#             display_str = '{0} [{1}개]'.format(
#                 date,
#                 Board.objects.filter(created__date=date).count()
#             )
#             display_str += ' - 오늘' if i == 0 else ''
#             results.append((date, display_str))
#         return results