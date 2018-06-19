# Generated by Django 2.0.2 on 2018-06-19 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecturers.Lecturer')),
            ],
        ),
    ]
