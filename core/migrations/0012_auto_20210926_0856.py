# Generated by Django 3.2.7 on 2021-09-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210923_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='active',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='active',
        ),
        migrations.AlterField(
            model_name='investor',
            name='investor_type',
            field=models.CharField(choices=[('Angel Investor', 'Angel Investor'), ('Other', 'Other'), ('Venture Capitalist', 'Venture Capitalist')], max_length=100),
        ),
        migrations.AlterField(
            model_name='investor',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('July', 'July'), ('March', 'March'), ('August', 'August'), ('April', 'April'), ('September', 'September'), ('January', 'January'), ('November', 'November'), ('December', 'December'), ('June', 'June'), ('February', 'February'), ('May', 'May'), ('October', 'October')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_year',
            field=models.CharField(blank=True, choices=[('2018', '2018'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('idea', 'Idea'), ('paying users', 'Paying Users'), ('prototype', 'Prototype'), ('users', 'Users')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
    ]
