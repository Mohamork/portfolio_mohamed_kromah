from django.contrib import admin
from .models import Project, Image, Tag

# -- Create the ImageInline field
class ProjectImageInline(admin.TabularInline) :
    model = Image
    extra = 1

# -- Create the projectadmin
class ProjectAdmin(admin.ModelAdmin) :
    list_display = (
        'title',
    )
    inLines = [ProjectImageInline]
    search_fields = (
        'title',
        'description'
    )
    list_filter = ('tags',)

# -- Create the tagadmin
class TagAdmin(admin.ModelAdmin) : 
    list_display = ('name',)
    search_fields = ('name',)


# -- Register the models
admin.site.register(Tag,TagAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Image)