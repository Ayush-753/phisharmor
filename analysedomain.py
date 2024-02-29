from urllib.parse import urlparse, parse_qs
import re
import ssl
import socket
import whois
from datetime import datetime


def analyze_url(url):
    parsed_url = urlparse(url)

    scheme = parsed_url.scheme
    domain = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query
    fragment = parsed_url.fragment
    query_params = parse_qs(parsed_url.query)

    is_phishing = False

    if scheme.lower() != 'https':
        is_phishing = True

    if re.search(r'\b(\w+)-(\w+)\b', domain):
        is_phishing = True

    if re.search(r'\blogin\b|\badmin\b|\bpassword\b', path, re.IGNORECASE):
        is_phishing = True
    
    sensitive_params = ['user', 'username', 'password', 'login']
    for param in sensitive_params:
        if param in query_params:
            is_phishing = True

    print(f"URL: {url}")
    print(f"Scheme: {scheme}")
    print(f"Domain: {domain}")
    print(f"Path: {path}")
    print(f"Query: {query}")
    print(f"Fragment: {fragment}")

    if query_params:
        print("Query Parameters:")
        for key, value in query_params.items():
            print(f"  {key}: {value}")

    if is_phishing:
        return "Phishing Alert: This URL may be a phishing attempt"
    else:
        return "No phishing indicators detected."


def check_ssl_certificate(domain):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
            if not cert["subjectAltName"]:
                return f"The domain {domain} does not have a valid SSL certificate. Phishing Alert: This URL may be a phishing attempt"
            else:
                return f"The domain {domain} has a valid SSL certificate"
    except Exception as e:
        return f"The domain {domain} does not have a valid SSL certificate. Phishing Alert: This URL may be a phishing attempt"


def check_domain_age(domain):
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            current_date = datetime.now()
            domain_age = (current_date - creation_date).days
            if domain_age>365:
                return f"The {domain} was registered {domain_age} days ago and might not be a Phishing Website"
            else:
                return f"The {domain} was registered recently around {domain_age} days ago and might be a Phishing Website"
        else:
            return None
    except whois.parser.PywhoisError as e:
        print(f'Error retrieving WHOIS information: {e}')

