from django.contrib import admin

from school.models import Position, Employees, EmployeesCharacteristic, EmployeesAddress, Salary, Projects, \
    EmployeesInProjects, Company, Leader, Product, Sales, Address, PaymentAccount

admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(EmployeesCharacteristic)
admin.site.register(EmployeesAddress)
admin.site.register(Salary)
admin.site.register(Projects)
admin.site.register(EmployeesInProjects)
admin.site.register(Company)
admin.site.register(Leader)
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(Address)
admin.site.register(PaymentAccount)
