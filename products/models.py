

# Create your models here.
from django.db import models

# Create your models here.
from category.models import Category
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class Product(models.Model):
    name = models.CharField(max_length=600, help_text=_("Mahsulot nomini kiriting"), verbose_name=_("Mahsulot nomi"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text=_("Mahsulot kategoriyasini tanlang"),
                                 verbose_name=_("Mahsulot kategoriyasi"))
    image = models.ImageField(upload_to='product-images', help_text=_("Mahsulot rasmini yuklang"),
                              verbose_name=_("Mahsulot rasmi"))
    description = models.TextField(help_text=_("Mahsulot haqida kiriting"), verbose_name=_("Mahsulot haqida qisqacha"))
    cost = models.IntegerField(help_text=_("Mahsulot narxini kiriting"), verbose_name=_("Mahsulot narxi"))
    discount = models.IntegerField(help_text=_("Mahsulot chegirma narxini kiriting"), verbose_name=_("Chegirma narxi"),
                                   default=0)
    viewed = models.IntegerField(help_text=_("Ko'rilganlari soni"), verbose_name=_("Ko'rilganlari soni"), null=True,
                                 blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
        verbose_name = _("Mahsulot ")
        verbose_name_plural = _("Mahsulotlar ")

    @property
    def image_show(self):
        return format_html('<img src={} width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
