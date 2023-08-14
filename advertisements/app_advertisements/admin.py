from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [

            'id','title' ,'description','price','auction','created_date' ,'updated_date' 
    ]
    list_filter = ['auction','created_at']
    actions = ['make_auction_is_false','make_auction_is_true']

    fieldsets = (
        (
            'Общее',
            (
                {
                'fields': ('title','description')
                }
            )

        ),
        (
            'Финансы',
            (
                {
                    'fields': ('price','auction'),
                    'classes':['collapse']
                }
            )
        )
    )

    @admin.action(description='убрать возможность аукциона')
    def make_auction_is_false(self,request ,queryset):
        queryset.update(auction = False)
    @admin.action(description='добавить возможность аукциона')
    def make_auction_is_true(self,request ,queryset):
        queryset.update(auction = True)
admin.site.register(Advertisement,AdvertisementAdmin)
