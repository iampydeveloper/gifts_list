# Generated by Django 5.0.6 on 2024-10-21 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0005_alter_gift_link_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='gift_image',
        ),
        migrations.RemoveField(
            model_name='gift',
            name='gift_link',
        ),
        migrations.AlterField(
            model_name='gift',
            name='link_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='GiftItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gift_images/')),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='gifts.gift')),
            ],
        ),
    ]
