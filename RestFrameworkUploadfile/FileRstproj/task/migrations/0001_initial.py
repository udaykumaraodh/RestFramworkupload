# Generated by Django 3.1.7 on 2021-08-20 07:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import task.validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='docs/photos/', validators=[task.validation.validate_img])),
                ('xlsdoc', models.FileField(upload_to='docs/xldoc/', validators=[task.validation.validate_xls])),
                ('idproof', models.FileField(upload_to='docs/proofs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfiles', models.FileField(upload_to='singledocs/multifiles/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
