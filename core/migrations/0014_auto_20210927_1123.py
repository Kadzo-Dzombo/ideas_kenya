# Generated by Django 3.2.7 on 2021-09-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210927_1049'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MailList',
        ),
        migrations.AlterField(
            model_name='investor',
            name='investor_type',
            field=models.CharField(choices=[('Other', 'Other'), ('Angel Investor', 'Angel Investor'), ('Venture Capitalist', 'Venture Capitalist')], max_length=100),
        ),
        migrations.AlterField(
            model_name='investor',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='applicant_title',
            field=models.CharField(choices=[('employee', 'Employee'), ('co-founder', 'Co-founder'), ('founder', 'Founder')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('October', 'October'), ('August', 'August'), ('April', 'April'), ('February', 'February'), ('December', 'December'), ('September', 'September'), ('May', 'May'), ('November', 'November'), ('January', 'January'), ('July', 'July'), ('June', 'June'), ('March', 'March')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_year',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2020', '2020'), ('2018', '2018'), ('2019', '2019')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('paying users', 'Paying Users'), ('idea', 'Idea'), ('users', 'Users'), ('prototype', 'Prototype')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
    ]
