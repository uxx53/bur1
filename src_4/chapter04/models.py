from django.db import models
from django.forms import ModelForm
import datetime

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name



class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
    # fields = ['name', 'title', 'birth_date']
    # exclude = ['created']


