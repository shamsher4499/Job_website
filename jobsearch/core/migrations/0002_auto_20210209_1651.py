# Generated by Django 3.1.6 on 2021-02-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_url',
        ),
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
        migrations.RemoveField(
            model_name='job',
            name='how_to_apply',
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='exp',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.IntegerField(choices=[(1, 'Full-time'), (2, 'Part-time'), (3, 'Internship')], default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
