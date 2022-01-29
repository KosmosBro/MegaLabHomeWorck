from rest_framework import viewsets

from api.serializers import PositionSerializers, EmployeesSerializers, EmployeesAddressSerializers, SalarySerializers, \
    EmployeesInProjectsSerializers, ProjectSerializers, CompanySerializers, LeaderSerializers, ProductSerializers, \
    SalesSerializers, AddressSerializers, PaymentAccountSerializers
from school.models import Position, Employees, EmployeesAddress, Salary, EmployeesInProjects, Projects, Company, Leader, \
    Product, Sales, Address, PaymentAccount


class PositionListAPIView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class EmployeesListAPIView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers


class EmployeesAddressListAPIView(viewsets.ModelViewSet):
    queryset = EmployeesAddress.objects.all()
    serializer_class = EmployeesAddressSerializers


class SalaryListAPIView(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializers


class EmployeesInProjectsListAPIView(viewsets.ModelViewSet):
    queryset = EmployeesInProjects.objects.all()
    serializer_class = EmployeesInProjectsSerializers


class ProjectsListAPIView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializers


class CompanyListAPIView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class LeaderListAPIView(viewsets.ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializers


class ProductListAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class SalesListAPIView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers


class AddressListAPIView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers


class PaymentAccountListAPIView(viewsets.ModelViewSet):
    queryset = PaymentAccount.objects.all()
    serializer_class = PaymentAccountSerializers
