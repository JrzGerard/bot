from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21591888"))
    API_HASH = getenv("API_HASH", "d3a40a4f3cd858f80a6ef1659cc4df48")
    BOT_TOKEN = getenv("BOT_TOKEN", "6519242550:AAEt_3j_Jw7Y4eDLqaIJ2q2nv8GVLMlUpVI")

config = Config()
