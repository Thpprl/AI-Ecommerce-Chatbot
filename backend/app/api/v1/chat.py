from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
service = ChatService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = service.ask_ai(request.message)
    return ChatResponse(reply=reply)
