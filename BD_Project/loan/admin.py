from django.contrib import admin

from .models import Loan,Payment_Plan
admin.site.register(Loan)
admin.site.register(Payment_Plan)