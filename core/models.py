import random
import string
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

STARTUP_STAGES = {
    ('idea', 'Idea'),
    ('prototype', 'Prototype'),
    ('users', 'Users'),
    ('paying users', 'Paying Users')
}

START_YEAR = {
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021')
}

START_MONTH = {
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
}

APPLICANT_TITLE = {
    ('co-founder', 'Co-founder'),
    ('founder', 'Founder'),
    ('employee', 'Employee'),
}


STATUS_CHOICES = {
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined')
}

INVESTOR_TYPE = {
    ('Venture Capitalist', 'Venture Capitalist'),
    ('Angel Investor', 'Angel Investor'),
    ('Other', 'Other')
}

CONTACT_USER = {
    ('Admin', 'Admin')
}

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = '{slug}-{randstr}'.format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_inquiry_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.subject)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = '{slug}-{randstr}'.format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class Startup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    web_address = models.CharField(max_length=100, null=True, blank=True)
    startup_pitch = models.TextField(max_length=1500)
    startup_stage = models.CharField(max_length=100, choices=STARTUP_STAGES)
    start_month = models.CharField(max_length=100, choices=START_MONTH)
    start_year = models.CharField(max_length=100, null=True, blank=True, choices=START_YEAR)
    incorporation = models.BooleanField(default=False)
    country = models.CharField(max_length=100, default='Kenya')
    city = models.CharField(max_length=100)
    applicant_title = models.CharField(max_length=100, null=True, blank=True)
    applicant_role = models.CharField(max_length=100, choices=APPLICANT_TITLE)
    applicant_email = models.CharField(max_length=100)
    linkedin_account = models.CharField(max_length=100, null=True, blank=True)
    applicant_bio = models.TextField(max_length=1500)
    startup_elevator_pitch = models.TextField(max_length=1500)
    motivation = models.TextField(max_length=1500) 
    application_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:startup-detail-view', kwargs={'slug': self.slug})

    def get_update_startup_url(self):
        return reverse('core:update-startup', kwargs={'slug': self.slug})

    def get_delete_startup_url(self):
        return reverse('core:delete-startup', kwargs={'slug': self.slug})

    def get_approve_startup_url(self):
        return reverse('core:startup-approved', kwargs={'slug': self.slug})

    def get_decline_startup_url(self):
        return reverse('core:startup-declined', kwargs={'slug': self.slug})


class Investor(models.Model):
    investor_type = models.CharField(max_length=100, choices=INVESTOR_TYPE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    linkedin_address = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=1500)
    experience = models.TextField(max_length=1500)
    reason = models.TextField(max_length=1500)
    application_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES ,default='Pending', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:investor-detail-view', kwargs={'slug': self.slug})

    def get_update_investor_url(self):
        return reverse('core:update-investor', kwargs={'slug': self.slug})

    def get_delete_investor_url(self):
        return reverse('core:delete-investor', kwargs={'slug': self.slug})

    def get_approve_investor_url(self):
        return reverse('core:investor_approved', kwargs={'slug': self.slug})

    def get_declined_investor_url(self):
        return reverse('core:investor_declined', kwargs={'slug': self.slug})


class MailList(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)


class Contact(models.Model):
    user = models.CharField(choices=CONTACT_USER, max_length=100)
    slug = models.SlugField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('core:view-inquiry', kwargs={'slug': self.slug})

    def get_delete_inquiry_url(self):
        return reverse('core:delete-inquiry', kwargs={'slug': self.slug})


def startup_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(startup_pre_save_receiver, sender=Startup)


pre_save.connect(startup_pre_save_receiver, sender=Investor)


def inquiry_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_inquiry_slug_generator(instance)

pre_save.connect(inquiry_pre_save_receiver, sender=Contact)