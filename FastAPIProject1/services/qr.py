# app/services/qr.py
import qrcode
import io
import json

def generate_qr_code(data: dict) -> bytes:
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(json.dumps(data))
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
