# Generated by Django 4.1.7 on 2023-02-28 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(default=0, help_text='Нужно указывать в процентах. Этот процент будет добавлен к стоимости товара', verbose_name='Надбавка')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Скидка')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category', to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150, verbose_name='Имя пользователя')),
                ('stars', models.IntegerField(default=0, verbose_name='Количество звезд')),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_rating', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('color', models.CharField(max_length=150, verbose_name='Цвет')),
                ('color_css', models.CharField(default='#FFFFFF', max_length=150, verbose_name='Цвет css')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150, verbose_name='Имя пользователя')),
                ('text', models.TextField(max_length=5000, verbose_name='Отзыв')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_comment', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
