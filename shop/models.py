from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name='Картинка', blank=True)
    sequence = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class Material(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    price = models.IntegerField(verbose_name="Надбавка", default=0,
                                help_text='Нужно указывать в процентах. Этот процент будет добавлен к стоимости товара')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка', blank=True)
    sequence = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='product_category',
                                 verbose_name='Категория')
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(max_length=5000, verbose_name="Описание")
    material = models.ManyToManyField(Material, related_name='product_material', blank=True, verbose_name='Материалы')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    discount = models.IntegerField(blank=True, null=True, default=0, verbose_name='Скидка')
    rating = models.FloatField(default=0, verbose_name="Общий рейтинг")
    sequence = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                related_name='product_comment', verbose_name='Товар')
    author = models.CharField(max_length=150, verbose_name="Имя пользователя")
    text = models.TextField(max_length=5000, verbose_name="Отзыв")
    sequence = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Товар: {self.product.name}, Автор: {self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                related_name='product_rating', verbose_name='Товар')
    author = models.CharField(max_length=150, verbose_name="Имя пользователя")
    stars = models.IntegerField(default=0, verbose_name="Количество звезд")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Товар: {self.product.name}, Автор: {self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                related_name='product_image', verbose_name='Товар')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    color = models.CharField(max_length=150, verbose_name="Цвет")
    color_css = models.CharField(max_length=150, default='#FFFFFF', verbose_name="Цвет css")
    sequence = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Товар: {self.product.name}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
