from django.db import models
from apps.auth_user.models import User
from datetime import datetime


# Create your models here.
class Car(models.Model):
    name_en = models.CharField(max_length=30)
    name_ru = models.CharField(max_length=30)
    owner_car = models.ForeignKey(User, on_delete=models.CASCADE)
    first_registration_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self):
        if self.clean():
            return super(Car, self).save()

    def clean(self):
        return Car.check_first_registration_date(self)

    @staticmethod
    def check_first_registration_date(car_obj):
        current_date = datetime.now().date()
        if current_date < car_obj.first_registration_date:
            print('The date entered from the form is larger than today')
            return False
        return True

    def __str__(self):
        return f"{self.id} - {self.name_en}"


class RentingCar(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='renting_cars')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()

    def save(self):
        if self.clean():
            return super(RentingCar, self).save()

    def clean(self):
        return RentingCar.does_reservation_overlap(self)

    @staticmethod
    def does_reservation_overlap(obj):
        if RentingCar.date_entered_correctly(obj):
            renting_cars = RentingCar.objects.filter(car__id=obj.car.id)
            for renting_car in renting_cars:
                if obj.lease_start_date <= renting_car.lease_end_date and renting_car.lease_start_date <= obj.lease_end_date:
                    print('Date is booked')
                    return False
            print('Save renting cars')
            return True
        return False

    @staticmethod
    def date_entered_correctly(obj):
        if obj.lease_start_date > obj.lease_end_date:
            print('The start date of the reservation cannot be longer than the end date')
            return False
        return True

    def __str__(self):
        return f"{self.user}, {self.car} ~~~ {self.lease_start_date} || {self.lease_end_date}"
