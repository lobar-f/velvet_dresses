from django.shortcuts import render
from .models import Product, Category, FAQ
# Create your views here.
from .filters import ProductFilter


from django.views.generic import TemplateView, ListView, DetailView

# class CategoryListView(ListView):
#     model = Category
#     template_name = 'product_list.html'

#     def get_queryset(self, **kwargs):
#        qs = super().get_queryset(**kwargs)
#        return qs.filter(category_slug=self.kwargs['slug'])


class HomeListView(ListView):
    model = Product
    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['favourite_products'] = Product.objects.filter(favorite=True)[:8]
        context['latest_products'] = Product.objects.order_by('-pub_date')[:8]
        context['mama_dochka'] = Product.objects.filter(category__slug ='platya-mama-dochka')[:1]


        return context

class AboutUsView(TemplateView):
    template_name = "about-us.html"

class FAQView(TemplateView):
    template_name = "faq.html"
    model = FAQ

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['questions']=FAQ.objects.all()
        return context

class TermsView(TemplateView):
    template_name = "terms.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_count'] = Product.objects.all().count()
        context['categories']=Category.objects.all()
        context['filter']=ProductFilter(self.request.GET, queryset=self.get_queryset().order_by('-pub_date'))
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        
        context['random_products'] = Product.objects.order_by('?')[:5]
        return context
