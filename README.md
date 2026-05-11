# JNV Attendance Management System

A simple attendance tracking website built for JNV South Goa — a residential central government school.
Previously deployed on PythonAnywhere for trial use and live testing.

---

## Why I built this

JNV is a residential school, so students stay on campus all year. Teachers have to take attendance multiple times a day — morning, evening, whenever needed — and it's done house-wise (Red, Blue, Green, Yellow).

The school administration wanted a quick digital way to handle this. So I built a simple website where teachers can open it on their phone or computer, fill in the attendance, and submit. All the data goes straight into a Google Sheet, so it can be checked from anywhere without needing to be physically present.

It's not the school's official system — teachers still maintain physical registers too. But this website is currently being used at JNV South Goa alongside those registers.

Since all JNV schools across India follow the same house system, this can work for any JNV with barely any changes.

---

## What it does

- Teachers fill a form with house and attendance details
- Date and time get recorded automatically on every submission
- Data is saved to Google Sheets and can be viewed from anywhere
- Works on mobile — no app to install, just open the link

---

## Built with

- HTML (frontend)
- Flask / Python (backend)
- Google Sheets API (to store data)
- PythonAnywhere (deployment)

---

## How it works

Teacher opens website → fills form → submits → Flask saves the entry to Google Sheets with a timestamp → admin can view it anytime from anywhere.

---

## Project files

```
├── app.py            # backend logic and Google Sheets connection
├── form.html         # the attendance form teachers fill
├── index.html        # home page
├── requirements.txt  # dependencies
```

---

## Running it locally

```bash
git clone https://github.com/AshlyBenny/jnvsg-attendance-system.git
cd jnvsg-attendance-system
pip install -r requirements.txt
python app.py
```

You'll need a Google Sheets API credentials file — set that up from Google Cloud Console and share your sheet with the service account email.

---

## What I'd add later

- A login system so each house teacher has their own access
- An admin view to see all houses at once
- Ability to export records as PDF or Excel
- Support for any JNV school to set it up for themselves

---

*Built by Ashly Benny · BenTech · For JNV South Goa*
