from django.db import models

# Create your models here.
class Course(models.Model):
	course_code = models.CharField(max_length=20)
	semester = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.course_code

	class Meta:
		verbose_name_plural = "courses"