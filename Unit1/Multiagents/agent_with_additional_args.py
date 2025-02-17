from smolagents import CodeAgent, HfApiModel
# Needs pro subscription, haven't tested yet
model_id = "meta-llama/Llama-3.3-70B-Instruct"
agent = CodeAgent(tools=[], model=HfApiModel(model_id=model_id), add_base_tools=True)
agent.run(
    "Why does Mike not know many people in New York?",
    additional_args={"mp3_sound_file_url": 'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/recording.mp3'}
)
