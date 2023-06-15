from django.db import models

STATE_CHOICE = ((
    ("Punjab", "Punjab"),
    ("Sindh", "Sindh"),
    ("KPK","KPK"),
    ("Karachi", "Karachi"),    
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to="pimage", blank= True) 
    rdoc = models.FileField(upload_to="rdoc", blank= True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    skills = models.TextField(max_length=100)
    experience = models.TextField(max_length=1000,     blank= True)
    education = models.TextField(max_length=1000,   blank= False)    
    projects = models.TextField(max_length=100, blank= True )
    achievements = models.TextField(max_length=100, blank   = True)
    hobbies = models.TextField(max_length=100, blank= False)  
    
    
    
    
    def __str__(self):
        return self.name
