import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "VoVanPhuc/sup-SimCSE-VietNamese-phobert-base")
    INDEX_NAME = os.getenv("INDEX_NAME", "hdhdhdhd")
    
