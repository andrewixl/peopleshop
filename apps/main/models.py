from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.mail import send_mail
from django.conf import settings
import re
from django.utils.translation import ugettext_lazy as _

class ContactManager(models.Manager):
    def createContact(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['name']) < 3:
            results['status'] = False
            results['errors'].append('Name Must be at Least 3 Characters.')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = False
            results['errors'].append('Please Enter a Valid Email.')
        if len(postData['subject']) < 5:
            results['status'] = False
            results['errors'].append(
                'Please Enter a Valid Subject in Subject Line.')
        if len(postData['message']) < 10:
            results['status'] = False
            results['errors'].append('Message Must be at Least 10 Characters.')

        if results['status'] == True:
            results['errors'].append(
                'Your Message Has Successfully Been Sent.')
            results['person'] = Contact.objects.create(contact_name=postData['name'], contact_email=postData['email'], contact_subject=postData['subject'], contact_message=postData['message'])
            # send_mail(postData['subject'], postData['message'], 'admin@emgraymedia.gq', ['burger.andrewixl@gmail.com'], fail_silently=False)

            subject = postData['subject']
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Message:\n' + postData['message']
            recipient_list = ['admin@peopleshop.gq','info@peopleshop.gq', postData['email']]
            #recipient_list = ['andrew@emgraymedia.gq', 'emily@emgraymedia.gq', 'contact@emgraymedia.gq', postData['email']]
            html_message = '''<h4>Name: </h4>
                              <h4>{name}</h4>
                              <h4>Email: </h4>
                              <h4>{email}</h4>
                              <h4>Message: </h4>
                              <h4>{message}</h4>
                              <h5>This is a Copy of the Sent Message From the Contact Form on peopleshop.gq/contact</h5> '''.format(name=postData['name'], email=postData['email'], message=postData['message'])

            send_mail(subject, message, from_email, recipient_list,
                      fail_silently=False, html_message=html_message)
        return results

@python_2_unicode_compatible
class Contact(models.Model):
    contact_name = models.CharField(max_length=25)
    contact_email = models.CharField(max_length=50)
    contact_subject = models.CharField(max_length=75)
    contact_message = models.CharField(max_length=750)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContactManager()

    class Meta:
        verbose_name = _("Contact Response")
        verbose_name_plural = _("Contact Responses")

    def __str__(self):
        return self.contact_subject

class EmailManager(models.Manager):
    def createEmail(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = False
            results['errors'].append('Please Enter a Valid Email.')

        if results['status'] == True:
            results['errors'].append(
                'Your Message Has Successfully Been Sent.')
            results['person'] = Contact.objects.create(contact_name=postData['name'], contact_email=postData['email'], contact_subject=postData['subject'], contact_message=postData['message'])

            subject = "Thanks for Joining Our Newsletter!"
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Message:\n' + "Hello!"
            recipient_list = ['admin@peopleshop.gq','info@peopleshop.gq', postData['email']]
            html_message = '''<h4>Thanks for Joining Our Newsletter</h4>
                              <h4>We will start emailing you daily deals for hot apparel items on the site.</h4>
                              <h4>Below is a coupon code for your next purchase!</h4>
                              <h4>Code: </h4>
                              <h4>HJKA8D2</h4>
                              <h5>This is a Sent Message From the Newsletter Form on peopleshop.gq</h5> '''.format(name=postData['name'], email=postData['email'], message=postData['message'])

            send_mail(subject, message, from_email, recipient_list,
                      fail_silently=False, html_message=html_message)
        return results

@python_2_unicode_compatible
class Email(models.Model):
    newsletter_email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContactManager()

    class Meta:
        verbose_name = _("Newsletter Email")
        verbose_name_plural = _("Newsletter Emails")

    def __str__(self):
        return self.newsletter_email

@python_2_unicode_compatible
class Apparel(models.Model):
    product_type = models.CharField(_("Product Type"),max_length=256, choices=[('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')])
    product_name = models.CharField(_("Name"), max_length=255)
    product_cover = models.ImageField( _("Album Cover (240px x 240px)"), upload_to='media/', default='media/None/no-img.jpg')
    product_gender_type = models.CharField(_("Gender"),max_length=256, choices=[('men', 'Male'), ('women', 'Female'), ('unisex', 'Unisex')])
    product_brand = models.CharField(_("Brand"),max_length=25)
    product_description = models.CharField(_("Description"),max_length=1000)
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
class Picture(models.Model):
    master_apparel_product = models.ForeignKey(Apparel, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
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
class Shipping(models.Model):
    master_apparel_product = models.ForeignKey(Apparel, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
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
class Sizes(models.Model):
    master_apparel_product = models.ForeignKey(Apparel, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
    size = models.CharField(_("Size"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")

    def __str__(self):
        return self.size

@python_2_unicode_compatible
class Colors(models.Model):
    master_apparel_product = models.ForeignKey(Apparel, verbose_name=_("Apparel Product"), on_delete=models.CASCADE)
    color = models.CharField(_("Color"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return self.color
