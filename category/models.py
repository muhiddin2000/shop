from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, help_text="_kategoriya nomi")
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table= 'Categories'
        verbose_name = _("Kategoriya ")
        verbose_name_plural = _("Kategoriyalar ")