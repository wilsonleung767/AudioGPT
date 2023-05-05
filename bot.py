from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("API_KEY")

# Split the script into parts according to chunk_size
def split_text_to_list(filename, chunk_size):
    with open(filename, "r") as file:
        text = file.read()

    splitted_text_list = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return splitted_text_list
    
texts = split_text_to_list('script/rid_acne_talk/rid_acne_talk.txt', 3000)

print(texts)
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

response = llm_chain.predict(human_input= "Summarize the podcast script in point form, keep all the detail, state the speaker of the content if possible")

# while True:
#     user_input = input("Enter your message ('end' to terminate): ")
#     if user_input == "end":
#         break
    
#     response = llm_chain.predict(human_input=user_input)
#     print(response)

print(response)

