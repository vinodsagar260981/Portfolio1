from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline
from . models import About, Category, Home, Portfolio, Skills, Profile

# Register your models here.
admin.site.register(Home)


#About 
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline
    ]

#Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


#Portfolio
admin.site.register(Portfolio)