


from flask import Flask, render_template, request
from utils.site_check import analyze_website
from utils.internship_check import analyze_internship_site  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    internship_result = None
    internship_url = ""
    ecommerce_url = ""

    if request.method == "POST":
        if 'check_url' in request.form:
            ecommerce_url = request.form.get("url")
            if ecommerce_url:
                if not ecommerce_url.startswith('http://') and not ecommerce_url.startswith('https://'):
                    ecommerce_url = 'https://' + ecommerce_url
                result = analyze_website(ecommerce_url)

        elif "check_internship" in request.form:
            internship_url = request.form.get("internship_url")
            if internship_url:
                if not internship_url.startswith('http://') and not internship_url.startswith('https://'):
                    internship_url = 'https://' + internship_url
                internship_result = analyze_internship_site(internship_url)

            if internship_result is None:
                internship_result = {
                    "url": internship_url,
                    "score": None,
                    "reasons": ["❌ Error analyzing internship site."]
                }

    
    if result is None:
        result = {"score": None, "details": []}
    if internship_result is None:
        internship_result = {"score": None, "reasons": []}

    return render_template(
        "index.html",
        result=result,
        internship_result=internship_result,
        internship_url=internship_url,
        ecommerce_url=ecommerce_url
    )

if __name__ == "__main__":
    app.run(debug=True)

