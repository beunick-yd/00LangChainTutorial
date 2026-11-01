from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(
    model='gemini-3.8-flash'
)

messages=[
    SystemMessage(content='You are a helpful assisstant'),
    HumanMessage(content='tell me about langchain')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)