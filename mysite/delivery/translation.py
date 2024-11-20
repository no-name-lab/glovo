from .models import Order
from modeltranslation.translator import TranslationOptions, register


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('delivery_address',)
