from django.urls import path
from . import views
urlpatterns = [
    path('api/employee',views.employeelistView),
    path('api/employee/<int:pk>',views.employeeDetailView),
]
