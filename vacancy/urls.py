from django.urls import path
from .views import all_vacancy,vacancy_by_category,vacancy_detail,add_vacancies,update_vacancy,delete_vacancy

urlpatterns = [
    path('',all_vacancy,name="all_vacancy"),
    path("vacancy/add/",add_vacancies,name="add_vacancies"),
    path('category/<int:category_id>/', vacancy_by_category, name="vacancy_by_category"),
    path('vacancy/<int:pk>/', vacancy_detail, name="vacancy_detail"),
    path("vacancy/<int:vacancy_id>/delete/", delete_vacancy, name="delete_vacancy"),
    path("vacancy/<int:vacancy_id>/update/", update_vacancy, name="update_vacancy"),

]
