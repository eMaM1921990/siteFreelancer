from siteFreelancer import settings

__author__ = 'emam'

import mailchimp

def get_mailchimp_api():
    return mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY) #your api key here

