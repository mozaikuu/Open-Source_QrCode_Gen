import streamlit as st
import QrCodeGen
from PIL import Image
import io

st.title("QR Code Generator")

text = st.text_input("Input text or URL")

if st.button("Generate QR Code"):
    if text:
        try:
            qr_image = QrCodeGen.QrCodeGen(text)
            if qr_image is not None:
                # Convert the image to bytes
                img_byte_arr = io.BytesIO()
                qr_image.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                st.image(img_byte_arr, caption="Generated QR Code", use_column_width=True)
                st.success("QR Code generated successfully!")
                
                # Add a download button for the QR code
                st.download_button(
                    label="Download QR Code",
                    data=img_byte_arr,
                    file_name="qr_code.png",
                    mime="image/png"
                )
            else:
                st.error("Failed to generate QR code. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some text or a URL to generate a QR code.")

st.markdown("---")
st.markdown("Created By Moussa with Streamlit and QrCodeGen")

