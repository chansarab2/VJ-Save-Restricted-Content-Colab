import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28908355"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d7f53de270d2ef1ad9754fc22f2ced5a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chanpreet151515:<db_password>@cluster0.uzvrequ.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
