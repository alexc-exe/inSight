# Main Import Libraries. Pandas for data.
import os
from dotenv import load_dotenv
import pandas as pd
import finnhub

load_dotenv()

api_key = os.getenv("FINNUHUB_API_KEY")

finnhub_client = finnhub.Client(api_key=api_key)

print(finnhub_client.quote("AAPL"))
