from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Vacancy
from django.http import HttpRequest
from .forms import VacancyForm


# Create your views here.

def all_vacancy(request):
    categories = Category.objects.all()
    vacancies = Vacancy.objects.filter(published=True)
    context = {
        "categories": categories,
        "vacancies": vacancies,
        "title": "E'lonlar",
    }
    return render(request, 'vacancy/index.html', context)


def vacancy_by_category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    vacancies = Vacancy.objects.filter(category=category, published=True)
    context = {
        "categories": categories,
        "vacancies": vacancies,
        "title": category.name,
    }
    return render(request, 'vacancy/index.html', context)


def vacancy_detail(request, pk: int):
    categories = Category.objects.all()
    vacancy = get_object_or_404(Vacancy, pk=pk, published=True)
    vacancy.views += 1
    vacancy.save()

    context = {
        "categories": categories,
        "vacancy": vacancy,
        "title": vacancy.title,
    }
    return render(request, "vacancy/detail.html", context)


#                       CRUD


def add_vacancies(request: HttpRequest):
    if not request.user.is_staff:
        raise PermissionDenied

    form = VacancyForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST" and form.is_valid():
        vacancy = form.save()
        messages.success(request, "Vacancy successfully added")

        return redirect("vacancy_detail", pk=vacancy.pk)

    return render(request, "vacancy/add_vacancy.html", {
        "form": form,
        "title": "Vakansiya qo'shish",
        "button_text": "Save",
    })


def delete_vacancy(request: HttpRequest, vacancy_id: int):
    if not request.user.is_staff:
        raise PermissionDenied

    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)

    if request.method == "POST":
        vacancy.delete()
        messages.success(request, "Vacancy successfully deleted")

        return redirect("all_vacancy")

    else:
        messages.warning(request, f"Are you sure deleted {vacancy.title}??")

        return render(request, "vacancy/delete.html",
                      {
                          "vacancy": vacancy,
                          "title": f"{vacancy.title} ni o'chirish"
                      })


def update_vacancy(request: HttpRequest, vacancy_id: int):
    if not request.user.is_staff:
        raise PermissionDenied

    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)

    if request.method == "POST":
        form = VacancyForm(request.POST, request.FILES, instance=vacancy)
        if form.is_valid():
            form.save()
            messages.success(request, "Vacancy successfully updated")

            return redirect('vacancy_detail', pk=vacancy.pk)
    else:
        form = VacancyForm(instance=vacancy)

    return render(request, "vacancy/update_vacancy.html",
                  {
                      "form": form,
                      "vacancy": vacancy,
                      "title": f"{vacancy.title} ni tahrirlash",
                      "button_text": "Update"
                  })
