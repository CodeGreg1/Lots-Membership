from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'membership_number',
        'membership_status',
        'title',
        'forename',
        'surname',
        'initial',
        'address_line1',
        'address_line2',
        'address_line3',
        'town',
        'country',
        'postcode',
        'telephone_number',
        'email_address',
        'last_payment_received_date',
        'annual_subscription',
        'paid_to_lbm_issue',
        'pay_subs_to',
        'outstanding_giro_letter_number',
    )

    def custom_username(self, obj):
        return obj.username
    custom_username.short_description = 'Custom Username'

    def custom_email(self, obj):
        return obj.email
    custom_email.short_description = 'Custom Email'

admin.site.register(CustomUser, CustomUserAdmin)