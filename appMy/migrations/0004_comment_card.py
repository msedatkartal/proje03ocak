# Generated by Django 4.2.2 on 2023-07-06 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.card', verbose_name='Kart'),
        ),
    ]
