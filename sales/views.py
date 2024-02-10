from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_bookname_from_id, get_chart
from django.contrib.auth.decorators import login_required 

def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None
    chart = None

    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')

        qs = Sale.objects.filter(book__name=book_title)
        if len(qs) > 0:
            sales_df = pd.DataFrame(qs.values())
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
            chart = get_chart(chart_type, sales_df, labels=sales_df['book_id'].values)
            sales_df = sales_df.to_html()

            print('Exploring querysets:')
            print('Case 1: Output of Sale.objects.all()')
            qs = Sale.objects.all()
            print(qs)

            print('Case 2: Output of Sale.objects.filter(book_name=book_title)')
            qs = Sale.objects.filter(book__name=book_title)
            print(qs)

            print('Case 3: Output of qs.values')
            print(qs.values())

            print('Case 4: Output of qs.values_list()')
            print(qs.values_list())

            print('Case 5: Output of Sale.objects.get(id=1)')
            obj = Sale.objects.get(id=1)
            print(obj)

    context = {
        'form': form,
        'sales_df': sales_df,
        'chart': chart
    }

    return render(request, 'sales/records.html', context)

def success(request):
    # Your success view logic goes here
    return render(request, 'sales/success.html')
