from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth import views as auth_views
from allauth.account.views import LoginView
from allauth.socialaccount.views import SignupView
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import CustomSignupForm, ProfileForm, LoginForm


# class SignupView(CreateView):
#     model = User
#     form_class = SignupForm
#     template_name = 'accounts/signup.html'
    
#     def get_success_url(self):
#         return resolve_url('profile')
    
#     def form_valid(self, form):
#         user = form.save()
#         auth_login(self.request, user)
#         return redirect(self.get_success_url())
        
# signup = SignupView.as_view()


@login_required #settings.login_url
def profile(request):
    
    return render(request, 'accounts/profile.html')

## 함수 기반 뷰
def signup(request):

    if request.method == 'POST':
        form_class =CustomSignupForm
        signupform = form_class(request.POST)
        # form_class = ProfileForm
        # profileform = form_class(request.POST)
        if signupform.is_valid():
            form = signupform.save()
            
            auth_login(request, form) # 회원가입과 동시에 로그인 처리
            
            # if profileform.is_valid():
            #     profile = profileform.save(commit=False)
            #     profile.user=request.user
            #     profile.save()
            return redirect('board:index')
    else:
        signupform = CustomSignupForm()
        # profileform = ProfileForm()
    return render(request, 'accounts/signup.html', {
        'signupform' : signupform,
        # 'profileform' : profileform,
    })

# class signup(SignupView):
#     form_class =SignupForm
#     template_name = 'accounts/signup.html'

### 간편 클래스 기반 뷰
# signup = CreateView.as_view(model=User,
#                             form_class=SignupForm,
#                             success_url=settings.LOGIN_URL,
#                             template_name='accounts/signup.html')

# def login(request):
#     providers = []
#     for provider in get_providers():  # settings/INSTALLED_APPS 내에서 활성화된 목록
#         # social_app속성은 provider에는 없는 속성입니다.
#         try:
#             # 실제 Provider 별 Client id/secret 이 등록이 되어있는가?
#             provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
#         except SocialApp.DoesNotExist:
#             provider.social_app = None
#         providers.append(provider)

#     return auth_login(
#         request, 
#         authentication_form=LoginForm,
#         template_name='accounts/login_form.html',
#         extra_context={'providers': providers}
#     )

class login(LoginView):
    pass