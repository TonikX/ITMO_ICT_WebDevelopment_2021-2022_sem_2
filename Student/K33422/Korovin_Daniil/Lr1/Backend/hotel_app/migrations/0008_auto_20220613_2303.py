# Generated by Django 3.2.7 on 2022-06-13 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0007_alter_cleaner_old_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaner',
            name='contract_number',
            field=models.CharField(max_length=255, verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='cleaner',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='cleaner',
            name='old_phone',
            field=models.CharField(blank=True, default='', max_length=14, verbose_name='Старый телефон'),
        ),
        migrations.AlterField(
            model_name='cleaner',
            name='phone',
            field=models.CharField(max_length=14, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=255, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='pasport',
            field=models.CharField(max_length=20, verbose_name='паспорт'),
        ),
        migrations.AlterField(
            model_name='inhabitation',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel_app.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='inhabitation',
            name='in_date',
            field=models.DateField(verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='inhabitation',
            name='out_date',
            field=models.DateField(verbose_name='Дата выселения'),
        ),
        migrations.AlterField(
            model_name='inhabitation',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel_app.room', verbose_name='Комната'),
        ),
        migrations.AlterField(
            model_name='room',
            name='cost_of_living',
            field=models.IntegerField(verbose_name='цена заселения'),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(verbose_name='этаж'),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(verbose_name='номер'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.IntegerField(choices=[(1, 'Одноместный'), (2, 'Двуместный'), (3, 'Трёхместный')], max_length=30, verbose_name='тип комнаты'),
        ),
    ]
