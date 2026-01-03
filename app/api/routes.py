from fastapi import APIRouter
from app.schemas.rag import QueryRequest, QueryResponse
from app.services.rag_services import ask_rag

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    answer = ask_rag(req.question)
    return {"answer": answer}
