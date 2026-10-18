
import time
from crewai import Agent, Task, Crew, Process
from crewai import LLM


def main():
    llm = LLM(
        model="ollama/llama3:latest",
        base_url="http://localhost:11434",
        temperature=0.2,
    )

    agent = Agent(
        role="Marketing Specialist",
        goal="Створити короткий план маркетингової кампанії",
        backstory="Ти маркетолог, який готує чіткі та практичні плани.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
        max_iter=2,
    )

    task = Task(
        description=(
            "Створи короткий план маркетингової кампанії для нового "
            "застосунку для вивчення англійської мови. Вкажи цільову "
            "аудиторію, три канали просування, три вимірювані KPI "
            "і бюджет. Не вигадуй статистику. Відповідай українською."
        ),
        expected_output=(
            "Стислий план із цільовою аудиторією, трьома каналами, "
            "трьома KPI та бюджетом."
        ),
        agent=agent,
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=False,
    )

    start = time.perf_counter()
    result = crew.kickoff()
    elapsed = time.perf_counter() - start

    print("\n=== SINGLE-AGENT RESULT ===")
    print(result)
    print(f"\nExecution time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
