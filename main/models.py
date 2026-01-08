from django.db import models

# Create your models here.

# -- Create fields for the Tags 
class Tag(models.Model) :
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) :
        return self.name    

# -- Create fields for the Projects
class Project(models.Model) :
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    link = models.URLField(max_length=200,blank=True)

    def __str__(self) :
        return self.title
    
class Image(models.Model) :
    project = models.ForeignKey(Project,related_name='images', on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='project_images/') 

    def __str__(self) :
        return f'{self.project.title} Image'


