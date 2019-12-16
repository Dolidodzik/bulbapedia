from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class HomePage(BaseModel):
    name = models.CharField(default="This will be displayed as header of your page, edit it in admin panel!", max_length=512)
    text = models.TextField(default="This text will be displayed on homepage of your site, edit it in admin panel! I will also give you here some really interesting lorem ipsum text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean gravida, orci non ultrices aliquam, lectus urna lobortis dui, in scelerisque augue turpis et turpis. Cras viverra, lectus et sodales tincidunt, mi justo egestas mi, nec porta enim nisl nec tellus. Integer a urna et enim mollis fringilla non eget ipsum. Fusce libero urna, tempor non commodo posuere, aliquam ut erat. Duis accumsan dictum erat. Morbi ullamcorper sem non venenatis pellentesque. Mauris et semper ante. Nam lacinia pellentesque iaculis. In vel dui augue. Nulla maximus neque a gravida tempus. Proin sodales bibendum dui et lacinia. Mauris vestibulum scelerisque risus vitae malesuada. Duis id lobortis diam.")

    def save(self, *args, **kwargs):
        # Checking if user didn't try to add more than one HomePage, just for safety
        if not self.pk and HomePage.objects.exists():
            raise ValidationError('There is can be only one HomePage instance, do not add more than one instance of this, you can edit an existing one as you want!')
        return super(HomePage, self).save(*args, **kwargs)
