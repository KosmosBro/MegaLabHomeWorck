from rest_framework import viewsets, generics

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
    serializer_class = CompanySerializers
    queryset = Company.objects.all()


class LeaderListAPIView(viewsets.ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializers


class ProductListAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.filter(price__gte=20)


# class ProductListAPIView(generics.ListAPIView):
#     serializer_class = ProductSerializers
#     queryset = Product.objects.all()
#
#     def get_queryset(self):
#         queryset = Product.objects.all()
#         price = self.request.query_params.get('price')
#         if price:
#             queryset = Product.objects.filter(price__gte=20)
#         return queryset


class SalesListAPIView(viewsets.ModelViewSet):
    serializer_class = SalesSerializers
    queryset = Sales.objects.all()


class AddressListAPIView(viewsets.ModelViewSet):
    serializer_class = AddressSerializers
    queryset = Address.objects.all()


class PaymentAccountListAPIView(viewsets.ModelViewSet):
    queryset = PaymentAccount.objects.all()
    serializer_class = PaymentAccountSerializers
