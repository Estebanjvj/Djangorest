from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """Base Class for any AppModel."""

    # TODO Define fields here
    id = models.AutoField(primary_key = True)
    status = models.BooleanField('Estatus',default = True)
    created_date = models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    modificated_date = models.DateTimeField('Fecha de modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateTimeField('Fecha de eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos base'
