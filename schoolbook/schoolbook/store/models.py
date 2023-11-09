from django.db import models


class book(models.Model):
    owner = models.CharField('owner', max_length=50)
    ownerscontact = models.CharField('ownerscontact', max_length=50, null = True )    
    name = models.CharField('name', max_length=50)
    price = models.CharField('price', max_length=10)
    description = models.TextField('description')
    author = models.CharField('author', max_length=50)
    year = models.CharField('year', max_length=4)
    publisher = models.CharField('publisher', max_length=50)
    status = models.CharField('status', max_length=10, null = True)
    image = models.ImageField(upload_to='store/static/images/', blank = True, null = True )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
