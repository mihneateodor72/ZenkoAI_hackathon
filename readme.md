BEST Brasov Chat AI

Welcome to the BEST Brasov Helpdesk Chat AI, a conversational chatbot designed to answer your questions about the festival.

The application is a python script using the Streamlit library to create a web-based chat application that interacts with a conversational AI model and supports document uploads in PDF format.
Streamlit is a Python library for creating web applications with minimal code
dotenv - library  used for loading environment variables from a .env file
PyPDF2 - library for working with PDF files. In this code, it's used to read and extract text from PDF documents
langchain - a custom library that provides various NLP-related functionalities like text splitting, embeddings, vector storage, chat models, memory management, and conversational chains

Steps to configure and open the application:

-git clone https://github.com/your-repo/best-brasov-chat-ai.git
-pip install streamlit pypdf2 langchain python-dotenv faiss-cpu openai huggingface_hub

After everything is insalled and set up, you need to run this command in the therminal to oppen the application and server:
- streamlit run app.py

Briefing of how-to-use the APP:
- On the sidebar, browse the files and upload .pdf files
- After hitting the button upload and processing it you can interact with the ChatBot.

BEST Brasov Chat AI Team - Rotaru Elena Alexia, Muntean Razvan, Petre Mihnea-Teodor (Zenko.AI Hackathon 2023)


