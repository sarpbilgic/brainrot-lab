from xai_sdk import Client
from app.core.config import settings

class GrokClient:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.client = Client(api_key=settings.GROK_API_KEY)
        return cls.instance

def get_grok_client() -> GrokClient:
    return GrokClient()

grok_client = get_grok_client()
