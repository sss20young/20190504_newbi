"""mydjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
import login.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login.views.main, name='main'),
    path('detail/<int:id>/', login.views.detail, name='detail'),
    path('accounts/', include('allauth.urls')),
    
    path('SNU/', login.views.suniv, name='SNU'),
    path('KW/', login.views.kuniv, name='KW'),
    path('tip/<int:tip_id>', login.views.detail_tip, name="detail_tip"),
    path('review/<int:review_id>', login.views.detail_review, name="detail_review"),
    path('like', login.views.tip_like, name="tip_like"),
    
]
