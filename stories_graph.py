from IPython.display import Image
from rasa_core.agent import Agent

agent = Agent('rail_domain.yml')
agent.visualize("./data/stories.md", output_file = "story_graph.png", max_history=2)

Image(filename="story_graph.png")