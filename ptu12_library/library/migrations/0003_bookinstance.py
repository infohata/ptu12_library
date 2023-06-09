# Generated by Django 4.2.1 on 2023-05-30 11:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateField(blank=True, db_index=True, null=True, verbose_name='due back')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Available'), (1, 'Reserved'), (2, 'Taken'), (3, 'Unavailable'), (7, 'Broken')], db_index=True, default=0, verbose_name='status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='library.book', verbose_name='book')),
            ],
            options={
                'verbose_name': 'book instance',
                'verbose_name_plural': 'book instances',
                'ordering': ['due_back'],
            },
        ),
    ]
