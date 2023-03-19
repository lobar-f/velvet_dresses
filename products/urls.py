
from django.urls import path

from . import views
app_name='products'

urlpatterns = [
    path('', views.HomeListView.as_view(),name='index'),
    path('about_us/',  views.AboutUsView.as_view(),name='about_us'),
    path('faq/',  views.FAQView.as_view(),name='faq'),
    path('terms/',  views.TermsView.as_view(), name='terms'),
    path('contacts/',  views.ContactsView.as_view(), name='contacts'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

	#path('<slug:category_slug>/', views.CategoryListView.as_view(), name='product_list_by_category'),
	]
    