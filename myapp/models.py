from django.db import models

# Create your models here.
class CompanyDetail(models.Model):
    company_name = models.CharField(max_length=50)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='myapp/images')
    employees = models.IntegerField()
    yearly_company_income = models.IntegerField()