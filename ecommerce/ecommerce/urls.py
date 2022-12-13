
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from ecommerce.userapp.views import SignUpView
from .import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name="home" ),
    path('contact', TemplateView.as_view(template_name='contact.html'), name="contact" ),
    path('about', TemplateView.as_view(template_name='about.html'), name="about" ),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
    re_path(r'^userapp/', include("ecommerce.userapp.urls")),
    re_path(r'^productapp/', include("ecommerce.productapp.urls")),
    
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
