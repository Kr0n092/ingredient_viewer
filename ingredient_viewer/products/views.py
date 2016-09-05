from django.shortcuts import render, get_list_or_404

# Create your views here.
from .models import Product


def list_all(request):
    """ Include all products in the response. """
    context = {
        'product_list' : get_list_or_404(Product),
    }
    return render(request=request, template_name='products/overview.html', context=context)