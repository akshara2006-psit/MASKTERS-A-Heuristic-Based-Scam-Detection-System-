

import re
import requests
from urllib.parse import urlparse

def analyze_internship_site(url, page_content=""):
    score = 100
    reasons = []

    
    if not page_content:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                return {
                    "url": url,
                    "score": 0,
                    "reasons": ["❌ Website is inaccessible or returned status code " + str(response.status_code)]
                }
            page_content = response.text
        except Exception as e:
            return {
                "url": url,
                "score": 0,
                "reasons": [f"❌ Error accessing site: {str(e)}"]
            }

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

   
    trusted_domains = [
        "linkedin.com", "internshala.com", "ycombinator.com", "naukri.com",
        "glassdoor.com", "indeed.com", "internship.aicte-india.org",
        "angel.co", "foundit.in", "devfolio.co", "letsintern.com",
        "careers.microsoft.com", "careers.google.com", "turing.com",
        "kaggle.com", "unstop.com", "firstnaukri.com", "futuremug.co.in",
        "hirect.in", "relevel.com", "goodinternships.in"
    ]
    if any(trusted in domain for trusted in trusted_domains):
        reasons.append("✅ Trusted domain (whitelisted). Minor checks skipped.")
        return {"url": url, "score": 95, "reasons": reasons}

    
    blacklisted_domains = [
        "internsavy.com", "internshiphub.in", "workfromhomecareer.com",
        "internshipswale.in", "careerboosters.online", "hiringcamp.in",
        "youthwork.in", "smartinternz.online", "virtualinternships.today",
        "techieinterns.pro", "stipend.in", "applyinternshipsnow.com"
    ]
    if domain in blacklisted_domains:
        score -= 50
        reasons.append("🚫 Domain is blacklisted as fake internship site.")

    
    suspicious_domain_keywords = [
        "internship", "apply", "job", "offer", "fast", "easy", "guaranteed",
        "codesoft", "instant", "free", "workfromhome"
    ]
    domain_penalty = 0
    for keyword in suspicious_domain_keywords:
        if keyword in domain:
            domain_penalty += 10
    if domain_penalty > 0:
        score -= domain_penalty
        reasons.append(f"⚠️ Domain contains suspicious keywords causing -{domain_penalty} points.")

    
    if len(domain) > 25:
        score -= 10
        reasons.append("🔍 Domain length suspiciously long.")
    generic_tlds = [".top", ".club", ".online", ".xyz", ".info", ".cc"]
    if any(domain.endswith(tld) for tld in generic_tlds):
        score -= 10
        reasons.append("⚠️ Domain uses suspicious TLD.")

    if not url.startswith("https://"):
        score -= 15
        reasons.append("🔓 Website is not using HTTPS.")

    
    lowered_content = page_content.lower()

    scam_phrases = [
        "registration fee", "training fee", "advance fee", "job guarantee",
        "certified by msme", "msme certified", "govt approved", "processing fee",
        "non-refundable", "pay to apply", "security deposit", "offer letter on payment",
        "instant offer", "immediate offer"
    ]
    scam_hits = [phrase for phrase in scam_phrases if phrase in lowered_content]
    if scam_hits:
        score -= 30
        reasons.append(f"💸 Scammy phrases found in content: {', '.join(scam_hits)}")

    scammy_words = ["stipend", "guaranteed", "advance fee", "pay", "offer", "instant", "earn", "job"]
    repeated_penalty = 0
    for word in scammy_words:
        count = lowered_content.count(word)
        if count > 3:
            repeated_penalty += (count - 3) * 3
    if repeated_penalty > 0:
        score -= repeated_penalty
        reasons.append(f"⚠️ Multiple repeated scam keywords causing -{repeated_penalty} points.")

    if re.search(r"(₹|\$|rs\.?|inr)\s?\d+", lowered_content):
        score -= 15
        reasons.append("💰 Detected direct money/payment requests.")

    if "linkedin" in lowered_content and "share" in lowered_content:
        score -= 10
        reasons.append("📣 Viral sharing on LinkedIn detected.")

    if len(lowered_content.strip()) < 4000:
        score -= 20
        reasons.append("⚠️ Content length suspiciously short (<4000 chars).")

    
    score = max(0, min(score, 100))

    return {"url": url, "score": score, "reasons": reasons}


