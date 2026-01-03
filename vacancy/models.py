from django.core.validators import FileExtensionValidator,RegexValidator
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=75, unique=True, verbose_name="Elon bo'lim nomi")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Elon nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Tavsifi")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Rasimi")
    salary = models.CharField(max_length=50,verbose_name="Oylik maosh",help_text="Masalan:500-600$/oy")
    video = models.FileField(upload_to="videos/", null=True, blank=True, verbose_name="Videosi",
                             help_text="Siz faqat 'mp4','avi','mov' video yuklay olasiz!",

                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])])
    phone = models.CharField(max_length=20,verbose_name="Telefon raqami",default='+998901234567',help_text="Masalan: +998901234567",
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$',message="Telefon raqami +998901234567 formatida bo'lishi kerak")])
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriyasi")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarilganmi?",
                                    help_text="Belgilasangiz saytga chiqadi!!!")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        ordering = ['created']
