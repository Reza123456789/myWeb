from django.contrib import admin
from django.urls import path , include

from  django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('projects.urls')),
    path((''),include('users.urls')),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
