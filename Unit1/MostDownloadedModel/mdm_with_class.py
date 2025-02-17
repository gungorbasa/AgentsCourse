from huggingface_hub import list_models
from smolagents import Tool, CodeAgent, HfApiModel

class ModelDownloadTool(Tool):
    name = "model_download_tool"
    description = "This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub. It returns the name of the checkpoint."
    inputs = {"task": {"type": "string", "description": "The task for which to get the download count."}}
    output_type = "string"
    
    def forward(self, task: str) -> str:
        most_downloaded_model = next(iter(list_models(task=task, sort="downloads", direction=-1)))
        return most_downloaded_model.id

agent = CodeAgent(tools=[ModelDownloadTool()], model=HfApiModel())
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub?"
)
