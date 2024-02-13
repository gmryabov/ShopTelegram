from django.db import models
from transliterate import translit


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Banner(models.Model):
    date = models.DateField('Дата создания', auto_now_add=True)
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    is_active = models.BooleanField('Активность', auto_created=True, default=True)
    banner = models.ImageField('Баннер', height_field=None, width_field=None, null=True, blank=True)
    url = models.CharField('Ссылка', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class PromoBlock(models.Model):
    is_active = models.BooleanField('Активность', auto_created=True, default=True)
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    old_price = models.IntegerField('Старая цена', null=True, blank=True)
    new_price = models.IntegerField('Новая цена', null=True, blank=True)
    image = models.ImageField('Баннер', height_field=None, width_field=None, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class CreditProgram(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    vznos = models.IntegerField('Первый взнос', null=True, blank=True)
    overprice = models.IntegerField('Переплата', null=True, blank=True)
    lengh = models.IntegerField('Срок кредита', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Программа рассрочки'
        verbose_name_plural = 'Программы рассрочки'


class CreditInfo(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    credit_text = models.TextField('Описание', max_length=1000, null=True, blank=True)
    # porgramm = models.ForeignKey(CreditProgram, on_delete=models.CASCADE, null=True, blank=True)
    programm = models.ManyToManyField(CreditProgram, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассрочка'
        verbose_name_plural = 'Информация о рассрочке'


class Categories(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    image = models.ImageField('Изображение категории', height_field=None, width_field=None, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
