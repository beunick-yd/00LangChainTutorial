from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llms = ChatGoogleGenerativeAI(
    model='gemini-3.8-flash',
    temperature=0.2,
    # temperature is a parameter that controls the randomness of a language model's output. It affects how creative 
        # creative or deterministic the response are.
         # lower values (0.0 - 0.3) : more deterministic
         #higher values : random
    #google_api_key=None
    max_output_tokens=10
) 
#result=llms.invoke("What is the capital of France")
result=llms.invoke("Write a 5 line poem on cricket")
# print(result.content)
text = "".join(
    block["text"]
    for block in result.content
    if isinstance(block, dict) and block.get("type") == "text"
)

print(text)