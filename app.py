from flask import Flask, render_template, request, redirect

def badge_class(status):
    status = status.lower()
    mapping = {
        "assigned": "badge-assigned",
        "in progress": "badge-inprogress",
        "submitted": "badge-submitted",
        "under review": "badge-underreview",
        "remediation": "badge-remediation",
        "approved": "badge-approved",
        "rejected": "badge-rejected"
    }
    return mapping.get(status, "badge")  

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    # Dummy KPI data (later comes from MySQL)
    kpi_data = {
        "total_vendors": 25,
        "pending_reviews": 6,
        "high_risk": 3,
        "completed_assessments": 18
    }

    # Recent activity (dummy)
    activities = [
        {"vendor": "ABC Pvt Ltd", "action": "Assessment Submitted", "status": "Pending"},
        {"vendor": "XYZ Corp", "action": "Risk Approved", "status": "Approved"},
        {"vendor": "TechSoft", "action": "Remediation Required", "status": "High Risk"},
        {"vendor": "GlobalSys", "action": "Assessment Completed", "status": "Completed"}
    ]

    return render_template(
        "dashboard.html",
        **kpi_data,
        activities=activities
    )

@app.route("/vendors")
def vendors():

    risk_filter = request.args.get("risk")

    # Dummy vendor data
    all_vendors = [
        {"name": "ABC Pvt Ltd", "category": "IT", "risk": "High", "status": "Pending"},
        {"name": "XYZ Corp", "category": "Finance", "risk": "Low", "status": "Approved"},
        {"name": "TechSoft", "category": "Software", "risk": "Medium", "status": "Review"},
        {"name": "GlobalSys", "category": "Cloud", "risk": "High", "status": "Pending"},
    ]

    if risk_filter:
        vendors = [v for v in all_vendors if v["risk"] == risk_filter]
    else:
        vendors = all_vendors

    return render_template("vendors.html", vendors=vendors)

@app.route("/assessments")
def assessments():
    assessments = [
        {"id": 1, "vendor": "ABC Pvt Ltd", "type": "Security", "status": "Assigned"},
        {"id": 2, "vendor": "XYZ Corp", "type": "Compliance", "status": "Submitted"},
        {"id": 3, "vendor": "TechSoft", "type": "Financial", "status": "Under Review"},
    ]
    return render_template("assessments.html", assessments=assessments)


@app.route("/assessments/assign", methods=["GET", "POST"])
def assign_assessment():
    if request.method == "POST":
        # later save to MySQL
        return redirect("/assessments")

    return render_template("assign_assessment.html")


@app.route("/assessments/<int:assessment_id>")
def assessment_detail(assessment_id):
    assessment = {
        "id": assessment_id,
        "vendor": "ABC Pvt Ltd",
        "type": "Security",
        "status": "Under Review",
        "score": "75%"
    }
    return render_template("assessment_detail.html", assessment=assessment)

@app.route("/templates")
def templates_list():
    templates = [
        {"name": "Security Basic", "category": "Security", "count": 10},
        {"name": "Compliance Checklist", "category": "Compliance", "count": 15},
        {"name": "Financial Risk", "category": "Financial", "count": 8},
    ]
    return render_template("templates_list.html", templates=templates)


@app.route("/templates/create", methods=["GET", "POST"])
def create_template():
    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        questions = request.form["questions"]
        # later save into MySQL
        return redirect("/templates")

    return render_template("create_template.html")

@app.route("/reviews")
def review_queue():
    reviews = [
        {"id": 1, "vendor": "ABC Pvt Ltd", "type": "Security", "date": "10-Jan-2026", "status": "Submitted"},
        {"id": 2, "vendor": "XYZ Corp", "type": "Compliance", "date": "12-Jan-2026", "status": "Under Review"},
    ]
    return render_template("review_queue.html", reviews=reviews)


