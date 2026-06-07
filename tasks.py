"""
Task definitions.
"""

from crewai import Task
from models.project_models import ProjectPlan


def create_tasks(
    tasks_config,
    project_planning_agent,
    estimation_agent,
    resource_allocation_agent
):
    """
    Create CrewAI tasks.
    """

    task_breakdown = Task(
        config=tasks_config["task_breakdown"],
        agent=project_planning_agent
    )

    time_resource_estimation = Task(
        config=tasks_config["time_resource_estimation"],
        agent=estimation_agent
    )

    resource_allocation = Task(
        config=tasks_config["resource_allocation"],
        agent=resource_allocation_agent,
        output_pydantic=ProjectPlan
    )

    return (
        task_breakdown,
        time_resource_estimation,
        resource_allocation
    )