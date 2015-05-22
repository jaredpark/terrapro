from django.contrib import admin
from accounts.models import Organization, Property, Contact, PropertyReport

class PropertyInline(admin.StackedInline):
    model = Property
    extra = 1

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class ReportInline(admin.StackedInline):
    model = PropertyReport
    extra = 1

class OrganizationAdmin(admin.ModelAdmin):
    inlines = [ PropertyInline, ContactInline]

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ ReportInline, ContactInline]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Contact)
admin.site.register(PropertyReport)