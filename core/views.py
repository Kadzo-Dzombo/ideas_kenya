import csv
from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponse
from .forms import (
    LoginForm, ContactForm,
    StartupModelForm, InvestorModelForm,
    StartupEditForm, InvestorEditForm, MailListForm
)
from .models import Startup, Investor, Contact, MailList
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import DetailView, ListView

User = get_user_model()

def landing_page(request):
    form = MailListForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'You have successfully subscribed to our newsletter')
        return redirect('/')
    return render(request, 'index.html', {'form': form})


def our_startups(request):
    return render(request, 'admin/startups.html', {})


def about_us(request):
    return render(request, 'about.html', {})


def help_page(request):
    return render(request, 'help.html', {})


def interests(request):
    return render(request, 'interest.html', {})


def intro(request):
    return render(request, 'intro.html', {})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your message was sent successfully.')
        return redirect('core:home')
    return render(request, 'contact-page.html', {'form': form})


def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully signed in')
            return redirect('core:dashboard')
        else:
            messages.warning(request, 'Invalid username or password')
    return render(request, 'admin/login.html', {'form': form})

# registration views
def startup_registration(request):
    form = StartupModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your application was successful.')
        return redirect('core:home')
    print('form invalid')
    return render(request, 'admin/startup-application.html', {'form': form})


def investor_registration(request):
    form = InvestorModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your application was successful.')
        return redirect('core:home')
    print('form invalid')
    return render(request, 'admin/investor-application.html', {'form': form})


def dashboard(request):
    user = request.user
    if user is None:
        return redirect('/admin/login/')
    contact = Contact.objects.all()
    active_count = Startup.objects.filter(status='Approved').count()
    pending_count = Startup.objects.filter(status='Pending').count()
    declined_count = Startup.objects.filter(status='Declined').count()
    active_investor_count = Investor.objects.filter(status='Approved').count()
    pending_investor_count = Investor.objects.filter(status='Pending').count()
    declined_investor_count = Investor.objects.filter(status='Declined').count()
    unread_inquiry = Contact.objects.filter(read=False).count()
    context = {
        'contact': contact,
        'active_count': active_count,
        'pending_count': pending_count,
        'declined_count': declined_count,
        'active_investor_count': active_investor_count,
        'pending_investor_count': pending_investor_count,
        'declined_investor_count': declined_investor_count,
        'unread_inquiry': unread_inquiry
    }
    return render(request, 'admin/dashboard.html', context)

# detail views
class StartupDetailView(DetailView):
    model = Startup
    template_name = 'admin/startup-detail-view.html'


class InvestorDetailView(DetailView):
    model = Investor
    template_name = 'admin/investor-detail-view.html'


# status update views
def startup_approved(request, slug):
    startup_object = get_object_or_404(Startup, slug=slug)
    startup_object.status = 'Approved'
    startup_object.save()
    messages.success(request, 'Status updated successfully')
    return redirect('/admin/startups/active/')


def startup_declined(request, slug):
    startup_object = get_object_or_404(Startup, slug=slug)
    startup_object.status = 'Declined'
    startup_object.save()
    messages.success(request, 'Status updated successfully')
    return redirect('/admin/startups/declined/')


def investor_approved(request, slug):
    investor = get_object_or_404(Investor, slug=slug)
    investor.status = 'Approved'
    investor.save()
    messages.success(request, 'Status updated successfully')
    return redirect('/admin/investors/active/')


def investor_declined(request, slug):
    investor = get_object_or_404(Investor, slug=slug)
    investor.status = 'Declined'
    investor.save()
    messages.success(request, 'Status updated successfully')
    return redirect('/admin/investors/declined/')


# object update views

def startupUpdateView(request, slug):
    startup_obj = get_object_or_404(Startup, slug=slug)
    form = StartupEditForm(request.POST or None, instance=startup_obj)

    if form.is_valid():
        form.save()
        print('saved')
        messages.success(request, 'Startup Status successfully updated.')
        return redirect('core:dashboard')
    print('form not valid')

    context = {
        'object': startup_obj,
        'form': form
    }
    return render(request, 'admin/startup-update-view.html', context)


