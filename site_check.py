



import cloudscraper
import certifi
from urllib.parse import urlparse
from .helpers import check_ssl, check_whois, check_design_grammar

TRUSTED_DOMAINS = [
    "amazon.com", "google.com", "flipkart.com", "myntra.com", "apple.com",
    "microsoft.com", "snapdeal.com", "reliance.com", "tata.com", "ebay.com",
    "aliexpress.com", "etsy.com", "walmart.com", "target.com", "bestbuy.com",
    "newegg.com", "ajio.com", "tatacliq.com", "reliancedigital.in",
    "blinkit.com", "nykaa.com","meesho.com"
]

def analyze_website(url):
    score = 0
    details = []

    
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    
    if any(trusted in domain for trusted in TRUSTED_DOMAINS):
        score = 100
        details.append("✅ MASKTER'S CREDENTIALS CONFIRMED (TRUSTED SITE)")
        return {"url": url, "score": score, "details": details}
    else:
        details.append("❌ MASKTER'S CREDENTIALS NOT CONFIRMED (Not in trusted list)")

    
    if domain == "ajio.com":
        url = "https://www.ajio.com"
        domain = "www.ajio.com"

    
    try:
        scraper = cloudscraper.create_scraper()
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }
        response = scraper.get(url, headers=headers, timeout=10, verify=certifi.where())
        if response.status_code != 200:
            return {
                "url": url,
                "score": 0,
                "details": [f"❌ Site returned status code {response.status_code}"]
            }
    except Exception as e:
        return {
            "url": url,
            "score": 0,
            "details": [f"❌ Could not connect to site: {str(e)}"]
        }

    

    
    try:
        if check_ssl(url):
            score += 35
            details.append("🔒 Secure SSL certificate identified.")
        else:
            details.append("🔓 Secure SSL certificate NOT detected.")
    except Exception as e:
        details.append(f"⚠️ SSL check failed: {str(e)}")

   
    try:
        domain_info = check_whois(url)
        if domain_info.get("age_in_days", 0) > 180:
            score += 35
            details.append("✅ Domain age check passed (older than 6 months).")
        else:
            score += 10
            details.append("⚠️ Domain is too new (less than 6 months old).")
    except Exception as e:
        details.append(f"⚠️ WHOIS lookup failed: {str(e)}")

 
    try:
        grammar_ok = check_design_grammar(url)
        if grammar_ok:
            score += 30
            details.append("💼✨ Page looks professional and credible.")
        else:
            score += 5
            details.append("💼⚠️ Page lacks professional design or has grammar issues.")
    except Exception as e:
        details.append(f"⚠️ Design/grammar check failed: {str(e)}")

    score = min(score, 100)
    return {"url": url, "score": score, "details": details}
