# Generated by Django 2.2.2 on 2019-07-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcomment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('상식', '상식'), ('철학', '철학'), ('정치', '정치')], default='상식', max_length=20),
        ),
    ]