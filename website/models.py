"""
Created by: Naresh Jonnala
Date: 19/08/2012
"""

from django.db import models
from PIL import Image
import sys
import time

class getSeconds():
    def __init__(self,p=None):
        t = time.time()
        if not p:
            if p == 'micro':
                return int(time.time()*1000000)
            elif p == 'mille':
                return int(time.time()*1000)
        return int(time.time())

DISABLE_CHOICES = ((1,'Enable'),(0,'Disable'))

class Category(models.Model):
#    id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length = 255, verbose_name ='Name')
    c_desc = models.TextField(null = True, verbose_name ='Description')
    status = models.IntegerField( default = 1, choices = DISABLE_CHOICES, verbose_name ='Status')
    sortorder = models.IntegerField( default = 10,  verbose_name ='sortorder')
    meta_desc = models.CharField(max_length = 255, null=True, blank=True, verbose_name ='Meta Desc')
    meta_key = models.CharField(max_length = 255, null=True, blank=True, verbose_name ='Meta Keywords')
    pg_title = models.CharField(max_length = 255, null=True, blank=True, verbose_name ='Page Title')
    #smallimage = models.ImageField(upload_to='images/', null=True, blank=True)
    bigimage = models.ImageField(upload_to='images/', null=True, blank=True)

    def __unicode__(self):
        if self.c_name:
            return '%s' % (self.c_name)
        
        if self.c_desc:
            return '%s' % (self.c_desc)


class Subcategory(models.Model):
#    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    c_name = models.CharField(max_length = 255, verbose_name ='Name')
    c_desc = models.TextField(null = True, verbose_name ='Description',blank = True)
    status = models.IntegerField( default = 1, choices = DISABLE_CHOICES, verbose_name ='Status')    
    sortorder = models.IntegerField( default = 10,  verbose_name ='sortorder')    
    def __unicode__(self):
        if self.c_name:
            return '%s-%s' % (self.category, self.c_name)
        
        if self.c_desc:
            return '%s' % (self.c_desc)


        
class Product(models.Model):
#    id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(Subcategory)
    product_name = models.CharField(max_length = 255)
    product_desc = models.TextField(null = True)
    prod_image = models.ImageField(upload_to = 'images/ProdImages', null = True, blank = True )
    inserteddate = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(max_length = 1, default = 1 ,choices = DISABLE_CHOICES)
    filepath = 'images/ProdImages/'
    
    def __unicode__(self):
        if self.product_name:
            return '%s' % (self.product_name)
        
        if self.product_desc:
            return '%s' % (self.product_desc)
            
    def save(self):
        sizes = {'thumbnail': {'height': 200, 'width': 180}}

        super(Product, self).save()
	if self.prod_image:
	    photopath = str(self.prod_image.path)  # this returns the full system path to the original file
	    im = Image.open(photopath)  # open the image using PIL
    
	    # pull a few variables out of that full path
	    photopath = photopath.replace('\\','/')
	    extension = photopath.rsplit('.', 1)[1]  # the file extension
	    
	    filename = photopath.rsplit('/', 1)[1].rsplit('.', 1)[0]  # the file name only (minus path or extension)
	    fullpath = photopath.rsplit('/', 1)[0]  # the path only (minus the filename.extension)
    
	    # use the file extension to determine if the image is valid before proceeding
	    if extension not in ['jpg', 'jpeg', 'gif', 'png']: sys.exit()
    
	    
	    # create thumbnail
	    im.thumbnail((sizes['thumbnail']['width'], sizes['thumbnail']['height']), Image.ANTIALIAS)
	    thumbname = filename + "_" + str(sizes['thumbnail']['width']) + "x" + str(sizes['thumbnail']['height']) + "." + extension
	    im.save(fullpath + '/' + thumbname)
	    self.prod_image = self.filepath + thumbname
    
	    super(Product, self).save()

class Aboutus(models.Model):
#    id = models.AutoField(primary_key=True)
    aboutus = models.TextField(verbose_name ='About Us')  
    
    
    def __unicode__(self):
        if self.aboutus:
            return '%s' % (self.aboutus)
        
