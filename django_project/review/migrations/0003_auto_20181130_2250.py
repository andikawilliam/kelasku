# Generated by Django 2.1.3 on 2018-11-30 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20181130_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lecturer', models.CharField(default='Mr. John Doe', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='lecturer',
        ),
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.Course'),
        ),
    ]
