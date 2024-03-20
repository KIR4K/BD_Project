from django.contrib import admin

from .models import Client, Passport




from loan.models import Loan

class CreditInline(admin.TabularInline):
    model = Passport
    extra = 0

class PassportInline(admin.TabularInline):
    model = Loan
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    inlines = [PassportInline,CreditInline]

admin.site.register(Client,ClientAdmin)
admin.site.register(Passport)
