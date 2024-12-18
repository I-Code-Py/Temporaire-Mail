import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk, Label, Entry, Text, Button, messagebox
import os
from dotenv import load_dotenv

def save_to_env():
    smtp_server = smtp_server_entry.get()
    smtp_port = smtp_port_entry.get()
    smtp_user = smtp_user_entry.get()
    smtp_password = smtp_password_entry.get()
    sender_email = sender_entry.get()
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message_body = message_text.get("1.0", "end-1c")

    if not smtp_server or not smtp_port or not smtp_user or not smtp_password:
        messagebox.showerror("Erreur", "Tous les champs SMTP doivent être remplis !")
        return

    if not sender_email or not recipient_email or not subject or not message_body:
        messagebox.showerror("Erreur", "Tous les champs e-mail doivent être remplis !")
        return

    with open(".env", "w") as env_file:
        env_file.write(f"SMTP_SERVER={smtp_server}\n")
        env_file.write(f"SMTP_PORT={smtp_port}\n")
        env_file.write(f"SMTP_USER={smtp_user}\n")
        env_file.write(f"SMTP_PASSWORD={smtp_password}\n")
        env_file.write(f"SENDER_EMAIL={sender_email}\n")
        env_file.write(f"RECIPIENT_EMAIL={recipient_email}\n")
        env_file.write(f"SUBJECT={subject}\n")
        env_file.write(f"MESSAGE_BODY={message_body}\n")

    messagebox.showinfo("Succès", "Configuration sauvegardée dans .env")

def send_email():
    try:
        # Charger les variables d'environnement
        load_dotenv()
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_user = os.getenv("SMTP_USER")
        smtp_password = os.getenv("SMTP_PASSWORD")
        sender_email = os.getenv("SENDER_EMAIL")
        recipient_email = os.getenv("RECIPIENT_EMAIL")
        subject = os.getenv("SUBJECT")
        message_body = os.getenv("MESSAGE_BODY")

        # Préparation du message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(message_body, "plain"))

        # Envoi de l'e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        messagebox.showinfo("Succès", "E-mail envoyé avec succès !")

    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de l'envoi de l'e-mail : {e}")

# Interface graphique
app = Tk()
app.title("Service de Messagerie")
app.geometry("400x600")

Label(app, text="Serveur SMTP :").pack(pady=5)
smtp_server_entry = Entry(app, width=50)
smtp_server_entry.pack(pady=5)

Label(app, text="Port SMTP :").pack(pady=5)
smtp_port_entry = Entry(app, width=50)
smtp_port_entry.pack(pady=5)

Label(app, text="Utilisateur SMTP :").pack(pady=5)
smtp_user_entry = Entry(app, width=50)
smtp_user_entry.pack(pady=5)

Label(app, text="Mot de passe SMTP :").pack(pady=5)
smtp_password_entry = Entry(app, show="*", width=50)
smtp_password_entry.pack(pady=5)

Button(app, text="Sauvegarder Config SMTP", command=save_to_env).pack(pady=10)

Label(app, text="Expéditeur :").pack(pady=5)
sender_entry = Entry(app, width=50)
sender_entry.pack(pady=5)

Label(app, text="Destinataire :").pack(pady=5)
recipient_entry = Entry(app, width=50)
recipient_entry.pack(pady=5)

Label(app, text="Sujet :").pack(pady=5)
subject_entry = Entry(app, width=50)
subject_entry.pack(pady=5)

Label(app, text="Message :").pack(pady=5)
message_text = Text(app, width=50, height=10)
message_text.pack(pady=5)

Button(app, text="Envoyer", command=send_email).pack(pady=20)

app.mainloop()
