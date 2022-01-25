from django.contrib import admin

from school.models import Position, Employees, EmployeesCharacteristic, EmployeesAddress, Salary, Projects, \
    EmployeesInProjects

admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(EmployeesCharacteristic)
admin.site.register(EmployeesAddress)
admin.site.register(Salary)
admin.site.register(Projects)
admin.site.register(EmployeesInProjects)
