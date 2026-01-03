from chromadb import PersistentClient
from app.core.config import VECTOR_DB_DIR, COLLECTION_NAME

client = PersistentClient(
    path=VECTOR_DB_DIR
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)
print(client.list_collections())
