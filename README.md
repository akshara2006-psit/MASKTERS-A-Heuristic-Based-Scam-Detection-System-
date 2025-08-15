TOPIC OF INVENTION
MASKTERS: A Heuristic-Based Scam Detection System for Internship and E-Commerce Websites Using Web Scraping and Domain Verification

FIELD / AREA OF THE INVENTION
The fields of cybersecurity, digital fraud detection, and information verification systems encompass this concept. In particular, it uses a rule-based heuristic algorithm to discover internship or e-commerce websites that are fraudulent, scammy, or unreliable. With an emphasis on safeguarding students and online shoppers, it uses secure scraping, domain analysis, SSL verification, WHOIS search, and web content analysis to identify criminal activity and flag suspicious platforms.

BACKGROUND OF THE INVENTION
Online scams that target consumers and job seekers have grown more complex in recent years. Students are drawn to fake internship websites by their imitation of trustworthy platforms, exaggerated compensation offers, and upfront costs. Similar to this, fraudulent websites advertise deals that, after being paid for, never come to pass. Although there are certain cybersecurity technologies available, the majority are not designed to combat domain-specific fraud, such as shopping or internship scams. To assess a website's legitimacy, there lack enough lightweight, adaptable systems that integrate web scraping, SSL, WHOIS validation, and content heuristics. In order to close this gap, "Maskters" offers an automated, rule-based fraud detection solution that is intended for practical use by individuals, small cybersecurity teams, and educational institutions.

. OBJECTIVE OF THE INVENTION
- To use non-AI, rule-based logic to identify bogus internship and retail websites.
- To analyze domain credibility through SSL, WHOIS, and grammar/design verification.
- To detect websites that require upfront payment or abuse official certificates such as MSME.
- To offer a score-based assessment that includes thorough justifications for users' comprehension.

- To help students and consumers avoid fraud through automated web content scanning.
- To incorporate the identification of trusted and banned domains into the analysis process


FEATURES OF THE INVENTION
- Heuristic Rule Engine: Uses predefined rules and keyword scans to detect scam-related phrases like “registration fee”, “MSME certified”, or “job guarantee”.
- Domain Analysis: Checks whether the website is on a known trusted or blacklisted domain list.
- SSL Verification: Confirms whether the website has a valid and secure SSL certificate using automated certificate checks.
- WHOIS Age Check: Retrieves domain information to determine if the site is newly registered (which is often a red flag).
- Grammar and Design Analysis: uses uniform sentences and design to assess the site's professionalism.
- Score-Based Result: Returns a numeric score (0–100) based on risk factors and detailed warnings or confirmations.
- Extensible Design: By simply updating configuration files or lists, new rules, keywords, and domains can be introduced.
- Web-based scraping: This method retrieves HTML and analyzes live content using tools like requests and cloudscraper.
- Fast and Lightweight: Completely rule-based and quick, it doesn't rely on bulky libraries like TensorFlow or outside AI APIs.
 

. WORKING METHODOLOGY
When a user enters a URL to be checked, the invention starts to function. First, the domain is extracted by the system using conventional URL parsing. After that, it determines whether the domain matches any entries in the blacklisted or trusted lists. A high score (around 100) and a relevant message are returned by the algorithm if the website is included in the trusted list (e.g., "linkedin.com," "amazon.com").


The scraper module uses `cloudscraper` to retrieve the page's content if the website is not on the trusted list, avoiding anti-bot tools like Cloudflare. Next, the material is examined for deceptive terms like "job guarantee," "non-refundable," and "registration fee."

At the same time, the system uses an SSL certificate validator to verify the website's security. The domain's age is then ascertained using a WHOIS checker. Domains that are new (less than six months old) are viewed with suspicion.


Next, the content is passed to a grammar and design checker, which flags websites with excessive grammatical mistakes or unprofessional design elements. These checks contribute positively or negatively to the final score.

The scoring engine combines all these factors:
- Domain reputation
- SSL presence
- Domain age
- Scam phrases in content
- Keyword repetition
- Professional appearance

After that, it provides a score out of 100 as well as thorough justification. A website is generally considered high-risk if its score is less than 60. The end-user can swiftly determine whether to trust a website owing to this clear, methodical assessment. Additionally, the system is readily expandable to accommodate future enhancements or additional detecting logic.

