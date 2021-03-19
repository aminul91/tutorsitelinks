from django.db import models

# Create your models here.
class user_info(models.Model):
    user_name = models.CharField(max_length=50,default="")
    pass_user = models.CharField(max_length=50,default="")
    user_email = models.EmailField()
    def __str__(self):
        return self.user_name

class tutorial_type(models.Model):
    type_name = models.CharField(max_length=50)
    type_value = models.IntegerField(default=0,primary_key = True)
    def __str__(self):
        return self.type_name

class language_type(models.Model):
    language_name = models.CharField(max_length=50)
    language_value = models.IntegerField(default=0,primary_key = True)
    def __str__(self):
        return self.language_name   

class links_db(models.Model):
    links_name = models.CharField(max_length=70,default="")
    links_path = models.CharField(max_length=300,default="")
    links_val = models.IntegerField(default=0,primary_key = True)
    type_value = models.ForeignKey(tutorial_type, on_delete=models.CASCADE)
    language_value = models.ForeignKey(language_type, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.links_path

class suggestion(models.Model):
    suggestor_name = models.CharField(max_length=50,default="anonymous")
    suggestion = models.CharField(max_length=200,default="")
    suggestion_value = models.IntegerField(default=0,primary_key = True)
    def __str__(self):
        return self.suggestion_value

