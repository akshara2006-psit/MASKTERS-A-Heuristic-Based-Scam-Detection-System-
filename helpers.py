

import ssl
import socket
import whois
import requests
from datetime import datetime

def check_ssl(url):
    try:
        hostname = url.replace("http://", "").replace("https://", "").split("/")[0]
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(5)
            s.connect((hostname, 443))
        return True
    except Exception:
        return False

def check_whois(url):
    try:
        hostname = url.replace("http://", "").replace("https://", "").split("/")[0]
        domain = whois.whois(hostname)
        
        
        creation_date = domain.creation_date
        expiration_date = domain.expiration_date
        
        if creation_date and expiration_date:
           
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0]
                
            age = (expiration_date - creation_date).days
            return {"age_in_days": age}
        else:
        
            if creation_date:
                if isinstance(creation_date, list):
                    creation_date = creation_date[0]
                age = (datetime.now() - creation_date).days
                return {"age_in_days": age}
        
        return {}
    except Exception as e:
        print(f"WHOIS error: {str(e)}")
        return {}

def check_design_grammar(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page = requests.get(url, timeout=10, headers=headers)
        text = page.text.lower()
        
  
        has_placeholder = any(phrase in text for phrase in ["lorem ipsum", "dummy text", "placeholder", "text here"])
        has_content = len(text) > 500
        
        
        has_cart = any(phrase in text for phrase in ["add to cart", "shopping cart", "checkout", "buy now", "purchase"])
        has_contact = any(phrase in text for phrase in ["contact us", "support", "customer service", "help center"])
        has_policy = any(phrase in text for phrase in ["privacy policy", "terms of service", "return policy", "shipping"])
        
        
        score = 0
        if not has_placeholder:
            score += 1
        if has_content:
            score += 1
        if has_cart:
            score += 1
        if has_contact:
            score += 1
        if has_policy:
            score += 1
            
        return score >= 3  
    except Exception as e:
        print(f"Design check error: {str(e)}")
        return False

def check_suspicious_pricing(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page = requests.get(url, timeout=10, headers=headers)
        text = page.text.lower()
        
       
        suspicious_patterns = [
            "90% off", "80% off", "70% off", 
            "free shipping worldwide",
            "clearance sale",
            "going out of business"
        ]
        
        for pattern in suspicious_patterns:
            if pattern in text:
                return False  
                
        return True  
    except:
        return True 