from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
CORS(app)

# CONNECT GOOGLE SHEETS
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",   # <-- rename your JSON file to this
    scope
)

client = gspread.authorize(creds)
sheet = client.open("Attendance").sheet1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    required = ["date", "house", "total", "present", "leave", "onduty", "submittedBy"]

    for f in required:
        if data.get(f) in [None, ""]:
            return jsonify({"msg": f"{f} missing"}), 400

    try:
        total   = int(data["total"])
        present = int(data["present"])
        leave   = int(data["leave"])
        onduty  = int(data["onduty"])
        sick    = int(data.get("sick", 0))
    except:
        return jsonify({"msg": "Invalid numbers"}), 400

    if present + leave + onduty != total:
        return jsonify({"msg": "Numbers don't add up! Check total ❌"}), 400

    formatted_date = datetime.strptime(data["date"], "%Y-%m-%d").strftime("%d-%m-%Y")
    current_time   = datetime.now().strftime("%I:%M %p")

    row = [
        formatted_date,
        current_time,
        data["house"],
        total,
        present,
        leave,
        data.get("leaveNames", ""),
        onduty,
        data.get("ondutyNames", ""),
        sick,
        data.get("sickNames", ""),
        data["submittedBy"]
    ]

    try:
        sheet.append_row(row)
        return jsonify({"msg": "Saved Successfully ✅"})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"msg": "Server Error ❌"}), 500


if __name__ == "__main__":
    app.run(debug=True)