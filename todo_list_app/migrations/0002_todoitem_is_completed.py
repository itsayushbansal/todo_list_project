# Generated by Django 4.0.3 on 2022-03-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = 'admin'
        DJANGO_SU_EMAIL = 'admin@admin.com'
        DJANGO_SU_PASSWORD = 'admin'

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(generate_superuser),
    ]
