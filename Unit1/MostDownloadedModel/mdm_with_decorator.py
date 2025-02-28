from huggingface_hub import list_models
from smolagents import tool, CodeAgent, HfApiModel

@tool
def most_download_model_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    most_downloaded_model = next(iter(list_models(task=task, sort="downloads", direction=-1)))
    return most_downloaded_model.id


agent = CodeAgent(tools=[most_download_model_tool], model=HfApiModel())
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub?"
)
