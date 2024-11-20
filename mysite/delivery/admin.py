from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ("id", "status", "client", "delivery_address", "created_at", "courier")
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(User)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Courier)
admin.site.register(Review)
