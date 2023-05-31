from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from product.models import Product


class ProductListView(ListView):
    model = Product
    #'product_list.html', {product_list' : Product.objets.all()}
    paginate_by = 3

def list_product(request):
    product_list = Product.objects.all()[:2] #DB에 있는 product 전체 가져오자
    context = {'product_list' : product_list} #product_list라는 키로 놓자
    #product/product_list.html에 보내자
    return render(request, 'product/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    #'product_detail.html' {'product': Product.objects.get(pk=pk)} pk = 'primary key'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']  #'__all__'
    template_name_suffix = '_create'    #product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')  #추가 성공하면, 이동할 url 이름

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price']
    template_name_suffix = '_update'  #product_form.html -> product_update.html
    # 일반적으로 성공하면 detail로 간다
    # success_url = reverse_lazy('product:list') #수정 성공하면, 이동할 url 이름

class ProductDeleteView(DeleteView):
    model = Product
    # 삭제할 항목만 알면 되기 때문에 fields는 필요없음.
    success_url = reverse_lazy('product:list') #삭제 성공하면 이동할 url 이름
    #product_confirm_delete.html
