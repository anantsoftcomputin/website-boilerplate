from django.contrib import admin

from .models import Contact, Service, Client, Testimonial, Team, Portfolio


class ContactAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['Servicename', 'Serviceicon']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['Clientname']
    list_filter = ['Clientname']


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['Testimonialname', 'Testimonialtext']
    list_filter = ['Testimonialname']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['Teamname', 'Teamdesignation']
    list_filter = ['Teamname']


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['Projectname', 'Projectlink','Projectimage','Projectcasestudy']
    list_filter = ['Projectname']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Portfolio, PortfolioAdmin)

# Register your models here.
