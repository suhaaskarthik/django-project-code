from django.db import models
import datetime
from django.utils import timezone
from picklefield.fields import PickledObjectField
class sign_up_email(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default = 'password')
    username = models.CharField(max_length=200, default= 'username')
    pub_date = models.DateTimeField('date published', default=datetime.date.today())
    def __str__(self):
        return self.email

class Query(models.Model):
    tut = models.ForeignKey(sign_up_email, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=200, default = 'None')
    product_name = models.CharField(max_length=200)
    expectations = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=datetime.date.today())
    def __str__(self):
        return self.product_name
class Answers(models.Model):
    answer_question = models.ForeignKey(Query, on_delete=models.CASCADE)
    publisher  = models.CharField(max_length=200, default = 'None')
    answer = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=datetime.date.today())
    star_rating = models.CharField(default = '0', max_length = 2)
    def __str__(self):
        return self.answer

