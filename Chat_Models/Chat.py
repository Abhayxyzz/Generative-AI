from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(model = "groq/compound", max_tokens = 500)

response = model.invoke("write a short poem about the beauty of nature")

print(response.content)