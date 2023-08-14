from django.db import models

class customerinfo(models.Model):#Used for customer submitting request and using application
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address= models.CharField(max_length=200)
    contact_no= models.CharField(max_length=10)
    pwd=models.CharField(max_length=10)
    # Other fields like address, contact details, etc.
    
    class Meta:
        db_table = "customerinfo"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class servicerequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    
    customer = models.ForeignKey(customerinfo, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50,default="user")
    request_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='media/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "servicerequest"
    
    def __str__(self):
        return f"Request #{self.id} - {self.customer} - {self.request_type}"
