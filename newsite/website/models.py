from ckeditor.fields import RichTextField
from django.db import models

import ckeditor



# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=255, verbose_name="Name")
    Email = models.EmailField(max_length=255, verbose_name="Email")
    Message = RichTextField(verbose_name="Message")

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Contacts"

class Service(models.Model):
    Serviceicon = models.CharField(max_length=50, verbose_name="Service Icon")
    Servicename = models.CharField(max_length=255, verbose_name="Service Name")
    Servicedescription = RichTextField(verbose_name="Service Description")

    def __str__(self):
        return self.Servicename

    class Meta:
        verbose_name_plural = "Services"

class Client(models.Model):
    Clientname = models.CharField(max_length=255, verbose_name="Client Name")
    Clientimage = models.ImageField(upload_to='client_images/', verbose_name="Client Image", blank=True, null=True)

    def __str__(self):
        return self.Clientname

    class Meta:
        verbose_name_plural = "Clients"

class Testimonial(models.Model):
    Testimonialname = models.CharField(max_length=255, verbose_name="Testimonial Name")
    Testimonialimage = models.ImageField(upload_to='testimonial_images/', verbose_name="Testimonial Image", blank=True, null=True)
    Testimonialtext = RichTextField(verbose_name="Testimonial Text")

    def __str__(self):
        return self.Testimonialname

    class Meta:
        verbose_name_plural = "Testimonials"

class Team(models.Model):
    Teamname = models.CharField(max_length=255, verbose_name="Team Name")
    Teamimage = models.ImageField(upload_to='team_images/', verbose_name="Team Image", blank=True, null=True)
    Teamdesignation = models.CharField(max_length=255, verbose_name="Team Designation")
    Teamtwitter = models.CharField(max_length=255, verbose_name="Team Twitter", blank=True)
    Teamfacebook = models.CharField(max_length=255, verbose_name="Team Facebook", blank=True)
    Teaminstagram = models.CharField(max_length=255, verbose_name="Team Instagram", blank=True)

    def __str__(self):
        return self.Teamname

    class Meta:
        verbose_name_plural = "Teams"
class Portfolio(models.Model):
    Projectname = models.CharField(max_length=255, verbose_name="Project Name")
    Projectdescription = RichTextField(verbose_name="Project Description")
    Projectlink = models.URLField(max_length=500, verbose_name="Project Link")
    Projectimage = models.ImageField(upload_to='portfolio_images/', verbose_name="Project Image", blank=True, null=True)
    Projectcasestudy = RichTextField(verbose_name="Project Case Study", blank=True)

    def __str__(self):
        return self.Projectname

    class Meta:
        verbose_name_plural = "Portfolios"