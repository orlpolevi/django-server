# Generated by Django 3.0.5 on 2021-03-05 11:28

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Users.User')),
                ('coursesRequired', models.CharField(choices=[('alg1', 'Algebra 1'), ('alg2', 'Algebra 2'), ('clc1', 'Calculus 1'), ('clc2', 'Calculus 2'), ('prb1', 'Probability'), ('dsc1', 'Descrete 1'), ('dsc2', 'Descrete 2'), ('psc1', 'Physics 1'), ('psc2', 'Physics 2'), ('psc3', 'Physics 3'), ('defo', 'default')], default='defo', max_length=4)),
            ],
            bases=('Users.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='academicYear',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(default='Choose department', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='Enter email', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='gradeSheet',
            field=models.FileField(default='null', upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='Enter password', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default='Enter phone number', max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='user',
            name='programRequest',
            field=models.CharField(choices=[('per', 'Perach'), ('ifk', 'Ifak'), ('def', 'None')], default='defo', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='Enter last name', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='Enter name', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userStatus',
            field=models.CharField(default='ACTIVE', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(default='Student', max_length=20),
        ),
    ]
