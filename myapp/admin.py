from django.contrib import admin
from .models import CompanyDetail

# Register your models here.

@admin.register(CompanyDetail)
class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['company_name','contact','image','employees','yearly_company_income']
