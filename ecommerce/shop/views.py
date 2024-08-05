from django.shortcuts import render, redirect
from .forms import ProductForm

def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Assume you have a product_list view
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})
