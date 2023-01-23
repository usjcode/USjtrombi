from django.db import models

# Create your models here.

class Trombinoscope(models.Model):
    year=models.CharField((""), max_length=50,primary_key=True)
    def __str__(self) -> str:
        return self.year
    
class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    color=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
    
    
class Role(models.Model):
    name=models.CharField(verbose_name=("description"), max_length=50,null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    def __str__(self):
        if self.category ==None:
            return self.name + " 00000"
        else:
            return self.name + self.category.name
        
        
        
        

    
    

    

class Member(models.Model):
    photo=models.ImageField(default="default.jpeg")
    firstname=models.CharField((""), max_length=50,null=True)
    lastname=models.CharField("",max_length=50,null=True)
    email=models.EmailField(null=True,blank=True)
    contact=models.IntegerField(null=True,blank=True)
    bio=models.TextField("",null=True,blank=True)
    trombinoscope=models.ForeignKey(Trombinoscope, on_delete=models.CASCADE,null=True)
    role=models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    
    


    
