from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.

class MeasureUnit(BaseModel):
    """Clase para unidad de medida."""

    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    # Configuration for custom historical user
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, changed_by):
        self.changed_by = changed_by
    # End Configuration for custom historical user

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'

    def __str__(self):
        return f'Unidad: {self.description}'

class CategoryProduct(BaseModel):
    """Clase para unidad de medida."""

    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida')
    historical = HistoricalRecords()

    # Configuration for custom historical user
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, changed_by):
        self.changed_by = changed_by
    # End Configuration for custom historical user

    class Meta:
        verbose_name = 'Categoría de producto'
        verbose_name_plural = 'Categorías de productos'

    def __str__(self):
        return f'Categoría: {self.description}'

class Indicator(BaseModel):
    """Clase para un indicador."""
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta')
    historical = HistoricalRecords()

    # Configuration for custom historical user
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, changed_by):
        self.changed_by = changed_by
    # End Configuration for custom historical user

    class Meta:
        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de ofertas'

    def __str__(self):
        return f'Descuento por categoría:{self.category_product} {self.descount_value}'

class Product(BaseModel):
    """Clase para unidad de medida."""

    name = models.CharField('Nombre de producto', max_length=50, blank=False, null=False, unique=True)
    description = models.CharField('Descripción', max_length=150, blank=False, null=False, unique=True)
    image = models.ImageField('Imagen del producto', upload_to='products/',blank=True, null=True)
    historical = HistoricalRecords()

    # Configuration for custom historical user
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, changed_by):
        self.changed_by = changed_by
    # End Configuration for custom historical user

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'Producto: {self.name}'