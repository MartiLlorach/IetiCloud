# Generated by Django 3.2 on 2022-02-10 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arxius', '0002_alter_carpeta_carpeta_pare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arxiu',
            name='carpeta_pare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arxius.carpeta'),
        ),
        migrations.AlterField(
            model_name='carpeta',
            name='carpeta_pare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arxius.carpeta'),
        ),
    ]
