from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Apparel_Product(models.Model):
    product_type = "apparel"
    product_name = models.CharField(_("Name"), max_length=255)
    product_cover = models.ImageField( _("Album Cover (240px x 240px)"), upload_to='media/', default='media/None/no-img.jpg')
    product_gender_type = models.CharField(_("Gender"),max_length=256, choices=[('men', 'Male'), ('women', 'Female'), ('unisex', 'Unisex')])
    product_brand = models.CharField(_("Brand"),max_length=25)
    product_description = models.CharField(_("Description"),max_length=500)
    product_price = models.CharField(_("Price"),max_length=500)
    real_brand_price = models.CharField(_("Real Brand Price"),max_length=500)
    paypal_button = models.CharField(_("Real Brand Price"),max_length=750)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Apparel Product")
        verbose_name_plural = _("Apparel Products")

    def __str__(self):
        return self.product_name


@python_2_unicode_compatible
class Apparel_Picture(models.Model):
    master_apparel_product = models.ForeignKey(Apparel_Product, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
    product_caption = models.CharField(_("Caption"), max_length=255)
    product_photo = models.ImageField(_("Picture"), upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    def __str__(self):
        return self.product_caption

@python_2_unicode_compatible
class Apparel_Shipping(models.Model):
    master_apparel_product = models.ForeignKey(Apparel_Product, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
    shipping_method = models.CharField(_("Shipping Method"), max_length=255)
    shipping_price = models.CharField(_("Shipping Price"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Shipping Price")
        verbose_name_plural = _("Shipping Prices")

    def __str__(self):
        return self.shipping_price

@python_2_unicode_compatible
class Apparel_Sizes(models.Model):
    master_apparel_product = models.ForeignKey(Apparel_Product, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
    size = models.CharField(_("Size"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")

    def __str__(self):
        return self.size

@python_2_unicode_compatible
class Apparel_Colors(models.Model):
    master_apparel_product = models.ForeignKey(Apparel_Product, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
    color = models.CharField(_("Color"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return self.color
