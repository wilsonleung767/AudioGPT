from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain import LLMChain, PromptTemplate


import os
os.environ['OPENAI_API_KEY'] = "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"

def split_text_to_list(filename, chunk_size):
    with open(filename, "r") as file:
        text = file.readline()

    splitted_text_list = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return splitted_text_list
    
texts = split_text_to_list("script/cutVer.txt", 2500)


llm = OpenAI(model_name="gpt-3.5-turbo", temperature= 0.6 )

template = """You are a helpful assistant that can help me summerize the content of a podcast script. Do not response to me until I ask you to give a summary!
{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], 
    template= template
)
memory = ConversationBufferMemory(memory_key="chat_history")


llm_chain = LLMChain(
    llm= llm, 
    prompt=prompt, 
    verbose=True, 
    memory=memory,
)


for text_segment in texts:
    llm_chain.predict(human_input= f"This is the podcast script : {text_segment}")

response = llm_chain.predict(human_input= "There is a hidden key word in the script, tell me what is that word")

print(response)

# embeddings = OpenAIEmbeddings()
# doserach  = FAISS.from_texts(texts[], embeddings)


# chain = load_qa_chain(OpenAI(), chain_type= "stuff")

# query= "who are involved in the script?"
# chain.run(input_documents = texts[0] , question=query)