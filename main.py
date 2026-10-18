
import time

from crewai import Crew, Process, Task

from agents.coordinator import create_coordinator
from agents.delegator import create_delegator
from agents.worker import create_worker


def main():
    start_time = time.perf_counter()

    delegator = create_delegator()
    worker = create_worker()
    coordinator = create_coordinator()

    planning_task = Task(
        description=(
            "Підготуй план маркетингової кампанії для нового застосунку "
            "для вивчення англійської мови. Визнач цільову аудиторію, "
            "три основні канали просування та критерії успіху. "
            "Відповідай українською."
        ),
        expected_output=(
            "Структурований план із цільовою аудиторією, трьома каналами "
            "просування та вимірюваними критеріями успіху."
        ),
        agent=delegator,
    )

    content_task = Task(
        description=(
            "На основі плану попереднього завдання підготуй конкретні "
            "маркетингові матеріали: два короткі рекламні тексти та "
            "три ідеї публікацій для соціальних мереж. "
            "Не вигадуй статистичних даних. Відповідай українською."
        ),
        expected_output=(
            "Два рекламні тексти та три ідеї публікацій, "
            "узгоджені з маркетинговим планом."
        ),
        agent=worker,
        context=[planning_task],
    )

    review_task = Task(
        description=(
            "Перевір маркетинговий план і матеріали попередніх завдань. "
            "Оціни відповідність цілі, конкретність, узгодженість і "
            "відсутність непідтверджених фактів. Виправ недоліки та "
            "сформуй фінальний результат українською."
        ),
        expected_output=(
            "Перевірена фінальна маркетингова кампанія з планом, "
            "рекламними текстами, ідеями публікацій і короткою оцінкою якості."
        ),
        agent=coordinator,
        context=[planning_task, content_task],
    )

    crew = Crew(
        agents=[delegator, worker, coordinator],
        tasks=[planning_task, content_task, review_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    elapsed = time.perf_counter() - start_time

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print(result)
    print(f"\nExecution time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
