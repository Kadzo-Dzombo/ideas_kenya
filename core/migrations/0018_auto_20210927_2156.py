# Generated by Django 3.2.7 on 2021-09-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210927_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='investor',
            name='investor_type',
            field=models.CharField(choices=[('Other', 'Other'), ('Angel Investor', 'Angel Investor'), ('Venture Capitalist', 'Venture Capitalist')], max_length=100),
        ),
        migrations.AlterField(
            model_name='investor',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='applicant_role',
            field=models.CharField(choices=[('co-founder', 'Co-founder'), ('employee', 'Employee'), ('founder', 'Founder')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('October', 'October'), ('November', 'November'), ('February', 'February'), ('January', 'January'), ('July', 'July'), ('June', 'June'), ('March', 'March'), ('May', 'May'), ('April', 'April'), ('August', 'August'), ('December', 'December'), ('September', 'September')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('idea', 'Idea'), ('paying users', 'Paying Users'), ('users', 'Users'), ('prototype', 'Prototype')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=100),
        ),
    ]
