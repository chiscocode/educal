from django.contrib import admin


# Register your models here.
from .models import *
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('topic','project_topic_views','date_added')
    list_filter = ("topic",)
    prepopulated_fields={'slug': ('topic',)}
    search_fields = ['topic',]

admin.site.register(Proposal,ProposalAdmin)