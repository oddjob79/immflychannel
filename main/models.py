from django.db import models

class Channel(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    language = models.CharField(max_length=2, null=False, blank=False)
    picture = models.ImageField(upload_to='images/')
    parent_channel = models.ForeignKey('self', null=True, blank=True, related_name='parent', on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Content(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    content = models.ImageField(upload_to='content/')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__lte=10.0), name='rating_lte_10.0',)
        ]

class ContentMeta(models.Model):
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=30, null=False, blank=False)
    meta_value = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return str(self.meta_key) + ': ' + str(self.meta_value)
