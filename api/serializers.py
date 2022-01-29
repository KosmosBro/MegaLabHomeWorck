from rest_framework import serializers

from school.models import Position, Employees, EmployeesAddress, EmployeesInProjects, Projects, Company, Leader, \
    Product, Sales, Address, PaymentAccount


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'title']


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'last_name', 'first_name', 'second_name', 'position']


class EmployeesAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeesAddress
        fields = ['id', 'address_title', 'number_address']


class SalarySerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeesAddress
        fields = ['id', 'salary', 'employees']


class EmployeesInProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeesInProjects
        fields = ['id', 'days_in_project', 'employees']


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'start_date', 'end_date', 'in_project']


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'title']


class LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ['last_name', 'second_name', 'name', 'company']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'weight']


class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['count', 'date_of_sale', 'product', 'company']


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['title', 'number', 'company']


class PaymentAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentAccount
        fields = ['number', 'company']
