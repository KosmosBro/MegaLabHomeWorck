from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100, )

    def __str__(self):
        return self.title


class Employees(models.Model):
    last_name = models.CharField(max_length=100, )
    first_name = models.CharField(max_length=100, )
    second_name = models.CharField(max_length=100, )
    position = models.ManyToManyField(Position)

    def __str__(self):
        return self.first_name


class EmployeesCharacteristic(models.Model):
    title = models.CharField(max_length=200)
    employees = models.ManyToManyField(Employees)

    def __str__(self):
        return self.title


class EmployeesAddress(models.Model):
    address_title = models.CharField(max_length=50)
    number_address = models.IntegerField(max_length=10)
    employees = models.OneToOneField(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.address_title


class Salary(models.Model):
    salary = models.IntegerField(max_length=100)
    employees = models.ManyToManyField(Employees)

    def __str__(self):
        return self.salary


class EmployeesInProjects(models.Model):
    days_in_project = models.IntegerField()
    employees = models.ManyToManyField(Employees)

    def __str__(self):
        return self.days_in_project


class Projects(models.Model):
    title = models.CharField(max_length=100, )
    stat_date = models.DateField()
    end_date = models.DateField()
    in_project = models.OneToOneField(EmployeesInProjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=50, )

    def __str__(self):
        return self.title


class Leader(models.Model):
    last_name = models.CharField(max_length=20, )
    second_name = models.CharField(max_length=20, )
    name = models.CharField(max_length=20, )
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name


class Product(models.Model):
    title = models.CharField(max_length=50, )
    price = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.title


class Sales(models.Model):
    count = models.IntegerField()
    date_of_sale = models.DateField()
    product = models.ManyToManyField(Product, )
    company = models.ManyToManyField(Company, )

    def __str__(self):
        return self.count


class Address(models.Model):
    title = models.CharField(max_length=50, )
    number = models.IntegerField()
    company = models.ManyToManyField(Company, )

    def __str__(self):
        return self.title


class PaymentAccount(models.Model):
    number = models.IntegerField()
    company = models.ManyToManyField(Company, )
