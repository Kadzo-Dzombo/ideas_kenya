from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    landing_page, login_page, dashboard, 
    startup_registration, delete_startup,
    StartupDetailView, startupUpdateView,
    investor_registration,  delete_investor,
    InvestorDetailView, investorUpdateView,
    ActiveStartups, PendingStartups, DeclinedStartups,
    ActiveInvestors, PendingInvestors, DeclinedInvestors,
    contact_page, Inquiries, InquiryDetailView, delete_inquiry,
    our_startups, about_us, help_page, interests, intro
)

app_name = 'core'

urlpatterns = [
    path('', landing_page, name='home'),
    path('admin/login/', login_page, name='login'),
    path('intro/', intro, name='intro'),
    path('our-startups/', our_startups, name='startups'),
    path('who-we-are/', about_us, name='about'),
    path('how-we-can-help/', help_page, name='help'),
    path('our-interests', interests, name='interests'),
    path('admin/', dashboard, name='dashboard'),
    path('contact-us/', contact_page, name='contact'),
    path('admin/inquiries/', Inquiries.as_view(), name='inquiry'),
    path('admin/inquiry/delete/<slug>', delete_inquiry, name='delete-inquiry'),
    path('admin/inquiry/view/<slug>', InquiryDetailView.as_view(), name='view-inquiry'),
    path('logout', LogoutView.as_view(), name='logout'),
    # startups
    path('register-startup/', startup_registration, name='register-startup'),
    path('admin/startups/active/', ActiveStartups.as_view(), name='active-startups'),
    path('admin/startups/pending/', PendingStartups.as_view(), name='pending-startups'),
    path('admin/startups/declined/', DeclinedStartups.as_view(), name='declined-startups'),
    path('admin/startup/update/<slug>', startupUpdateView, name='update-startup'),
    path('admin/startup/<slug>/', StartupDetailView.as_view(), name='startup-detail-view'),
    path('admin/startup/<slug>/delete/', delete_startup, name="delete-startup"),
    # investors
    path('register-investor/', investor_registration, name='register-investor'),
    path('admin/investors/active/', ActiveInvestors.as_view(), name='active-investors'),
    path('admin/investors/pending/', PendingInvestors.as_view(), name='pending-investors'),
    path('admin/investors/declined/', DeclinedInvestors.as_view(), name='declined-investors'),
    path('admin/investor/update/<slug>', investorUpdateView, name='update-investor'),
    path('admin/investor/<slug>/', InvestorDetailView.as_view(), name='investor-detail-view'),
    path('admin/investor/<slug>/delete/', delete_investor, name="delete-investor"),
    
]