@app.route("/review/<int:review_id>")
def review_detail(review_id):
    review = {
        "id": review_id,
        "vendor": "ABC Pvt Ltd",
        "type": "Security Assessment",
        "status": "Under Review"
    }

    questions = [
        {"question": "Do you have ISO 27001 certification?", "answer": "Yes", "score": 10},
        {"question": "Is data encrypted at rest?", "answer": "Yes", "score": 8},
        {"question": "Do you perform regular backups?", "answer": "Partial", "score": 6},
    ]

    return render_template(
        "review_detail.html",
        review=review,
        questions=questions
    )

@app.route("/remediations")
def remediation_list():
    remediations = [
        {
            "id": 1,
            "vendor": "ABC Pvt Ltd",
            "finding": "No data encryption at rest",
            "severity": "High",
            "due": "30-Jan-2026",
            "status": "Open",
            "status_class": "open"
        },
        {
            "id": 2,
            "vendor": "XYZ Corp",
            "finding": "Backup policy not documented",
            "severity": "Medium",
            "due": "05-Feb-2026",
            "status": "In Progress",
            "status_class": "progress"
        }
    ]
    return render_template("remediation_list.html", remediations=remediations)


@app.route("/remediation/<int:remediation_id>")
def remediation_detail(remediation_id):
    remediation = {
        "id": remediation_id,
        "vendor": "ABC Pvt Ltd",
        "finding": "No data encryption at rest",
        "severity": "High",
        "action": "Enable encryption for all stored customer data",
        "due": "30-Jan-2026",
        "status": "In Progress"
    }
    return render_template("remediation_detail.html", remediation=remediation)


@app.route("/remediation/<int:remediation_id>/response")
def vendor_response(remediation_id):
    response = {
        "id": remediation_id,
        "vendor": "ABC Pvt Ltd",
        "finding": "No data encryption at rest",
        "status": "In Progress",
        "comment": "We have enabled AES-256 encryption for all databases. Final validation in progress."
    }
    return render_template("vendor_response.html", response=response)

@app.route("/renewals")
def renewals():
    renewals = [
        {
            "vendor": "ABC Pvt Ltd",
            "item": "Security Assessment",
            "date": "25-Jan-2026",
            "status": "Upcoming",
            "badge_class": "b-upcoming"
        },
        {
            "vendor": "XYZ Corp",
            "item": "Compliance Review",
            "date": "15-Jan-2026",
            "status": "Due",
            "badge_class": "b-due"
        },
        {
            "vendor": "TechSoft",
            "item": "Contract Renewal",
            "date": "05-Jan-2026",
            "status": "Overdue",
            "badge_class": "b-overdue"
        }
    ]

    return render_template("renewal_list.html", renewals=renewals)

@app.route("/reports")
def reports():
    reports = [
        {
            "vendor": "ABC Pvt Ltd",
            "assessment": "Security Assessment",
            "score": "72%",
            "status": "Approved",
            "date": "14-Jan-2026"
        },
        {
            "vendor": "XYZ Corp",
            "assessment": "Compliance Review",
            "score": "65%",
            "status": "Approved",
            "date": "12-Jan-2026"
        },
        {
            "vendor": "TechSoft",
            "assessment": "Financial Risk",
            "score": "55%",
            "status": "Pending"
        }
    ]

    return render_template("reports.html", reports=reports)

@app.route("/search")
def global_search():
    query = request.args.get("q", "").lower()

    # Dummy data
    vendors = [
        {"id": 1, "name": "ABC Pvt Ltd"},
        {"id": 2, "name": "XYZ Corp"},
        {"id": 3, "name": "TechSoft"}
    ]

    assessments = [
        {"id": 1, "name": "Security Assessment"},
        {"id": 2, "name": "Compliance Review"},
        {"id": 3, "name": "Financial Risk"}
    ]

    results = []

    # Search vendors
    for v in vendors:
        if query in v["name"].lower():
            results.append({"type": "Vendor", "name": v["name"], "id": v["id"]})

    # Search assessments
    for a in assessments:
        if query in a["name"].lower():
            results.append({"type": "Assessment", "name": a["name"], "id": a["id"]})

    return render_template("search_results.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)