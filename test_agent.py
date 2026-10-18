
from crewai import Agent, Task, Crew, Process

agent = Agent(
    role="Помічник",
    goal="Коротко відповідати на запитання",
    backstory="Ти тестовий AI-агент для лабораторної роботи.",
    llm="ollama/llama3:latest",
    verbose=True,
)

task = Task(
    description="Поясни українською трьома реченнями, що таке багатагентна система.",
    expected_output="Коротке пояснення українською мовою.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print("\nРЕЗУЛЬТАТ:")
print(result)
