# Generated by Django 4.1.3 on 2022-11-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='rating',
            name='date',
            field=models.DateField(verbose_name='Date Rating Was Created:'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.CharField(choices=[('E', 'Excellent'), ('G', 'Good'), ('F', 'Fair'), ('P', 'Poor')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='game',
            name='characters',
            field=models.ManyToManyField(to='main_app.character'),
        ),
    ]
