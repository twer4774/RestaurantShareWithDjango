from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import * #모델 사용

# Create your views here.
def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants': restaurants}
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant': restaurant}
    # return render(request, 'shareRes/restaurantDetail.html')
    return render(request, 'shareRes/restaurantDetail.html', content)

#레스토랑 수정
def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories':categories, 'restaurant': restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)

#레스토랑 삭제
def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))

#레스토랑 업데이트
def Update_restaurant(request):
    resId= request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))

#레스토랑 추가화면 보여줌
def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    # return render(request, 'shareRes/restaurantCreate.html')
    return render(request, 'shareRes/restaurantCreate.html', content)

#레스토랑 추가
def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link, restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

#카테고리 추가 화면을 보여줌
def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate.html', content)

#카테고리 추가 버튼을 눌렀을 때 동작
def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save() #데이터베이스에 저장
    return HttpResponseRedirect(reverse('index')) #리다이렉트


#카테고리 삭제
def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    deltete_categoery.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

