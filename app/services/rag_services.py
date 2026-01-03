from app.core.embedding import embedder
from app.core.vectordb import collection
from app.core.llm import llm
from app.core.config import TOP_K

def ask_rag(question: str) -> str:
    query_embedding = embedder.encode(
        question,
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    contexts = results["documents"][0]
    context_text = "\n\n".join(contexts)

    prompt = f"""
Responde usando el contexto.

Contexto:
{context_text}

Pregunta:
{question}

Respuesta:
"""

    output = llm(
        prompt,
        max_tokens=300,
        temperature=0.2
    )

    return output["choices"][0]["text"].strip()
