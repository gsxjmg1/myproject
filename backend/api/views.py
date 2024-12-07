from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from api.models import HomePage, Swiper, DetailPage


def home(request, id):
    if request.method == 'GET':
        if id == 1:
            # 当 id 为 1 时，获取所有 HomePage 数据
            home_pages = HomePage.objects.all()
            data = [
                {
                    'id': hp.id,
                    'page_name': hp.page_name,
                    'home_image': hp.home_image,
                }
                for hp in home_pages
            ]
            return JsonResponse({'data': data})
        if id == 2:
            # 当 id 为 2 时，获取所有 Swiper 数据
            swiper_images = Swiper.objects.all()
            data = [
                {
                    'id': hp.id,
                    'imageSrc': hp.swiper_image,
                }
                for hp in swiper_images
            ]
            return JsonResponse({'data': data})


def detail(request, id):
    if request.method == 'GET':
        if id == 1:
            # 查询 id 为 1 的记录
            detail_page = DetailPage.objects.get(id=1)
            # 返回 model_info 字段中的 JSON 数据
            return JsonResponse(detail_page.model_info, safe=False)
        elif id == 2:
            # 查询 id 为 2 的记录
            detail_page = DetailPage.objects.get(id=2)
            # 返回 model_info 字段中的 JSON 数据
            return JsonResponse(detail_page.model_info, safe=False)
        elif id == 3:
            # 查询 id 为 3 的记录
            detail_page = DetailPage.objects.get(id=3)
            # 返回 model_info 字段中的 JSON 数据
            return JsonResponse(detail_page.model_info, safe=False)
        elif id == 4:
            # 查询 id 为 4 的记录
            detail_page = DetailPage.objects.get(id=4)
            # 返回 model_info 字段中的 JSON 数据
            return JsonResponse(detail_page.model_info, safe=False)
        else:
            # 如果没有找到正确的 id
            return JsonResponse({"error": "DetailPage with id 1 not found"}, status=404)
