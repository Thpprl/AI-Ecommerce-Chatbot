from app.core.ai_model import AIModel

class ChatService:
    def __init__(self):
        self.model = AIModel()

    def ask_ai(self, message: str) -> str:
        return self.model.generate_response(message)
