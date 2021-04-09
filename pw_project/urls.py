"""pw_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('mains.urls')),
                  path('register/', user_views.register, name='register'),
                  path('login/', user_views.login_user, name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  path('profile/<int:pk>/', user_views.profile, name = 'profile'),
                  path('post/<int:pk>/', user_views.post_details, name = 'post-details'),
                  path('create-post/', user_views.create_post, name = 'create-post'),
                  path('delete-post/<int:pk>/', user_views.delete_post, name='delete-post'),
                  path('update-post/<int:pk>/', user_views.update_post, name='update-post'),
                  path('update-profile/<int:pk>/', user_views.update_profile, name='update-profile'),
                  path('my-admin/', user_views.my_admin, name = 'my-admin'),
                  path('delete-user/<int:pk>/', user_views.delete_user, name='delete-user'),
                  path('manage-types-domains/', user_views.manage_types_domains, name = 'manage-types-domains'),
                  path('create-domain', user_views.create_domain, name = 'create-domain'),
                  path('create-type', user_views.create_type, name = 'create-type'),
                  path('delete-domain/<int:pk>', user_views.delete_domain, name = 'delete-domain'),
                  path('delete-type/<int:pk>', user_views.delete_type, name='delete-type'),
                  path('update-domain/<int:pk>/', user_views.update_domain, name='update-domain'),
                  path('update-type/<int:pk>/', user_views.update_type, name='update-type'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
