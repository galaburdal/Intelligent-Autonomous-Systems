
from crewai import Agent, LLM


def create_worker() -> Agent:
    """Create a worker powered by the local Ollama model."""

    llm = LLM(
        model="ollama/llama3:latest",
        base_url="http://localhost:11434",
        temperature=0.2,
    )

    return Agent(
        role="Research and Content Worker",
        goal="Виконувати доручене завдання на основі доступної інформації",
        backstory=(
            "Ти спеціаліст із дослідження інформації та підготовки "
            "структурованого, точного й зрозумілого контенту."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=True,
        max_iter=3,
    )
