# Generated by Django 4.1.5 on 2023-02-15 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('checkout', models.BooleanField(default=False)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
