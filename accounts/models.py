from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from registration.signals import user_registered
from datetime import datetime
from utilities import urlify

from django.forms import ModelForm

from cms.models.fields import PlaceholderField

class Organization(models.Model):
	user = models.ForeignKey(User, unique=True) #each client has one user and the reverse
	org_name = models.CharField(default='',blank=True, null=True, max_length=120)
	phone = models.CharField(default='',blank=True, null=True, max_length=12)
	email = models.EmailField(default='',blank=True, null=True, max_length=80)
	address = models.CharField(default='',blank=True, null=True, max_length=120)
	city = models.CharField(default='',blank=True, null=True, max_length=120)
	state = models.CharField(default='',blank=True, null=True, max_length=120)
	zipcode = models.CharField(default='',blank=True, null=True, max_length=9)

	public = models.BooleanField(default=False,blank=True)
	
	class Meta:
		verbose_name = _('Organization')
		verbose_name_plural = _('Organizations')
		
	def __unicode__(self):
		return(self.org_name)

	def __str__(self):
		return(self.org_name)

	# def attrs(self):
	# 	out = []
	# 	for field in self._meta.fields:
	# 		out.extend([field.name, getattr(self, field.name)])
	# 	return(out)

	def user_registered_callback(sender, user, request, **kwargs):
		organization = Organization(user = user)
		organization.save()
		user.first_name = request.POST["first_name"]
		user.last_name = request.POST["last_name"]
		user.email = request.POST["email"]
		user.save()
 
	user_registered.connect(user_registered_callback)

class Property(models.Model):
	organization = models.ForeignKey(Organization, related_name = 'Properties')
	property_name = models.CharField(default='',blank=True, null=True, max_length=120)
	property_contact = models.CharField(default='',blank=True, null=True, max_length=120)
	property_phone = models.CharField(default='',blank=True, null=True, max_length=12)
	property_email = models.EmailField(default='',blank=True, null=True, max_length=80)
	property_address = models.CharField(default='',blank=True, null=True, max_length=120)
	property_city = models.CharField(default='',blank=True, null=True, max_length=120)
	property_state = models.CharField(default='',blank=True, null=True, max_length=120)
	property_zipcode = models.CharField(default='',blank=True, null=True, max_length=9)
	property_notes = models.TextField(default='',blank=True, null=True, max_length=400)

	# property_slug = urlify(property_name.value)

	class Meta:
		verbose_name = _('Property')
		verbose_name_plural = _('Properties')
		
	def __unicode__(self):
		return(self.property_address)

	def __str__(self):
		return(self.property_address)

class Contact(models.Model):
	organization = models.ForeignKey(Organization, related_name = 'Contacts')
	contact_property = models.ForeignKey(Property, related_name = 'Properties', blank=True, null=True)
	contact_name = models.CharField(default='',blank=True, null=True, max_length=120)
	contact_phone = models.CharField(default='',blank=True, null=True, max_length=12)
	contact_email = models.EmailField(default='',blank=True, null=True, max_length=80)
	contact_address = models.CharField(default='',blank=True, null=True, max_length=120)
	contact_city = models.CharField(default='',blank=True, null=True, max_length=120)
	contact_state = models.CharField(default='',blank=True, null=True, max_length=120)
	contact_zipcode = models.CharField(default='',blank=True, null=True, max_length=9)
	contact_notes = models.TextField(default='',blank=True, null=True, max_length=400)

	class Meta:
		verbose_name = _('Contact')
		verbose_name_plural = _('Contacts')
		
	def __unicode__(self):
		return(self.organization.org_name)

	def __str__(self):
		return(self.organization.org_name)

class PropertyReport(models.Model):
	report_property = models.ForeignKey(Property, related_name = 'Reports')
	document = models.FileField(upload_to = "propertyreports/uploads/")
	notes = models.TextField(default='',blank=True, null=True, max_length=400)
	date = models.DateField(blank=True, null=True)
	class Meta:
		verbose_name = _('Report')
		verbose_name_plural = _('Reports')
		
	def __unicode__(self):
		return(self.report_property.property_name)

	def __str__(self):
		return(self.report_property.property_name)

