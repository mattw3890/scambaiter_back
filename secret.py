# MAIL
API_KEY = ""# "YOUR_MAILGUN_API_KEY"
API_BASE_URL = ""  # "YOUR_MAILGUN_API_BASE_URL"
DOMAIN_NAME = ""  # "YOUR_SERVER_DOMAIN_NAME"
MAIL_SAVE_DIR = "./emails/queued" # crawled and received emails
MAIL_ARCHIVE_DIR = "./emails/archive" #archive
MAIL_HANDLED_DIR = "./emails/handled" # emails replied to
ADDR_SOL_PATH = "./emails/record.json" # stores email addresses and names and strategies used
# MODEL PATHS
MODEL_HISTORY_PATH = "./models/history.json" #list of responders and times used
CLASSIFIER_PATH = "./models/classifier/final-model.pt"
OPENAI_API_KEY = ""
FILENAME1 = "./data/eliza_dane_green_days.json"
FILENAME2 = "./data/tushie-blessing.json"
FILENAME3 = "./data/noogie_california_dreamin.json"
FAKEDATADIR = "./data/fakeData"
TEMPLATES_DIR = "./responder/templates"
# CRAWLER CONF
CRAWLER_PROG_DIR = "./cache" # has crawled cache
MAX_PAGE_SL = 2
MAX_PAGE_SS = 7
