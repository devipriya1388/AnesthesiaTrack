Anesthesia Track

Anesthesia Record Management Web Application

Anesthesia Track is a web application built to support healthcare professionals in efficiently managing anesthesia-related patient records. It streamlines the documentation of patient data, procedure notes, vitals, and post-operative care tracking.


---

 Key Features

 User Interface & Authentication

Secure Login: Simple and responsive login page using Tailwind CSS and Flask.

Patient Registration: Structured form for demographic details, procedure type, vitals, allergies, etc.

Patient Records Viewer: View stored data in card layout format.

Doctor Notes Section: Authorized users can add anesthesia and post-op notes.

Submission Confirmation: A success screen after completing data entry.



---

 Tech Stack

Technology	Purpose

HTML5 + CSS3	Page structure and styling
Tailwind CSS	Responsive design framework
Flask	Backend routing and templating
Python	Server-side programming


> Note: Flask and Python are inferred based on the use of Jinja templates.




---

 Folder Structure

anesthesia-track/
├── static/
│   └── favicon.ico               # App icon
├── templates/
│   ├── login.html                # Login interface
│   ├── form.html                 # Patient registration
│   ├── view.html                 # Data display page
│   └── success.html              # Submission confirmation
├── app.py                        # Main Flask script
├── README.md                     # Project documentation
└── requirements.txt              # Dependency file


---

 Getting Started

 Prerequisites

Python 3.x installed

Git version control system


 Installation Steps

git clone https://github.com/your-username/anesthesia-track.git
cd anesthesia-track

Install the required packages:

pip install flask

Start the server:

python app.py

Open your browser at:
http://127.0.0.1:5000/


---

 Advantages

Clean UI: Tailored to healthcare workflows with responsive layouts.

Modular & Extensible: Codebase allows easy feature upgrades.

Anesthesia-Specific: Tracks vital patient data relevant to anesthesia.

Cross-device Compatibility: Works on desktop, tablet, and mobile browsers.



---

 Planned Enhancements

Database Support: SQLite/PostgreSQL for persistent storage.

Role-Based Access: Doctor, Nurse, Admin permissions.

PDF Report Export: Generate downloadable summaries.

Vitals Charting: Show trends over time.

Dark Mode: For clinical comfort in low-light settings.



---

 License

This project is licensed under the MIT license
