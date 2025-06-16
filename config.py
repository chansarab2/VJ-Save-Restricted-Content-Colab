import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22877961"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "01b4a2f33d106880b4524073ef2242ea")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chanpreet2424tgt:FtXUmhmYOfeit3t7@cluster0.tkxto8d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
