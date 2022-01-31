from django.urls import path, include
from rest_framework import routers

from api import api_views as v
from api.api_views import ProductListAPIView

router = routers.DefaultRouter()
router.register(r'position', v.PositionListAPIView),
router.register(r'employees', v.EmployeesListAPIView),
router.register(r'address', v.EmployeesAddressListAPIView),
router.register(r'salary', v.SalaryListAPIView),
router.register(r'in_project', v.EmployeesInProjectsListAPIView),
router.register(r'project', v.ProjectsListAPIView),
router.register(r'company', v.CompanyListAPIView),
router.register(r'leader', v.LeaderListAPIView),
router.register(r'sales', v.SalesListAPIView),
router.register(r'address', v.AddressListAPIView),
router.register(r'products', v.ProductListAPIView),
router.register(r'paymentAccount', v.PaymentAccountListAPIView),


urlpatterns = [
    path('', include(router.urls)),
    # path('products/', ProductListAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

