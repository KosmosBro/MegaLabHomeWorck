from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Employees(models.Model):
    last_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100, null=False)
    position = models.ManyToManyField(Position, blank=False)

    def __str__(self):
        return self.first_name


class EmployeesCharacteristic(models.Model):
    title = models.CharField(max_length=200, null=False)
    employees = models.ManyToManyField(Employees, null=False)

    def __str__(self):
        return self.title


class EmployeesAddress(models.Model):
    address_title = models.CharField(max_length=50, null=False)
    number_address = models.IntegerField(max_length=10, null=False)
    employees = models.OneToOneField(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.address_title


class Salary(models.Model):
    salary = models.IntegerField(max_length=100, null=False)
    employees = models.ManyToManyField(Employees, null=False)


class EmployeesInProjects(models.Model):
    days_in_project = models.IntegerField(null=False)
    employees = models.ManyToManyField(Employees, null=False)


class Projects(models.Model):
    title = models.CharField(max_length=100, null=False)
    stat_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    in_project = models.OneToOneField(EmployeesInProjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




