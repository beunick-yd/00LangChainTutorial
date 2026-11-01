# from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id='google/gemma-2-2b-it',
#     task='text-generation',
#     max_new_tokens=256,
#  )
# model=ChatHuggingFace(
#     llm=llm
# )
model=ChatGoogleGenerativeAI(model='gemini-3.8-flash')
# chat_history=[]
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]
while True:
    user_input=input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.text))
    print('AI : ',result.text)

print(chat_history)

#types of msg - System, Human , AI