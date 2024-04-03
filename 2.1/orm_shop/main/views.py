from django.http import Http404
from django.shortcuts import render
from .models import Car, Client, Sale


def cars_list_view(request):
    template_name = 'main/list.html'
    cars = Car.objects.all()
    return render(request, template_name, context={'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        template_name = 'main/details.html'
        car = Car.objects.get(id=car_id)
        return render(request, template_name, {'car': car})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')



def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        context = {'car': car, 'sales': sales}
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')
