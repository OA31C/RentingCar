from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from renting_car.settings import EMAIL_HOST_USER
from apps.car.models import Car, RentingCar
from django.core.mail import send_mail
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
class CarCreate(LoginRequiredMixin, CreateView):
    login_url = 'login_url'
    model = Car
    fields = ['name_en', 'name_ru', 'first_registration_date']
    template_name = 'car/car_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner_car = self.request.user
        self.object.save()
        message = f"Car is create - {self.object.name_en}"
        send_mail('Renting Car Django', message, EMAIL_HOST_USER, [self.request.user.email])
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
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        message = f"Book car {self.object.car.name_en} is create." \
                  f"Forget date {self.object.lease_start_date} - {self.object.lease_end_date}"
        send_mail('Renting Car Django', message, EMAIL_HOST_USER, [self.request.user.email])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car_all_url')
