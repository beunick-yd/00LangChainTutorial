from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
# hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm=HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model=ChatHuggingFace(
    llm=llm
)
result=model.invoke("How to survive Bengaluru traffic!")

print(result)