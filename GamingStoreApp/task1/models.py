from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])  # Возраст от 0 до 100

    def __str__(self):
        return self.name
    
class Achievement(models.Model):
    class RarityChoices(models.TextChoices):
        COMMON = 'common', _('Обычное')
        RARE = 'rare', _('Редкое')
        ULTRA_RARE = 'ultra_rare', _('Сверхредкое')
        MYTHICAL = 'mythical', _('Мифическое')
        LEGENDARY = 'legendary', _('Легендарное')
        SECRET = 'secret', _('Секретное')

    title = models.CharField(max_length=200, verbose_name="Название")
    rarity = models.CharField(
        max_length=20,
        choices=RarityChoices.choices,
        default=RarityChoices.COMMON,
        verbose_name="Редкость"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    buyer = models.ManyToManyField('Buyer', related_name='achievements', verbose_name="Покупатели")

    def __str__(self):
        return f"{self.title} ({self.get_rarity_display()})"
    
class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title