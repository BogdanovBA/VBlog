# Generated by Django 3.2.3 on 2021-07-01 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InfoBlog', '0002_auto_20210629_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Посты', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='InfoBlog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(upload_to='images/%Y/%m/d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]