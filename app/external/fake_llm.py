from app.external.llm_service import LLMService

class FakeLLMService(LLMService):

    def generate_report(self, score: int, message: str) -> str:
        return f"""
        健康评分为 {score} 分。
        状态评估：{message}。
        建议保持良好作息，适当增加运动。
        """