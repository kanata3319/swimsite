"""swimsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.urls import include, path
import debug_toolbar
from event.views import HomeView, ResultKojinFormView, ResultTaikaiListView, ResultKojinCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('result/kojin', ResultKojinFormView.as_view(), name='result_kojin'),
    path('result/taikai', ResultTaikaiListView.as_view(), name='result_taikai'),
    path('result/kojin/create', ResultKojinCreateView.as_view(), name='result_kojin_create'),
    path('result/relay/create', ResultKojinCreateView.as_view(), name='result_relay_create'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
