from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext as _
from apps.car.models import Car, RentingCar
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .helpers import exception_email


# Create your views here.
class CarCreate(LoginRequiredMixin, CreateView):
    login_url = 'login_url'
    model = Car
    fields = ['name_en', 'name_ru', 'first_registration_date']
    template_name = 'car/car_create.html'

    def form_valid(self, form):
        entered_data_form = form.save(commit=False)
        entered_data_form.owner_car = self.request.user

        if entered_data_form.save():
            messages.add_message(self.request, messages.SUCCESS, _('Car is create success!'))
            message = f"Car is create - {entered_data_form.name_en}"
            exception_email(message=message, send_to=[self.request.user.email])
        else:
            messages.add_message(self.request, messages.SUCCESS, _('Incorrect data entered!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car_all_url')


class CarProfile(LoginRequiredMixin, View):
    login_url = 'login_url'

    def get(self, request, pk):
        car_object = Car.objects.get(id=pk)
        return render(request, 'car/car_profile.html', context={'car_object': car_object})


class CarAll(LoginRequiredMixin, View):
    login_url = 'login_url'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'car/car_all.html', context={'cars': cars})


class CarEdit(LoginRequiredMixin, UpdateView):
    login_url = 'login_url'
    model = Car
    fields = ['name_en', 'name_ru', 'first_registration_date']
    template_name = 'car/car_edit.html'

    def get_success_url(self):
        car_object = self.object
        return reverse('car_profile_url', kwargs={'pk': car_object.pk})


class CarRentedUser(View):
    def get(self, request):
        my_renting_cars = request.user.renting_cars.all()
        return render(request, 'car/car_rented_user.html', context={'cars': my_renting_cars})


class CarDelete(LoginRequiredMixin, View):
    login_url = 'login_url'

    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        return render(request, 'car/car_delete.html', context={'car': car})

    def post(self, request, pk):
        car = Car.objects.get(id=pk)
        car.delete()
        return redirect('car_all_url')


class CarRenting(LoginRequiredMixin, View):
    login_url = 'login_url'

    def get(self, request):
        renting_cars = RentingCar.objects.all()
        return render(request, 'car_renting/car_renting.html', context={'renting_cars': renting_cars})


class CarRentingAdd(LoginRequiredMixin, CreateView):
    login_url = 'login_url'
    model = RentingCar
    fields = ['car', 'lease_start_date', 'lease_end_date']
    template_name = 'car_renting/car_renting_add.html'

    def form_valid(self, form):
        entered_data_form = form.save(commit=False)
        entered_data_form.user = self.request.user

        if entered_data_form.save():
            message = f"Book car {entered_data_form.car.name_en} is create." \
                      f"Forget date {entered_data_form.lease_start_date} - {entered_data_form.lease_end_date}"
            messages.add_message(self.request, messages.SUCCESS, _('Renting car added is success!'))
            exception_email(message=message, send_to=[self.request.user.email])
        else:
            messages.add_message(self.request, messages.SUCCESS, _('Renting car added not success!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car_all_url')
