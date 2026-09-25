from dotenv import load_dotenv
load_dotenv()

from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Model
model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7, max_tokens=2000)

# 3. Output Parser
parser = StrOutputParser()

#Runnable chain
chain = prompt | model | parser

result = chain.invoke("Machine Learning")
print(result)