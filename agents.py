"""
Agent definitions.
"""

from crewai import Agent


def create_agents(agents_config):
    """
    Create all agents from configuration.
    """

    project_planning_agent = Agent(
        config=agents_config["project_planning_agent"]
    )

    estimation_agent = Agent(
        config=agents_config["estimation_agent"]
    )

    resource_allocation_agent = Agent(
        config=agents_config["resource_allocation_agent"]
    )

    return (
        project_planning_agent,
        estimation_agent,
        resource_allocation_agent
    )
