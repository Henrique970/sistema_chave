# Generated by Django 2.2.3 on 2019-07-02 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_pegou', models.TimeField(auto_now_add=True)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Chave')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Devolver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_devolveu', models.TimeField(auto_now_add=True)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Chave')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
            ],
        ),
    ]
