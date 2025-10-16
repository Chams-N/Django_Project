from django.contrib import admin
from .models import Conference,Submission

admin.site.site_header = "Conference Management Admin"
admin.site.site_title = "Conference Dashboard"
admin.site.index_title = "Welcome to Conference Management Admin"
#admin.site.register(Conference)
admin.site.register(Submission)

# Register your models here.


class submissionTabInline(admin.TabularInline):
    model = Submission    #the model to be displayed inline
    extra = 1              #number of extra forms to display) i chose 1 so 1form by 1form
    readonly_fields = ('submission_id',)
    #fields = ('title','keywords','payed','user_id','submission_date')
    can_delete = False
    show_change_link = True
    #we can add a fieldset to display only specific fields
    
    
class submissionStackInline(admin.StackedInline):
    model = Submission    #the model to be displayed inline
    extra = 1              #number of extra forms to display) i chose 1 so 1form by 1form
    readonly_fields = ('submission_id',)
    #fields = ('title','keywords','payed','user_id','submission_date')
    can_delete = False
    show_change_link = True
    #we can add a fieldset to display only specific fields
    
#decorators:
@admin.register(Conference)
#cutomisation of admin interface
class AdminPerson(admin.ModelAdmin):
    list_display = ('name','location','start_date', 'end_date','theme','duration')
    ordering = ('-start_date',) #descending order
    search_fields = ('name', 'theme')
    list_filter = ('theme', 'start_date')
    date_hierarchy = 'start_date'
    fieldsets = (
     ("Gneral Information",{
         'fields':('name','description','theme')
                            }),   
        ("Logistics",{
            'fields':('location','start_date','end_date')
                            }),   
    )
    readonly_fields = ('conference_id',)
    
    inlines = [submissionStackInline]
    
    def duration(self,obj):
        #calculate duration in days between start_date and end_date
        if obj.start_date and obj.end_date:
            return (obj.end_date - obj.start_date).days + 1  #inclusive of both start and end date
        return 'N/A'
    
    duration.short_description = 'Duration (days)'


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user_id', 'conference_id', 'submission_date', 'payed', 'short_abstract')
    list_editable = ('status', 'payed')
    ordering = ('-submission_date',)
    search_fields = ('title', 'keywords', 'user_id__username')
    list_filter = ('status', 'payed', 'conference_id', 'submission_date')
    
    fieldsets = (
        ("General Information", {
            'fields': ('submission_id', 'title', 'abstract', 'keywords')
        }),
        ("File and Conference", {
            'fields': ('paper', 'conference_id')
        }),
        ("Tracking", {
            'fields': ('status', 'payed', 'submission_date', 'user_id')
        }),
    )
    
    readonly_fields = ('submission_id',)
    
    def short_abstract(self, obj):
        """Truncate abstract to 50 characters for quick display"""
        if obj.abstract:
            return obj.abstract[:50] + '...' if len(obj.abstract) > 50 else obj.abstract
        return '-'
    short_abstract.short_description = 'Abstract Preview'
    
admin.site.unregister(Submission)
admin.site.register(Submission, SubmissionAdmin)