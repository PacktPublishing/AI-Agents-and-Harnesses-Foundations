from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# The single place a model is named. Change this line to switch models or providers.
model = init_chat_model("openai:gpt-5.6-sol")
