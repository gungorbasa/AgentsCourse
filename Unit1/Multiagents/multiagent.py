from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool

model = HfApiModel()
web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
      model=model,
      name="web_agent",
      description="Runs a web search for you. Give it your query as an argument",
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[web_agent]
)

manager_agent.run("Who is the CEO of Google?")