def investorUpdateView(request, slug):
    investor_obj = get_object_or_404(Investor, slug=slug)
    form = InvestorEditForm(request.POST or None, instance=investor_obj)

    if form.is_valid():
        form.save()
        print('saved')
        messages.success(request, 'Investor Status successfully updated.')
        return redirect('core:dashboard')
    print('form not valid')

    context = {
        'object': investor_obj,
        'form': form
    }
    return render(request, 'admin/investor-update-view.html', context)


# delete views
def delete_startup(request, slug):
    startup_object = get_object_or_404(Startup, slug=slug)
    startup_object.delete()
    messages.success(request, 'Record was deleted successfully')
    return redirect('core:dashboard')


def delete_investor(request, slug):
    investor_object = get_object_or_404(Investor, slug=slug)
    investor_object.delete()
    messages.success(request, 'Record was deleted successfully')
    return redirect('core:dashboard')


class Inquiries(ListView):
    model = Contact
    queryset = Contact.objects.all()
    template_name = 'admin/inquiries.html'


class InquiryDetailView(DetailView):
    model = Contact
    template_name = 'admin/inquiry-detail-view.html'

    def get_object(self, *args, **kwargs):
        inquiry_slug = self.kwargs.get('slug')
        if inquiry_slug:
            inquiry_query = Contact.objects.filter(slug=inquiry_slug)
            if inquiry_query.exists():
                inquiry_object = inquiry_query.first()
                inquiry_object.read = True
                inquiry_object.save()
            return inquiry_object
        raise Http404


def delete_inquiry(request, slug):
    inquiry_object = get_object_or_404(Contact, slug=slug)
    inquiry_object.delete()
    messages.success(request, 'Inquiry was deleted successfully')
    return redirect('core:dashboard')


# list views active, pending, declined
class ActiveStartups(ListView):
    model = Startup
    queryset = Startup.objects.filter(status='Approved')
    template_name = 'admin/active-startups.html'

class PendingStartups(ListView):
    model = Startup
    queryset = Startup.objects.filter(status='Pending')
    template_name = 'admin/pending-startups.html'

class DeclinedStartups(ListView):
    model = Startup
    queryset = Startup.objects.filter(status='Declined')
    template_name = 'admin/declined-startups.html'

class ActiveInvestors(ListView):
    model = Investor
    queryset = Investor.objects.filter(status='Approved')
    template_name = 'admin/active-investors.html'

class PendingInvestors(ListView):
    model = Investor
    queryset = Investor.objects.filter(status='Pending')
    template_name = 'admin/pending-investors.html'

class DeclinedInvestors(ListView):
    model = Investor
    queryset = Investor.objects.filter(status='Declined')
    template_name = 'admin/declined-investors.html'


# exports
class MailList(ListView):
    model = MailList
    template_name = 'admin/mail-list.html'


def export_mail_list(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email'])

    for receipient in MailList.objects.all().values_list('name', 'email'):
        writer.writerow(receipient)

    response['Content-Disposition'] = 'attachment; filename="mail-list.csv"'

    return response


def export_startup_list(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Name', 'Web Address', 'Startup Pitch', 'Startup Stage', 'Startup Month', 'Startup Year', 'Is Incorporated', 'Country', 'City', 'Applicant title', 'Applicant Role', 'Bio', 'Elevator Pitch', 'Motivation', 'Application Date'])

    for startup in Startup.objects.filter(status='Approved').values_list('name', 'web_address', 'startup_pitch', 'startup_stage', 'start_month', 'start_year', 'incorporation', 'country', 'city', 'applicant_title', 'applicant_role', 'applicant_bio', 'startup_elevator_pitch', 'motivation', 'application_date'):
        writer.writerow(startup)

    response['Content-Disposition'] = 'attachment; filename="startups.csv"'

    return response


def export_investor_list(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Type','Firstname', 'Lastname', 'Email Address', 'Linkedin Address', 'Country', 'City', 'Employement Status', 'Bio', 'Experience', 'Motivation', 'Application Date'])

    for investor in Investor.objects.filter(status='Approved').values_list('investor_type', 'name', 'surname', 'email', 'linkedin_address', 'country', 'city', 'employment_status', 'bio', 'experience', 'reason', 'application_date'):
        writer.writerow(investor)

    response['Content-Disposition'] = 'attachment; filename="investors.csv"'

    return response