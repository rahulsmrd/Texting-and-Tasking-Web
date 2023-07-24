from django.urls import path,include
from user_data import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


app_name='user_data'

urlpatterns = [
    # path("<pk>",views.user_list,name="user_list"),
    path("login/",auth_views.LoginView.as_view(template_name='user_data/login.html'),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("signup/",views.SignUp,name="signup"),
    # path("profile/",views.profile_form_view,name="profile"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)