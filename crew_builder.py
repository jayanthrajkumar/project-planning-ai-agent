"""
Crew builder module.
"""

from crewai import Crew


def build_crew(
    agents,
    tasks
):
    """
    Build CrewAI crew.
    """

    return Crew(
        agents=list(agents),
        tasks=list(tasks),
        verbose=True
    )
