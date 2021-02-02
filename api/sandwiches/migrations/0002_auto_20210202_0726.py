# Generated by Django 3.1.6 on 2021-02-02 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwich',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', through='sandwiches.Sand_Ing', to='sandwiches.Ingredient'),
        ),
        migrations.AlterField(
            model_name='sandwich',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sandwiches', to='sandwiches.order'),
        ),
    ]
