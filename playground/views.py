from django.core.mail import send_mail, mail_admins,EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    # try:
    #     # message = EmailMessage('subject', 'message', 
    #     #                        'info@admin.com',['bob@admin.com'])
    #     # message.attach_file()
    #     # message.send()

    #     message = BaseEmailMessage(
    #         template_name ='emails/send_mail.html',
    #         context = {'name': 'Abel'}
    #     )
    #     message.send(['abel@admin.com'])


    # except BadHeaderError:
    #     pass

    notify_customers.delay('hello')
    return render(request, 'emails/hello.html', {'name': 'Mosh'})
