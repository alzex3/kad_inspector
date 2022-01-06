# Generated by Django 3.1.2 on 2022-01-05 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('verbose_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Типы объектов',
                'verbose_name_plural': 'Типы объектов',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('full_address', models.CharField(max_length=450)),
                ('update_date', models.DateField(max_length=10)),
                ('created_date', models.DateField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=13)),
                ('stamp', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.objecttype')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('user', models.CharField(max_length=15, verbose_name='Пользователь')),
                ('objects', models.ManyToManyField(related_name='lists', to='home.Object')),
            ],
            options={
                'verbose_name': 'Списки объектов',
                'verbose_name_plural': 'Списки объектов',
            },
        ),
    ]