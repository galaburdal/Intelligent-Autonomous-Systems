
from crewai import Agent, LLM


def create_delegator() -> Agent:
    llm = LLM(
        model="ollama/llama3:latest",
        base_url="http://localhost:11434",
        temperature=0.2,
    )

    return Agent(
        role="Task Delegator",
        goal="Розбивати складне завдання на чіткі підзавдання",
        backstory=(
            "Ти координуєш розподіл роботи. Ти визначаєш мету, "
            "необхідні кроки, очікувані результати та критерії якості."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=True,
        max_iter=3,
    )
