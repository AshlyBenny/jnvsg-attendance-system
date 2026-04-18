#  School Attendance Management System

A web-based Attendance Management System designed for managing **house-wise attendance** in a school environment.  
This system allows teachers to submit daily attendance records efficiently, with all data being stored and organized automatically in Google Sheets.

##  Live Application
🔗 https://jnvsgattendance.pythonanywhere.com

##  Project Description

This project was developed to simulate a real-world school scenario where students are divided into different houses (e.g., Red, Blue, Green, Yellow).  

Teachers are responsible for submitting attendance details for their respective houses. The system simplifies this process by providing a centralized web interface where attendance can be recorded and stored in real-time.

##  Key Features

-  Simple and clean attendance submission form  
-  House-wise attendance tracking system  
-  Automatic date and time recording  
-  Direct integration with Google Sheets  
-  Real-time data storage and access  
-  Fully deployed and accessible online  

##  Technologies Used

- **Frontend:** HTML  
- **Backend:** Flask (Python)  
- **Database:** Google Sheets (via API)  
- **Deployment:** PythonAnywhere  

##  System Workflow

1. Teacher opens the attendance website  
2. Selects/enters house and attendance details  
3. Submits the form  
4. Flask backend processes the request  
5. Current date and time are added automatically  
6. Data is stored in the connected Google Sheet  

##  Project Structure
app.py #Backend logic(Flask)
form.html #Attendance input form
index.html #Landing page 
requirements.txt #Required dependencies

## Data Management

- Attendance data is securely stored in Google Sheets  
- Each entry is recorded with timestamp and house details  
- The system ensures organized and structured data collection  

##  Future Improvements

- Role-based login system for teachers  
- Admin dashboard for monitoring attendance  
- Data analytics and visualization  
- Exportable attendance reports  

##  Author

**Ashly Benny**

##  Project Objective

This project demonstrates the practical implementation of:
- Web development using Flask  
- API integration (Google Sheets)  
- Real-time data handling  
- Deployment of a live web application  

 This system is designed as a real-world solution for efficient attendance management in schools.
