from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def loan_approval():
    if request.method == "POST":
        # Retrieve form data
        name = request.form.get("name")
        property_owned = request.form.get("property")
        education = request.form.get("education")
        loan_amount = request.form.get("loan_amount")

        # Placeholder approval logic
        result = "Accepted" if int(loan_amount) < 50000 else "Rejected"
        
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True, port=8801)
