from django.db import models

# 缺少主键的设置
class User(models.Model):
	userid = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 32)
	def __str__(self):
		return '%s(%s)' % (self.username , self.userid);
# Create your models here.
class Article(models.Model):
	articleid = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 63)
	author = models.ForeignKey('User' , on_delete = models.CASCADE)
	content = models.CharField(max_length = 255)
	def __str__(self):
		return '%s(%s)' % (self.title,self.articleid);
