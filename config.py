import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6885232721:AAGkYm_7SW1IUdwJYTJ8eZwC4PX39rU3_uk")
      API_ID = int(os.environ.get("APP_ID", 29942004))
      API_HASH = os.environ.get("API_HASH", "ad92f01e4a90cddebbea0ad16fa23026")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Punikin")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 1680073194 )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
