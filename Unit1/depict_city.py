from smolagents import CodeAgent, HfApiModel, load_tool,tool, GradioUI
import datetime
import pytz

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None,
)

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local date and time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"
    
@tool
def depict_city(city: str) -> str:
    """A tool that generates a description of a city at a given time with weather.
    Args:
        city: The name of the city to depict.
    """
    agent = CodeAgent(
        model=model,
        tools=[get_current_time_in_timezone], ## add your tools here (don't remove final answer)
        max_steps=6,
    )

    date = agent.run(f"What is the current date and time in {city}?")

    return agent.run(
        f"""Generate a detailed visual description of a random landmark in {city} for text-to-image tools. 
        The date is {date}. Ensure that your description reflects time and seasonal details appropriately. 
        For example, if it’s nighttime, depict a dark sky with artificial lighting; if it’s winter, illustrate snowy landscapes and winter-themed elements. 
        Incorporate environmental factors such as weather conditions, seasonal changes, and the surrounding urban or natural scenery to create a visually accurate and immersive representation."""
    )

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 


# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

agent = CodeAgent(
    model=model,
    tools=[depict_city, image_generation_tool], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None
)

# agent.run("What is the weather in Paris right now?")
GradioUI(agent).launch()
