# Generated by Django 4.1.2 on 2022-11-03 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinicaapp", "0003_pacientes_obra_social_pacientes_turno_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="pacientes", name="obra_social",),
        migrations.AlterField(
            model_name="pacientes", name="turno", field=models.BooleanField(),
        ),
    ]
