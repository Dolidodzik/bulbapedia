from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class HomePage(BaseModel):
    text = models.TextField(default="This text will be displayed on homepage of your site")

    def save(self, *args, **kwargs):
        # Checking if user didn't try to add more than one HomePage, just for safety
        if not self.pk and HomePage.objects.exists():
            raise ValidationError('There is can be only one HomePage instance, do not add more than one instance of this, you can edit an existing one as you want!')
        return super(HomePage, self).save(*args, **kwargs)
