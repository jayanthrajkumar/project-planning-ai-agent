"""
Pydantic models for project planning output.
"""

from typing import List
from pydantic import BaseModel, Field


class TaskEstimate(BaseModel):
    """
    Represents a project task and its estimation.
    """

    task_name: str = Field(
        ...,
        description="Name of the task"
    )

    estimated_time_hours: float = Field(
        ...,
        description="Estimated completion time in hours"
    )

    required_resources: List[str] = Field(
        ...,
        description="Resources required for the task"
    )


class Milestone(BaseModel):
    """
    Represents a project milestone.
    """

    milestone_name: str = Field(
        ...,
        description="Milestone name"
    )

    tasks: List[str] = Field(
        ...,
        description="Associated tasks"
    )


class ProjectPlan(BaseModel):
    """
    Final structured project plan.
    """

    tasks: List[TaskEstimate]
    milestones: List[Milestone]