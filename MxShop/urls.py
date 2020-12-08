"""MxShop URL Configuration

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
import xadmin
from django.urls import path,include,re_path
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


# from goods.views import GoodsListView
from goods.views import GoodsListViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter
from users.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewset,LeavingMessageViewset,AddressViewset
from trade.views import ShoppingCartViewset,OrderViewset

router = DefaultRouter()
#配置googs的Url
router.register(r'goods',GoodsListViewSet)
router.register('categorys',CategoryViewSet,basename='categorys')
# 配置code的url
router.register('code',SmsCodeViewset,basename='code')
router.register('users',UserViewset,basename='users')
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset,basename="messages")
# 配置收货地址
router.register(r'address',AddressViewset , basename="address")
# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
# 配置订单的url
router.register(r'orders', OrderViewset, basename="orders")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls' )),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),

    path("desc",include_docs_urls(title="在线生鲜")),
    path('api-auth/',include('rest_framework.urls')),

    # path("goods/",GoodsListView.as_view(),name='goods-list'),#商品列表页
    re_path('^',include(router.urls)),

    # django 认证token
    path('api-token-auth/', views.obtain_auth_token),
    # jwt的token认证接口
    path('jwt-auth/', obtain_jwt_token),
    path('login/',obtain_jwt_token), #登录


]
