from django.db import models


class TradeNetwork(models.Model):
    """
    Модель торговой сети с иерархией
    """
    LEVELS = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    title = models.CharField(max_length=255)
    level = models.IntegerField(choices=LEVELS)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Торговая сеть'
        verbose_name_plural = 'Торговые сети'

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Модель контактов
    """
    network = models.ForeignKey(TradeNetwork, on_delete=models.CASCADE, related_name='contacts')
    email = models.EmailField(null=True, blank=True, unique=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    house_number = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    """
    Модель продукта
    """
    network = models.ForeignKey(TradeNetwork, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
