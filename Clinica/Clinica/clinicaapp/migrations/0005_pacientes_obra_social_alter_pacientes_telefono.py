# Generated by Django 4.1.2 on 2022-11-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinicaapp", "0004_remove_pacientes_obra_social_alter_pacientes_turno"),
    ]

    operations = [
        migrations.AddField(
            model_name="pacientes",
            name="obra_social",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="pacientes", name="telefono", field=models.IntegerField(),
        ),
    ]
