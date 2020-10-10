from django.db import models
from apps.auth_user.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Car(models.Model):
    name_en = models.CharField(verbose_name=_("Name EN"), max_length=30)
    name_ru = models.CharField(verbose_name=_("Name RU"), max_length=30)
    owner_car = models.ForeignKey(User, on_delete=models.CASCADE)
    first_registration_date = models.DateField(verbose_name=_("First registration date"))
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self):
        if self.clean():
            super(Car, self).save()
            return True

    def clean(self):
        if Car.check_first_registration_date(self):
            print('Коректно введені дані')
            return True

    @staticmethod
    def check_first_registration_date(entered_data_about_car):
        """Checks whether the date entered by the user is not greater than today"""

        current_date = datetime.now().date()
        if current_date < entered_data_about_car.first_registration_date:
            return False
        return True

    def __str__(self):
        return f"{self.id} - {self.name_en}"


class RentingCar(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='renting_cars')
    car = models.ForeignKey(Car, verbose_name=_("Car"), on_delete=models.CASCADE)
    lease_start_date = models.DateField(verbose_name=_("Lease start date"))
    lease_end_date = models.DateField(verbose_name=_("Lease end date"))

    def save(self):
        if self.clean():
            super(RentingCar, self).save()
            return True

    def clean(self):
        if RentingCar.run_all_checks(self):
            return True

    @staticmethod
    def run_all_checks(entered_form_data):
        """Launches all checks."""
        if (RentingCar.check_correctness_start_and_end_rental_date(entered_form_data) and
                RentingCar.check_start_rental_date(entered_form_data) and
                RentingCar.does_reservation_overlap(entered_form_data)):
            return True

    @staticmethod
    def does_reservation_overlap(entered_form_data):
        """Check reservation overlap date."""

        renting_cars = RentingCar.objects.filter(car__id=entered_form_data.car.id)
        print()
        print()
        print()
        print()
        print()
        print('renting cars')
        print(renting_cars)
        print()
        print()
        print()

        for renting_car in renting_cars:
            if not (entered_form_data.lease_start_date <= renting_car.lease_end_date and
                    renting_car.lease_start_date <= entered_form_data.lease_end_date):
                return True
            return False
        return True

    @staticmethod
    def check_start_rental_date(entered_form_data):
        """Checks whether the entered start date is not in the past tense."""

        current_date = datetime.now().date()
        print(current_date)
        if entered_form_data.lease_start_date >= current_date:
            print('Введена дата коректна')
            return True

    @staticmethod
    def check_correctness_start_and_end_rental_date(entered_form_data):
        """Checks whether the start of the lease date, is not greater than the end of the lease date."""

        if not (entered_form_data.lease_start_date > entered_form_data.lease_end_date):
            print('Дата введена коректно')
            return True
        print('Введена дата не є коректною')

    def __str__(self):
        return f"{self.user}, {self.car} ~~~ {self.lease_start_date} || {self.lease_end_date}"
