# Generated by Django 2.0.7 on 2018-07-10 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='products')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('width', models.PositiveSmallIntegerField(default=0)),
                ('length', models.PositiveSmallIntegerField(default=0)),
                ('height', models.PositiveSmallIntegerField(default=0)),
                ('ray', models.PositiveSmallIntegerField(default=0)),
                ('availability', models.DateField()),
                ('category', models.ManyToManyField(related_name='products', to='main.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='picture',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='main.Product'),
        ),
    ]