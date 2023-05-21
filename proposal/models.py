from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Count
from django.conf import settings

# Create your models here.

class Proposal(models.Model):
    topic=models.CharField(max_length=2500, null=True)
    slug=models.SlugField(max_length=255, null=True)
    motivation=RichTextUploadingField(blank=True,null=True)
    introduction=RichTextUploadingField(blank=True,null=True)
    background_of_study=RichTextUploadingField(blank=True,null=True)
    statement_of_problem=RichTextUploadingField(blank=True,null=True)
    aim_and_objective_of_the_study=RichTextUploadingField(blank=True,null=True)
    methodology=RichTextUploadingField(blank=True,null=True)
    software_developement_tools=RichTextUploadingField(blank=True,null=True)
    scope_of_the_study=RichTextUploadingField(blank=True,null=True)
    significance_of_the_study=RichTextUploadingField(blank=True,null=True)
    project_topic_views=models.IntegerField(default=0)
    date_added= models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.topic