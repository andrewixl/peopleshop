from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.text import force_text
from django.utils.translation import ugettext_lazy as _
from .models import Apparel, Picture, Shipping, Sizes, Colors, Contact

admin.site.register(Contact)

# Register your models here.
def get_picture_preview(obj):
    if obj.pk:
        return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.product_photo.url,
            title=obj.product_caption,
        )
    return _("(choose a picture and save and continue editing to see the preview)")
get_picture_preview.allow_tags = True
get_picture_preview.short_description = _("Picture Preview")


class PictureInline(admin.StackedInline):
    model = Picture
    extra = 0
    fields = ["get_edit_link", "product_caption", "product_photo", get_picture_preview]
    readonly_fields = ["get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if obj.pk:
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            )
        return _("(save and continue editing to create a link)")
    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True

class ShippingInline(admin.StackedInline):
    model = Shipping
    extra = 0
    fields = ["master_apparel_product", "shipping_method", "shipping_price",]

class SizeInline(admin.StackedInline):
    model = Sizes
    extra = 0
    fields = ["master_apparel_product", "size",]

class ColorInline(admin.StackedInline):
    model = Colors
    extra = 0
    fields = ["master_apparel_product", "color",]


@admin.register(Apparel)
class Apparel_ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["active", "onsale","product_type","product_name", "product_cover","product_gender_type", "product_brand", "product_price","real_brand_price","product_description",]
    inlines = [SizeInline, ColorInline, ShippingInline, PictureInline,]

@admin.register(Picture)
class Apparel_PictureAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["master_apparel_product", "product_caption", "product_photo", get_picture_preview]
    readonly_fields = [get_picture_preview]
