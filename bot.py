from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
# Embeddings
from langchain.vectorstores import chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

# Own function
from audio_to_text import audio_to_text

# https://www.youtube.com/watch?v=h0DHDp1FbmQ&ab_channel=DataIndependent
import os
from dotenv import load_dotenv

def AudioGPT(audio_file):
    # Load environment variables from .env file
    load_dotenv()
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

    file = os.path.basename(audio_file)
    file_name = os.path.splitext(file)[0]
    
    if os.path.isfile(f"script/{file_name}.txt"):
        with open(f"script/{file_name}.txt", "r") as file:
            text = file.read()
    else:    
        text = audio_to_text(audio_file)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=0)
    # texts splitted into specified chunks
    texts = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("API_KEY"))
    pinecone.init(
        api_key= os.getenv("PINECONE_API_KEY ") ,
        environment= os.getenv("PINECONE_ENVIRONMENT")
    )
    index_name = "chatbot"
    docsearch = Pinecone.from_texts(texts, embeddings, index_name= index_name)

    # Chatgpt part
    llm = ChatOpenAI(temperature=0.6, model_name='gpt-3.5-turbo')
    chain = load_qa_chain(llm, chain_type='stuff')
    query = "This this a script of a audio. Now, please summarize the script in point form, include all the details like the statistics ,time and source that are mentioned in the talk."
    docs = docsearch.similarity_search( query= query , include_metadata = True)
    # print(docs)
    summary = chain.run(input_documents = docs, question= query)
    print(summary)


    while True:
        user_input = input("Enter your question (Type 'end' to terminate): ")
        if user_input == "end":
            break
        docs = docsearch.similarity_search(query= user_input, include_metadata = True)
        response = chain.run(input_documents = docs , question = user_input)
        print(f"AudioGPT: {response}")
        print("\n")


AudioGPT("audio/192.mp3")

# Split the script into parts according to chunk_size
# def split_text_to_list(filename, chunk_size):
#     with open(filename, "r") as file:
#         text = file.read()

#     splitted_text_list = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
#     return splitted_text_list
    
# texts = split_text_to_list('script/rid_acne_talk/rid_acne_talk.txt', 3000)

# template = """You are a helpful assistant that can help me summerize the content of a podcast script. Do not response to me until I ask you to give a summary!
# {chat_history}
# Human: {human_input}
# Chatbot:"""

# prompt = PromptTemplate(
#     input_variables=["chat_history", "human_input"], 
#     template= template
# )
# memory = ConversationBufferMemory(memory_key="chat_history")

# llm_chain = LLMChain(
#     llm= llm, 
#     prompt=prompt, 
#     verbose=True, 
#     memory=memory,
# )


# for text_segment in texts:
#     llm_chain.predict(human_input= f"This is the podcast script : {text_segment}")

# response = llm_chain.predict(human_input= "Summarize the podcast script in point form, keep all the detail, state the speaker of the content if possible")


# print(response)

