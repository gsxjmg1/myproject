
from django.contrib import admin
from django.urls import path
from api import views
from django.http import HttpResponse


# 示例根路径视图
def home_view(request):
    return HttpResponse("<h1>Welcome to the Django Backend!</h1>")


urlpatterns = [
    path('', home_view, name='home'),  # 根路径
    path('admin/', admin.site.urls),
    path('api/home/<int:id>', views.home),  # 主页面接口
    path('api/detail/<int:id>', views.detail)  # 子页面接口
]
