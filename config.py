import os

API_ID = API_ID = 4410228

API_HASH = os.environ.get("API_HASH", "e73c6f2e8842acdeb8bf8c18628bb772")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6458939607:AAFoGSkcqvfS7W4F1_o0jjbAH-Vx_qWkBSI")

PASS_DB = int(os.environ.get("PASS_DB", "7210"))

OWNER = int(os.environ.get("OWNER", 1700825627))

LOG = -1001841872891

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1700825627").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


