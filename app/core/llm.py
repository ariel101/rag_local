from llama_cpp import Llama
from app.core.config import LLM_MODEL_PATH

llm = Llama(
    model_path=LLM_MODEL_PATH,
    n_ctx=2048,
    n_threads=4
)
