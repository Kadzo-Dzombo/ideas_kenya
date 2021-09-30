from django.shortcuts import render, redirect, get_object_or_404, Http404
from .forms import (
    LoginForm, ContactForm,
    StartupModelForm, InvestorModelForm,
    StartupEditForm, InvestorEditForm,
    EditStartupStatusForm
)
from .models import Startup, Investor, Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import DetailView, ListView

User = get_user_model()

def landing_page(request):
    return render(request, 'index.html', {})


def our_startups(request):
    return render(request, 'startups.html', {})


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
    return render(request, 'login.html', {'form': form})

# registration views
def startup_registration(request):
    form = StartupModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your application was successful.')
        return redirect('core:home')
    print('form invalid')
    print(form)
    return render(request, 'startup-application.html', {'form': form})


def investor_registration(request):
    form = InvestorModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your application was successful.')
        return redirect('core:home')
    print('form invalid')
    return render(request, 'investor-application.html', {'form': form})


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
    return render(request, 'dashboard.html', context)

# detail views
class StartupDetailView(DetailView):
    model = Startup
    template_name = 'startup-detail-view.html'


class InvestorDetailView(DetailView):
    model = Investor
    template_name = 'investor-detail-view.html'

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
    return render(request, 'startup-update-view.html', context)


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
    return render(request, 'investor-update-view.html', context)


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
    template_name = 'inquiries.html'


class InquiryDetailView(DetailView):
    model = Contact
    template_name = 'inquiry-detail-view.html'

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
    template_name = 'active-startups.html'

class PendingStartups(ListView):
    model = Startup
    queryset = Startup.objects.filter(status='Pending')
    template_name = 'pending-startups.html'

class DeclinedStartups(ListView):
    model = Startup
    queryset = Startup.objects.filter(status='Declined')
    template_name = 'declined-startups.html'

class ActiveInvestors(ListView):
    model = Investor
    queryset = Investor.objects.filter(status='Approved')
    template_name = 'active-investors.html'

class PendingInvestors(ListView):
    model = Investor
    queryset = Investor.objects.filter(status='Pending')
    template_name = 'pending-investors.html'

class DeclinedInvestors(ListView):
    model = Investor
    queryset = Investor.objects.filter(status='Declined')
    template_name = 'declined-investors.html'
