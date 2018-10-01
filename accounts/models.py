from django.conf import settings
from django.db.models.signals import post_save
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    authnum = models.CharField(
        max_length=7,
        verbose_name=u'인증번호', 
        help_text='※ 인증번호 7자리는 게임 내에서 주민등록번호 뒷자리 대신 본인인증 용도로 사용됩니다. 기억하기 쉬운 7자리 숫자를 입력해주세요. 예: 1412927, 2236665, 1234567'
    )
    gender = models.CharField(
        max_length=2,
        verbose_name=u'성별',
        help_text='※ 성별은 인게임 정보에 실제 반영됩니다. 신중히 선택해주세요.',
        )

# def on_post_save_for_user(sender, **kwargs):
#     if kwargs['created']:
#         user = kwargs['instance']
#         print(user)
#         Profile.objects.create(user=user,)
    
# post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)



    
