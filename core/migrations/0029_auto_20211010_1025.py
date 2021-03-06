# Generated by Django 3.2.7 on 2021-10-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20211010_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='investor_type',
            field=models.CharField(choices=[('Venture Capitalist', 'Venture Capitalist'), ('Angel Investor', 'Angel Investor'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='investor',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Declined', 'Declined'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='applicant_role',
            field=models.CharField(choices=[('founder', 'Founder'), ('co-founder', 'Co-founder'), ('employee', 'Employee')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_month',
            field=models.CharField(choices=[('February', 'February'), ('November', 'November'), ('May', 'May'), ('January', 'January'), ('April', 'April'), ('June', 'June'), ('October', 'October'), ('March', 'March'), ('September', 'September'), ('July', 'July'), ('August', 'August'), ('December', 'December')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='start_year',
            field=models.CharField(blank=True, choices=[('2010', '2010'), ('2020', '2020'), ('2014', '2014'), ('2007', '2007'), ('2009', '2009'), ('2006', '2006'), ('2021', '2021'), ('2003', '2003'), ('2005', '2005'), ('2019', '2019'), ('2015', '2015'), ('2017', '2017'), ('2012', '2012'), ('2004', '2004'), ('2008', '2008'), ('2011', '2011'), ('2016', '2016'), ('2018', '2018'), ('2013', '2013')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='startup_stage',
            field=models.CharField(choices=[('prototype', 'Prototype'), ('users', 'Users'), ('idea', 'Idea'), ('paying users', 'Paying Users')], max_length=100),
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Declined', 'Declined'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
    ]
