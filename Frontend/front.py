import streamlit as st
import requests

st.title("Text")

text_input = st.text_area("Введите текст")

uploaded_file = st.file_uploader("Прикрепите файл", type=["txt", "pdf", "docx"])

if st.button("Отправить"):
    if text_input:
        endpoint_url = "http://your-backend-endpoint.com/generate"
        response = requests.post(endpoint_url, json={"text": text_input})
        if response.status_code == 200:
            st.write("Ответ на введенный текст:")
            st.write(response.json().get("response_text", "Ошибка в ответе от сервера."))
        else:
            st.error("Произошла ошибка при обращении к серверу. Попробуйте позже.")
    else:
        st.warning("Пожалуйста, введите текст перед отправкой.")

    if uploaded_file is not None:
        st.write("Загруженный файл:")
        st.write(uploaded_file.name)
    else:
        st.warning("Пожалуйста, загрузите файл перед отправкой.")

st.text_input("Input Text", "Введите ваш текст здесь")