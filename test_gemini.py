
from dotenv import load_dotenv
from crewai import LLM
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not api_key:
    raise ValueError("GEMINI_API_KEY не знайдено у .env")

llm = LLM(
    model=f"gemini/{model}",
    api_key=api_key,
    temperature=0.1,
)

response = llm.call(
    [{"role": "user", "content": "Відповідай українською: напиши одне речення про роль координатора в багатoагентній системі."}]
)

print("Gemini працює!")
print(response)
