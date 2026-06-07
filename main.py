"""
Main execution file.
"""

import os
import warnings

from dotenv import load_dotenv

from utils.config_loader import load_yaml
from crew.agents import create_agents
from crew.tasks import create_tasks
from crew.crew_builder import build_crew

warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

# Model selection
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

# Load configurations
agents_config = load_yaml("config/agents.yaml")
tasks_config = load_yaml("config/tasks.yaml")

# Create agents
agents = create_agents(agents_config)

# Create tasks
tasks = create_tasks(
    tasks_config,
    *agents
)

# Build crew
crew = build_crew(
    agents,
    tasks
)

# Inputs
inputs = {
    "project_type": "Website",
    "project_objectives": "Create a website for a small business",
    "industry": "Technology",
    "team_members": """
John Doe (Project Manager)
Jane Doe (Software Engineer)
Bob Smith (Designer)
Alice Johnson (QA Engineer)
Tom Brown (QA Engineer)
""",
    "project_requirements": """
Create a responsive design
Implement modern UI
Develop navigation system
Include About Us page
Create Services page
Create Contact page
Implement blog section
SEO optimization
Social media integration
Testimonials section
"""
}

# Run Crew
result = crew.kickoff(inputs=inputs)

print(result)