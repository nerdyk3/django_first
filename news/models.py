from django.db import models

class Reporter(models.Model):
    full_name= models.CharField(max_lenght=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date=models.DateFeild()
    headline=models.CharField(max_le
    nght=200)
    content=models.TextFeild()
    reporter= models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
