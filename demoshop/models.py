from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.forms import MultipleChoiceField


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


class CreditInfo(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    credit_text = models.TextField('Описание', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассрочка'
        verbose_name_plural = 'Информация о рассрочке'


class CreditProgram(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    vznos = models.IntegerField('Первый взнос', null=True, blank=True)
    overprice = models.IntegerField('Переплата', null=True, blank=True)
    lengh = models.IntegerField('Срок кредита', null=True, blank=True)
    parent = models.ForeignKey(CreditInfo, related_name="Родитель+", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Программа рассрочки'
        verbose_name_plural = 'Программы рассрочки'


class Categories(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    image = models.ImageField('Изображение категории', height_field=None, width_field=None, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    parent = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="Родительская категория+", parent_link=True)
    title = models.CharField('Название', max_length=100, null=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class ContactInfo(models.Model):
    title = "Контактная информация"
    phone = models.CharField('Номер телефона', max_length=11, null=True, blank=False)
    telega = models.CharField('Telegram', max_length=200, null=True, blank=False)
    whatsapp = models.CharField('Whatsapp', max_length=200, null=True, blank=False)
    insta = models.CharField('Instagramm', max_length=200, null=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class TagsShild(models.Model):
    CHOICES = (
        ('Новинка', 'Новинка 1'),
        ('Рассрочка', 'Рассрочка 2'),
        ('Акция', 'Акция 3'),
    )


class Products(models.Model):
    tags = models.CharField("Шильдик", max_length=100, null=True, blank=True, choices=TagsShild.CHOICES)
    name = models.CharField('Наименовение', max_length=100, null=False, blank=False, unique=True)
    price = models.FloatField('Цена', null=False, blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(9999999)])
    description = models.TextField('Описание', null=False, blank=False, default="", validators=[MinLengthValidator(0)])
    image = models.ImageField('Картинка для анонса', null=True, blank=True)
    memory = models.CharField("Объем памяти ГБ", max_length=100, null=True, blank=True, default="", validators=[MinLengthValidator(0)])
    category = models.ForeignKey(SubCategory, verbose_name="Родительская категория", on_delete=models.CASCADE, related_name="Родительский элемент+", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class ProductImage(models.Model):
  image = models.ImageField("Изображения подробно", null=True, blank=True)
  product = models.ForeignKey(Products, verbose_name="Изображения подробно", related_name="images", on_delete=models.CASCADE)