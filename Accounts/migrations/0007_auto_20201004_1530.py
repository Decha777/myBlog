# Generated by Django 3.1.1 on 2020-10-04 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20201002_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='exprerience',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.experience'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='skills',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.skill'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='works',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.work'),
        ),
    ]