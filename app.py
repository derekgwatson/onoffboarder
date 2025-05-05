from flask import Flask, jsonify, request, render_template
from services.employment_hero import get_active_employees
from services.google_workspace import get_group_members, remove_from_group


app = Flask(__name__)


@app.route("/")
def home():
    group_email = request.args.get("group", "all-staff@watsonblinds.com.au")
    active_emails = set(get_active_employees())
    group_members = set(get_group_members(group_email))

    to_remove = [
        email for email in group_members
        if email not in active_emails and not email.endswith("@watsonblinds.com.au")
    ]

    return render_template("dashboard.html", group=group_email,
                           members=group_members,
                           to_remove=to_remove,
                           active_emails=active_emails)


@app.route("/sync/group", methods=["POST"])
def sync_group():
    group_email = request.args.get("group", "all-staff@watsonblinds.com.au")
    dry_run = request.args.get("dry_run", "true").lower() == "true"  # default to dry run

    active_emails = set(get_active_employees())
    group_members = set(get_group_members(group_email))

    to_remove = [
        email for email in group_members
        if email not in active_emails and not email.endswith("@watsonblinds.com.au")
    ]

    if not dry_run:
        for email in to_remove:
            remove_from_group(group_email, email)

    return render_template("sync_result.html", group=group_email,
                           removed=to_remove, dry_run=dry_run)


if __name__ == "__main__":
    app.run(debug=True)
