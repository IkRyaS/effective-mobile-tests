import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    URL_SAUCEDEMO_LOGIN = os.getenv('SAUCEDEMO_LOGIN', "https://www.saucedemo.com/")
    URL_SAUCEDEMO_INVENTORY = os.getenv('SAUCEDEMO_INVENTORY', "https://www.saucedemo.com/inventory.html")
    URL_SAUCEDEMO_CHECKOUT_COMPLETE = os.getenv('SAUCEDEMO_CHECKOUT_COMPLETE', "https://www.saucedemo.com/checkout-complete.html")
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
