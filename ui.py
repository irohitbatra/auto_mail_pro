import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from mailer import AutoMailer

class AutoMailUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Auto Mail Pro")
        self.root.geometry("500x450")
        self.contacts = None

        # UI Inputs
        tk.Label(root, text="SMTP Server").pack()
        self.smtp_entry = tk.Entry(root)
        self.smtp_entry.insert(0, "smtp.gmail.com")
        self.smtp_entry.pack()

        tk.Label(root, text="SMTP Port").pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.insert(0, "587")
        self.port_entry.pack()

        tk.Label(root, text="Your Email").pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        tk.Label(root, text="Password / App Password").pack()
        self.pass_entry = tk.Entry(root, show="*")
        self.pass_entry.pack()

        tk.Button(root, text="Load Contacts CSV", command=self.load_contacts).pack()

        tk.Label(root, text="Subject").pack()
        self.subject_entry = tk.Entry(root)
        self.subject_entry.pack()

        tk.Label(root, text="Email Body").pack()
        self.body_entry = tk.Text(root, height=10)
        self.body_entry.pack()

        tk.Button(root, text="Send Emails", command=self.send_emails).pack()

    def load_contacts(self):
        file_path = filedialog.askopenfilename()
        self.contacts = pd.read_csv(file_path)
        messagebox.showinfo("Loaded", f"Contacts Loaded: {len(self.contacts)}")

    def send_emails(self):
        if self.contacts is None:
            messagebox.showerror("Error", "Load contacts first!")
            return

        mailer = AutoMailer(
            self.smtp_entry.get(),
            int(self.port_entry.get()),
            self.email_entry.get(),
            self.pass_entry.get()
        )

        subject = self.subject_entry.get()
        body = self.body_entry.get("1.0", tk.END)

        success = 0
        failed = 0

        for _, row in self.contacts.iterrows():
            personalised_body = body.replace("{name}", row["name"])
            status = mailer.send_mail(row["email"], subject, personalised_body)

            if status:
                success += 1
            else:
                failed += 1

        messagebox.showinfo("Done", f"Emails Sent!\n✅ Success: {success}\n❌ Failed: {failed}")
