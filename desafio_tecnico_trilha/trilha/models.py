from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)    

class Trail(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    number_of_steps = models.PositiveIntegerField(default=0)

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(null=True)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name='steps')
    
    class Meta:
        #Impede que possua dois estepes em uma mesma trilha com a mesma orem
        constraints = [
            models.UniqueConstraint(
                fields=['trail', 'order'], 
                name='unique_step_order_in_trail'
            )
        ]

class Attachments(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE,  related_name='attachments')
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    video_duration = models.DurationField(blank=True, null=True)  # timedelta
    link = models.URLField(blank=True, null=True)
   

class Links(models.Model): 
    title = models.CharField(max_length=200)
    link = models.URLField()
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='links')

class ClientProgress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_progress')
    step = models.ForeignKey(Step, on_delete=models.CASCADE,  related_name='step_progress')
    trail = models.ForeignKey(Trail, on_delete=models.PROTECT, related_name='trail_progress')
    completed = models.BooleanField(default=False)