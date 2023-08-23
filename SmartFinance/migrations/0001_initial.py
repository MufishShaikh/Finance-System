# Generated by Django 4.1.2 on 2023-04-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('details', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=50)),
                ('ans', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('number', models.PositiveIntegerField(default='')),
                ('address', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('narration', models.CharField(blank=True, max_length=1000, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartFinance.categories')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartFinance.signup')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartFinance.signup'),
        ),
    ]