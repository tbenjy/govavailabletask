from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Organizations(models.Model):
    organizationID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)


class Employees(models.Model):
    employeeID = models.CharField(max_length=9, unique=True, validators=[MinLengthValidator(9)])
    privateName = models.CharField(max_length=20)
    familyName = models.CharField(max_length=20)
    organizationID = models.ForeignKey(Organizations, on_delete=models.CASCADE)


class Places(models.Model):
    placeID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    organizationID = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    catchBy = models.ForeignKey(Employees, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "organizationID"], name="Unique place")
        ]


class EmployeePlacesHistory(models.Model):
    historyID = models.BigAutoField(primary_key=True)
    employeeID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    placeID = models.ForeignKey(Places, on_delete=models.CASCADE)
    ReservationTime = models.DateTimeField()
