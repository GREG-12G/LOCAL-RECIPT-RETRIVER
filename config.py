from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "local_restaurant.db"
ASSETS_DIR = BASE_DIR / "assets" / "food_images"
BACKUP_DIR = BASE_DIR / "backups"
REPORTS_DIR = BASE_DIR / "reports"

# Money: store as INTEGER cents (KES * 100) to avoid float errors
# Example: 250.50 KES = 25050

RESTAURANT_NAME = "Your Restaurant Name"
RECEIPT_FOOTER = "Thank you, welcome again!"
TILL_NUMBER = "Buy Goods: 123456"
