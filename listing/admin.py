from django.contrib import admin

from listing.models import Version,Image, Project

# class ImageInline(admin.TabularInline):
#     model = Image

# class VersionAdmin(admin.ModelAdmin):
#     inlines = [
#         ImageInline,
#     ]

# admin.site.register(Version, VersionAdmin)



class VersionInline(admin.StackedInline):
    model = Version
    extra = 2


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["name"]
    inlines = [VersionInline]



class ImageInline(admin.StackedInline):
    model = Image
    extra = 2
    #fields = ["reviewer", "comment"]

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    save_on_top = True
    #fields = ["painter", "title", "picture", get_picture_preview]
    #readonly_fields = [get_picture_preview]
    inlines = [ImageInline]