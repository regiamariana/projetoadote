# Generated by Django 4.1.5 on 2023-03-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # crie um modelo
        migrations.CreateModel(
            # com esses campos e esse tipo de informação
            name='Raca',
            fields=[
                # sempre há um id com tipo de dado bigautofield
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=50)),

                #para isso criar no banco, precisa dar o comando migrate, que vai varrer todos os arquivos de migrate verificando quais foram executados e quais não, e os que não foram são executados
            ],
        ),
    ]