from django.db import models
# ============================================================================ #
# Create your models here.


# ================================ BASE MODEL ================================ #

class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



    STATUS = (
        ('True', 'Available'),
        ('False', 'Not Available'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    shape = models.ImageField(blank=True, upload_to='images/')
    cover = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    url = models.CharField(max_length=555, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title