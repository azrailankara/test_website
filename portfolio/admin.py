from django.contrib import admin
from .models import Skill, Project, Experience, Education, About

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_technologies', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)

    def get_technologies(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])
    get_technologies.short_description = 'Teknolojiler'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('position', 'company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'field', 'institution', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('institution', 'degree', 'field')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')

    def has_add_permission(self, request):
        # Sadece bir tane About kaydı olabilir
        if self.model.objects.exists():
            return False
        return True
