# Generated by Django 2.2.11 on 2020-03-08 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=80)),
                ('detail', models.TextField(max_length=200)),
                ('picture', models.ImageField(upload_to='')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('password', models.CharField(max_length=30)),
                ('create_date', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='')),
                ('poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll_Choice')),
                ('poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
                ('vote_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
