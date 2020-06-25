from django.contrib import admin
from . import models, hooks

admin.site.register(models.DomainRegistration)
admin.site.register(models.PendingDomainTransfer)
admin.site.register(models.ContactAddress)
admin.site.register(models.Contact)
admin.site.register(models.ContactRegistry)
admin.site.register(models.NameServer)
