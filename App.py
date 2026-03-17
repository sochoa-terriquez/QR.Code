import streamlit as st
import qrcode
from io import BytesIO

st.title("QR Code Generator")

text = st.text_input("Enter text or URL")

if st.button("Generate QR Code"):
    if text:
        qr = qrcode.make(text)
        buf = BytesIO()
        qr.save(buf)
        st.image(buf.getvalue(), caption="Generated QR Code")
    else:
        st.warning("Please enter text or a URL.")


