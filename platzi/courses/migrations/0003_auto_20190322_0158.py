# Generated by Django 2.0 on 2019-03-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190318_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100)),
                ('certificada', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='end_date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='name',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='start_date',
        ),
        migrations.AddField(
            model_name='courses',
            name='cantidad',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]