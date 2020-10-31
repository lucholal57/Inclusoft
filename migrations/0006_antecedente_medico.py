# Generated by Django 3.1 on 2020-10-31 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inclusoft', '0005_telefono_urgencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='antecedente_medico',
            fields=[
                ('ant_medico', models.AutoField(primary_key=True, serialize=False)),
                ('grupo_sanguineo', models.CharField(max_length=10)),
                ('factor_rh', models.CharField(max_length=10)),
                ('n_h_c', models.CharField(max_length=10)),
                ('convulsiona', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('medicacion_convulsion', models.CharField(max_length=50)),
                ('tipo_convulsion', models.CharField(max_length=50)),
                ('frecuencia', models.CharField(max_length=50)),
                ('doctor_asistente', models.CharField(max_length=50)),
                ('diabetico', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('medicacion_diabetico', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=100)),
                ('sangrado_nariz', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('problema_cardiaco', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('medicacion_cardiaco', models.CharField(max_length=50)),
                ('problema_hipertension', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('problemas_pulmonar', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('medicacion_pulmonar', models.CharField(max_length=50)),
                ('asma', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('desmayos', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('hernias', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('micosis', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=10)),
                ('medicacion_micosis', models.CharField(max_length=50)),
                ('comida_ptohibida', models.CharField(max_length=50)),
                ('dieta_especial', models.CharField(max_length=50)),
                ('tratamientos', models.CharField(max_length=50)),
                ('profesionales_tratamientos', models.CharField(max_length=50)),
                ('otra_medicacion', models.CharField(max_length=50)),
                ('conducta_fuga', models.CharField(max_length=50)),
                ('conduta_auto_o_hetero_agrecion', models.CharField(max_length=50)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inclusoft.alumno')),
            ],
        ),
    ]
