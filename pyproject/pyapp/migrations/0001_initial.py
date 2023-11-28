# Generated by Django 4.2.7 on 2023-11-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phonenumber', models.CharField(blank=True, max_length=20, null=True)),
                ('bankbalance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('isstudent', models.BooleanField(default=False)),
            ],
        ),
    ]
