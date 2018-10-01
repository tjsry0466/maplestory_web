from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M', '남자'),
    ('F', '여자'),
)

class LoginForm(AuthenticationForm):
    pass


# class SignupForm(UserCreationForm):
#     pass

class CustomSignupForm(UserCreationForm):

    username = forms.CharField(label='아이디',
                                 max_length=15,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                '아이디를 입력해주세요.', }))
    password1 = forms.CharField(label='비밀번호',
                                 max_length=15,
                                 widget=forms.PasswordInput(
                                     ))
    password2 = forms.CharField(label='비밀번호 확인',
                                 max_length=15,
                                 widget=forms.PasswordInput(
                                     ))

    authnum = forms.CharField(label='인증번호',
                                max_length=7,
                                help_text='※ 인증번호 7자리는 게임 내에서 주민등록번호 뒷자리 대신 본인인증 용도로 사용됩니다. 기억하기 쉬운 7자리 숫자를 입력해주세요. 예: 1412927, 2236665, 1234567',
                                widget=forms.TextInput(
                                    attrs={'placeholder':
                                               '*******', }))
    gender = forms.CharField(label='성별',
                            max_length=2,
                            help_text='※ 성별은 인게임 정보에 실제 반영됩니다. 신중히 선택해주세요.',
                            widget=forms.RadioSelect(
                                choices=GENDER_CHOICES,
                                ))

    def signup(self, request, user):
        Profile.objects.create(user=User.objects.get(username=self.cleaned_data['username']), authnum=self.cleaned_data['authnum'], gender = self.cleaned_data['gender'])

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'type':'text'
            }),
            'gender': forms.RadioSelect(choices=GENDER_CHOICES)
        }
