
import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()


def create_coordinator() -> Agent:
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY не знайдено у файлі .env"
        )

    llm = LLM(
        model=f"gemini/{model}",
        api_key=api_key,
        temperature=0.1,
    )

    return Agent(
        role="Project Coordinator",
        goal=(
            "Перевіряти результати роботи агентів, "
            "знаходити повтори та формувати якісну фінальну відповідь"
        ),
        backstory=(
            "Ти досвідчений координатор і редактор. "
            "Перевіряй логічність, повноту, конкретність і узгодженість "
            "результатів. Прибирай повтори, не вигадуй факти "
            "та чітко вказуй на недоліки."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=True,
        max_iter=3,
    )
