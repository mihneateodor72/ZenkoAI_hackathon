import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

# Define functions for new virtual agents
def handle_director_analytics(user_question):
    # Agent-specific logic for Director of Analytics
    if "evaluate customer satisfaction" in user_question.lower():
        response = "We're currently evaluating customer satisfaction by analyzing feedback forms and surveys."
    elif "analyze attendance data" in user_question.lower():
        response = "Attendance data is being tracked, and we will provide insights based on the numbers."
    else:
        response = "I'm the Director of Analytics. How can I assist you?"

    st.write(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)

def handle_volunteer_coordinator(user_question):
    # Agent-specific logic for Volunteer Coordinator
    if "assign volunteers" in user_question.lower():
        response = "I'm optimizing volunteer assignments based on festival needs."
    elif "monitor schedules" in user_question.lower():
        response = "We ensure volunteers have appropriate schedules and breaks."
    else:
        response = "I'm the Volunteer Coordinator. How can I assist you?"

    st.write(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size = 1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)
    return conversation_chain

def handle_userinput(user_question):
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    if "director_analytics" not in st.session_state:
        st.session_state.director_analytics = None

    if "volunteer_coordinator" not in st.session_state:
        st.session_state.volunteer_coordinator = None

    if st.session_state.director_analytics:
        handle_director_analytics(user_question)
    elif st.session_state.volunteer_coordinator:
        handle_volunteer_coordinator(user_question)
    elif st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    
    load_dotenv()
    st.set_page_config(page_title="BEST Brasov Chat AI", page_icon="🎉")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("BEST Brasov Helpdesk Chat AI 🎉")
    user_question = st.text_input("Ask a question about the festival!")
    
    if user_question:
        handle_userinput(user_question)

    #st.write(user_template.replace("{{MSG}}", "hello robotule"), unsafe_allow_html=True)
    #st.write(bot_template.replace("{{MSG}}", "hello omule") , unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your files here", accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner("Processing"):
            #get pdf text
                raw_text = get_pdf_text(pdf_docs)
                
            #get text chunks
                text_chunks = get_text_chunks(raw_text)

            #create vector store
                vectorstore = get_vectorstore(text_chunks)

            #create convo chain
            st.session_state.conversation = get_conversation_chain(vectorstore)
    


if __name__ == '__main__':
        main()