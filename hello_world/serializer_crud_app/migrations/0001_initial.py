# Generated by Django 4.1.7 on 2023-03-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snip_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ticket_no', models.IntegerField()),
                ('source', models.TextField(max_length=20)),
                ('destination', models.TextField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]