from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product.forms import ProductCreationForm, ProductChangeForm
from product.models import Product


class ProductListView(ListView):
    model = Product
    #'product_list.html', {product_list' : Product.objets.all()}
    paginate_by = 3

def list_product(request):
    product_list = Product.objects.all() #DB에 있는 product 전체 가져오자
    context = {'product_list' : product_list} #product_list라는 키로 놓자
    #product/product_list.html에 보내자
    return render(request, 'product/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    #'product_detail.html' {'product': Product.objects.get(pk=pk)} pk = 'primary key'

def detail_product(request, pk):
    # DB에서 pk가 pk인 product 하나 가져오자
    # product_detail.html에게 product라는 변수로 product를 보내자
    product_detail = Product.objects.get(pk=pk)
    context = {'product' : product_detail}
    return render(request, 'product/product_detail.html', context)

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']  #'__all__'
    template_name_suffix = '_create'    #product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')  #추가 성공하면, 이동할 url 이름

def create_product(request):
    if request.method == 'POST': #사용자가 입력하고 submit 버튼 눌렀을 때
        form = ProductCreationForm(request.POST)
        if form.is_valid(): #form 검사
            form.save() #form에 있는 정보 저장
        return redirect('product:list') #저장하고 product_lisz2로 넘어가기
    else: # 처음에 빈 폼 보여주기
        form = ProductCreationForm()
    return render(request, 'product/product_create.html', {'form': form})

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price']
    template_name_suffix = '_update'  #product_form.html -> product_update.html
    # 일반적으로 성공하면 detail로 간다
    # success_url = reverse_lazy('product:list') #수정 성공하면, 이동할 url 이름

def update_product(request, pk):
    if request.method == 'POST':    #사용자가 입력하고 submit 버튼을 눌렀을 때
        #form에 있는 내용 가져오기
        form = ProductChangeForm(request.POST)
        if form.is_valid(): #form 검사
            selected_product = Product.objects.get(pk=pk)   #pk로 Product에서 하나 꺼내기
        selected_product.name = form.cleaned_data.get('name')   #입력한 내용으로 Product 내용 수정
        selected_product.price = form.cleaned_data.get('price')
        selected_product.save() # product 저장
    else:
        #처음에 선택한 내용을 폼으로 보여주자
        selected_product = Product.objects.get(pk=pk)   #pk로 Product에서 하나 꺼내자 -- DB select문
        form = ProductChangeForm(instance=selected_product)     #form에 표시하자

    return render(request, 'product/product_update.html', {'form' : form})


class ProductDeleteView(DeleteView):
    model = Product
    # 삭제할 항목만 알면 되기 때문에 fields는 필요없음.
    success_url = reverse_lazy('product:list') #삭제 성공하면 이동할 url 이름
    #product_confirm_delete.html
