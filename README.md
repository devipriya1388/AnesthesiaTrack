Anesthesia Track

*Anesthesia Track* is a streamlined web application designed to help healthcare professionals manage and track anesthesia-related patient records. It simplifies the recording, retrieval, and management of vital patient data, procedure details, and notes in a modern and user-friendly interface.

---

 Features

 *Login Authentication Page*  
  Secure user login interface with smooth UI using Tailwind CSS.

 *Patient Registration Form*  
  Collects essential details such as demographics, procedure type, vitals, and allergies.

-  *Patient Records Viewer*  
  View stored patient data in a clean card layout with vital signs and notes.

-  *Notes Interface*  
  Add/view post-op and anesthesia-related notes per patient (integration ready).

-  *Success Page*  
  Confirmation screen upon successful data submission with intuitive UI.

---

 🛠 Tech Stack

| Technology      | Purpose                                 |
|------------------|-------------------------------------------|
| HTML5 + CSS3     | Base structure and styling               |
| Tailwind CSS     | Utility-first modern styling framework   |
| Flask (backend)* | To handle routing and database (assumed) |
| Python*          | Backend server language (if used)        |

> 🔹 *Flask & Python are assumed for server logic due to Jinja templating ({{ url_for(...) }}) usage.

---
 Folder Structure

anesthesia-track/
├── app.py                        # Main Flask application file
├── database.db                   # SQLite database file

├── static/                       # Folder for static files (CSS, images, JS)
│   └── style.css                 # Custom stylesheet

├── templates/                    # HTML templates rendered by Flask
│   ├── login.html                # Login page
│   ├── patient_form.html         # Patient registration form
│   ├── view_patients.html        # View submitted patient records
│   ├── doctor_notes.html         # Section to add/view doctor notes
│   └── result.html               # Success/result confirmation page How to Use (Assuming Flask)

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/anesthesia-track.git
   cd anesthesia-track

2. Install dependencies:

pip install flask


3. Run the Flask server:

python app.py


4. Open the app in your browser:

http://127.0.0.1:5000/




---
 Advantages

Clean, responsive UI (mobile-friendly)

Easy integration into any hospital/clinic system

Modular HTML pages for extensibility

Tailored for anesthesiology procedures and post-op tracking



---

 Future Enhancements

Database integration (e.g., SQLite/PostgreSQL)

Role-based user management

Export patient reports to PDF

Graphs for vitals over time

Dark mode toggle



---

 License

This project is open-source and available under the MIT License.

