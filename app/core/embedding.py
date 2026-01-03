from sentence_transformers import SentenceTransformer
from app.core.config import EMBED_MODEL

embedder = SentenceTransformer(EMBED_MODEL)
