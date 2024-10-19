import streamlit as st
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Backend.back as back

# Основной интерфейс
st.title("Text")

# Поле для ввода текста
text_input = st.text_area("Введите текст")

# Кнопка для загрузки файла
uploaded_file = st.file_uploader("Прикрепите файл", type=["txt", "pdf", "docx"])

# Кнопка для отправки данных
if st.button("Отправить"):
    if text_input:
        response = back.generate_response(text_input)
        st.write(response)
        print(response)
        # Отправка текста на endpoint для генерации ответа
    #     endpoint_url = "http://your-backend-endpoint.com/generate"  # Замените на фактический URL вашего endpoint
    #     response = requests.post(endpoint_url, json={"text": text_input})
    #     if response.status_code == 200:
    #         st.write("Ответ на введенный текст:")
    #         response_text = response.json().get("response_text", "Ошибка в ответе от сервера.")
    #         st.markdown(response_text)  # Отображение ответа в формате Markdown
    #     else:
    #         st.error("Произошла ошибка при обращении к серверу. Попробуйте позже.")
    # else:
    #     st.warning("Пожалуйста, введите текст перед отправкой.")

    if uploaded_file is not None:
        st.write("Загруженный файл:")
        st.write(uploaded_file.name)
    else:
        st.warning("Пожалуйста, загрузите файл перед отправкой.")

