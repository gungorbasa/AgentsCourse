from smolagents import (
    load_tool,
    CodeAgent,
    HfApiModel,
    GradioUI,
    DuckDuckGoSearchTool
)

model = HfApiModel()

web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
      model=model,
      name="web_agent",
      description="Runs a web search for you. Give it your query as an argument",
)

image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

# Initialize the agent with the image generation tool
agent = CodeAgent(tools=[], model=model, managed_agents=[web_agent, image_generation_tool])

GradioUI(agent).launch()
