# Generated by Django 2.1.4 on 2019-01-02 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Image',
        ),
        migrations.AlterField(
            model_name='image',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listing.Version'),
        ),
    ]
