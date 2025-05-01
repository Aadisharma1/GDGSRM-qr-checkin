# app/services/email.py
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
from app.config import SAPI_KEY, EMAIL


def send_qr_email(to_email: str, event_title: str, qr_image_bytes: bytes):
    message = Mail(
        from_email=EMAIL,
        to_emails=to_email,
        subject=f"Your QR Code for {event_title}",
        html_content=f"<strong>Attached is your QR code for {event_title}. Please bring it to the event for check-in.</strong>"
    )

    encoded = base64.b64encode(qr_image_bytes).decode()
    attachment = Attachment(
        FileContent(encoded),
        FileName("qr_code.png"),
        FileType("image/png"),
        Disposition("attachment")
    )
    message.attachment = attachment

    try:
        sg = SendGridAPIClient(SAPI_KEY)
        sg.send(message)
    except Exception as e:
        print("Error sending email:", e)
