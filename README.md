✅ Auto Mail Pro — Automated Bulk Email Sender (Python + Tkinter)

Auto Mail Pro is a lightweight, GUI-based email automation tool built with Python.
It allows you to:

✅ Send bulk personalized emails
✅ Load contacts from CSV
✅ Use Gmail SMTP with App Password
✅ Write custom subjects & email body
✅ Send test emails before bulk sending
✅ Track sending status in real-time

Designed for students, freelancers, and businesses who want a simple, secure, and fast solution for sending automated emails.

🚀 Features
✅ 1. User-Friendly GUI

Built using Tkinter, with clean input fields for SMTP settings, email content, and CSV loading.

✅ 2. Bulk Email Sending

Load a CSV file containing recipient names & email IDs, then send personalized messages to each contact.

CSV format:

name,email
Rohit Batra,rohit.demo@gmail.com
Aman Sharma,aman.test@yahoo.com
...

✅ 3. Gmail SMTP + App Password Support

The app supports Gmail’s secure App Password authentication, making email sending safe and reliable.

✅ 4. Test Email Button

Verify your SMTP settings before sending bulk mail, preventing errors.

✅ 5. Real-time Logs

See the status of each email — sent, failed, skipped.

📦 Installation
✅ Clone the repository
git clone https://github.com/irohitbatra/auto_mail_pro
cd auto_mail_pro

✅ Install dependencies
pip install -r requirements.txt

🔧 How to Use (Step-by-Step)
✅ 1. Generate a Gmail App Password

Go to Google Account

Security → Turn ON 2-Step Verification

Search App Passwords

Create new:

App: Mail

Device: Windows

Google gives a 16-digit App Password
Example:

abcd efgh ijkl mnop


(Remove spaces before inserting)

✅ 2. Launch the App
python app.py

✅ 3. Fill these fields in the GUI:

SMTP Server: smtp.gmail.com

SMTP Port: 587

Your Email: your Gmail

Password / App Password: 16-digit Google App Password

Subject: Any subject

Email Body: Your message (supports {name} placeholder)

Load Contacts CSV: Select your CSV file

✅ 4. Send a Test Email

Click "Test Email" to verify everything is working.

✅ 5. Send Bulk Emails

Click "Send Emails" — the app will deliver emails to all contacts, one by one.

🧪 CSV File Format

Your CSV should look like this:

name,email
Rohit Batra,rohit.batra.demo@gmail.com
Simran Kaur,simran.demo@outlook.com
Aman Verma,aman.verma.test@yahoo.com

📁 Project Structure

auto_mail_pro/
│
├── app.py                # Main GUI application
├── mailer.py             # Email sending logic
├── requirements.txt      # Dependencies
├── sample_contacts.csv   # Example contacts file
└── README.md             # Project documentation

✅ Tech Stack

Python

Tkinter (GUI)

smtplib (SMTP Email)

Pandas (CSV handling)

Threading (smooth UI + async sending)

🛡️ Security Notes

Never share your Gmail App Password

Never push .env or real credentials

Use App Password — NOT your real Gmail password

Gmail may block sending if spam detected

📜 License

This project is licensed under the MIT License, making it free to modify and distribute.

👨‍💻 Author

Rohit Batra
💼 Full Stack Developer | Cybersecurity | Python
🌐 GitHub: https://github.com/irohitbatra

Made with ❤️ by Rohit Batra
