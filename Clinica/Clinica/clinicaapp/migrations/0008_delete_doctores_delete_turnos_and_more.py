# Generated by Django 4.1.2 on 2022-11-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinicaapp", "0007_doctores_consultorio_doctores_especialidad_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Doctores",),
        migrations.DeleteModel(name="Turnos",),
        migrations.AlterField(
            model_name="pacientes",
            name="obra_social",
            field=models.CharField(max_length=20),
        ),
    ]
