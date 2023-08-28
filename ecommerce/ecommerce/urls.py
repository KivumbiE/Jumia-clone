"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from ecommerceapp import views
from ecommerceapp import AdminViews
from django.conf.urls.static import static
from ecommerce import settings

urlpatterns = [
    path('admin/', views.adminLogin,name="admin_login"),
    path('admindashboard/demo',views.demoPage),
    path('admindashboard/demoPage',views.demoPageTemplate),
    path('admindashboard/admin_login_process',views.adminLoginProcess,name="admin_login_process"),
    path('admindashboard/admin_logout_process',views.adminLogoutProcess,name="admin_logout_process"),

    path('admin_home',AdminViews.admin_home,name="admin_home"),

    #CATERGORIES
    path('admindashboard/category_list',AdminViews.CategoriesListView.as_view(),name="category_list"),
    path('admindashboard/category_create',AdminViews.CategoriesCreate.as_view(),name="category_create"),
    path('admindashboard/category_update/<slug:pk>',AdminViews.CategoriesUpdate.as_view(),name="category_update"),

    #SUBCATERGORIES
    path('admindashboard/sub_category_list',AdminViews.SubCategoriesListView.as_view(),name="sub_category_list"),
    path('admindashboard/sub_category_create',AdminViews.SubCategoriesCreate.as_view(),name="sub_category_create"),
    path('admindashboard/sub_category_update/<slug:pk>',AdminViews.SubCategoriesUpdate.as_view(),name="sub_category_update"),

    #Merchant User
    path('admindashboard/merchant_create',AdminViews.MerchantUserCreateView.as_view(),name="merchant_create"),
    path('admindashboard/merchant_list',AdminViews.MerchantUserListView.as_view(),name="merchant_list"),
    path('admindashboard/merchant_update/<slug:pk>',AdminViews.MerchantUserUpdateView.as_view(),name="merchant_update"),

    #Products
    path('admindashboard/product_create',AdminViews.ProductView.as_view(),name="product_view"),
    path('admindashboard/product_list',AdminViews.ProductListView.as_view(),name="product_list"),  
    path('admindashboard/product_edit/<str:product_id>',AdminViews.ProductEdit.as_view(),name="product_edit"),
    path('admindashboard/product_add_media/<str:product_id>',AdminViews.ProductAddMedia.as_view(),name="product_add_media"),
    path('admindashboard/product_edit_media/<str:product_id>',AdminViews.ProductEditMedia.as_view(),name="product_edit_media"),
    path('admindashboard/product_media_delete/<str:id>',AdminViews.ProductMediaDelete.as_view(),name="product_media_delete"),
    path('admindashboard/product_add_stocks/<str:product_id>',AdminViews.ProductAddStocks.as_view(),name="product_add_stocks"),

    #Staff User
    path('admindashboard/staff_create',AdminViews.StaffUserCreateView.as_view(),name="staff_create"),
    path('admindashboard/staff_list',AdminViews.StaffUserListView.as_view(),name="staff_list"),
    path('admindashboard/staff_update/<slug:pk>',AdminViews.StaffUserUpdateView.as_view(),name="staff_update"),

    #Customer User
    path('admindashboard/customer_create',AdminViews.CustomerUserCreateView.as_view(),name="customer_create"),
    path('admindashboard/customer_list',AdminViews.CustomerUserListView.as_view(),name="customer_list"),
    path('admindashboard/customer_update/<slug:pk>',AdminViews.CustomerUserUpdateView.as_view(),name="customer_update"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
