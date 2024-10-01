import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.title("QR Code Generator")

data = st.text_input("Enter text or URL to generate a QR code:")

if data:
    qr = qrcode.QRCode(version=2, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    st.image(buffer.getvalue(), caption="Generated QR Code", use_column_width=True)

    st.download_button("Download QR Code", buffer.getvalue(), file_name="qr_code.png", mime="image/png")
