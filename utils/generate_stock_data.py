import os
import random
import requests
from faker import Faker
from dotenv import load_dotenv
from datetime import datetime, timedelta
import uuid

# Load environment variables
load_dotenv()

# Get the Supabase URL and API Key from the environment
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_API_KEY = os.getenv('SUPABASE_API_KEY')

# Set the API URL for Supabase tables
USERS_TABLE = f"{SUPABASE_URL}/rest/v1/api_users"
STOCKS_TABLE = f"{SUPABASE_URL}/rest/v1/api_stocks"
STOCK_PRICE_HISTORY_TABLE = f"{SUPABASE_URL}/rest/v1/api_stockpricehistory"
PORTFOLIOS_TABLE = f"{SUPABASE_URL}/rest/v1/api_portfolios"
PORTFOLIO_ITEMS_TABLE = f"{SUPABASE_URL}/rest/v1/api_portfolioitems"
TRANSACTIONS_TABLE = f"{SUPABASE_URL}/rest/v1/api_transactions"
EARNINGS_TABLE = f"{SUPABASE_URL}/rest/v1/api_earnings"

HEADERS = {
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "apikey": SUPABASE_API_KEY,
    "Content-Type": "application/json",
}

fake = Faker()

# Predefined stocks with their corresponding 3-character ticker symbols
STOCKS = {
    "Rua_Bien": "RBB",
    "Ho": "HOO",
    "Te_Giac": "TGG",
    "Voi": "VOI"
}

# Function to generate fake user data
def generate_fake_user():
    return {
        "user_id": str(uuid.uuid4()),
        "username": fake.user_name(),
        "house": random.choice(["Rua_Bien", "Ho", "Te_Giac", "Voi"]),
    }

# Function to generate fake stock data
def generate_fake_stock(ticker):
    tick_to_name = {
        "RBB": "Rua_Bien",
        "HOO": "Ho",
        "TGG": "Te_Giac",
        "VOI": "Voi"
    }

    return {
        "stock_ticker": ticker,
        "stock_name": f"{tick_to_name[ticker]}",
        "full_name": f"{tick_to_name[ticker]} House",
        "current_price": round(random.uniform(10, 200), 2),
        "volume": random.randint(100, 1000)
    }

# Function to generate fake stock price history data
def generate_fake_stock_price_history(stock_ticker):
    timestamp = datetime.now() - timedelta(days=random.randint(1, 90))

    return {
        "price_history_id": str(uuid.uuid4()),
        "stock_ticker_id": stock_ticker,
        "price": round(random.uniform(10, 200), 2),
        "timestamp": timestamp.isoformat()
    }

# Function to generate fake portfolio data
def generate_fake_portfolio(user_id):
    return {
        "portfolio_id": str(uuid.uuid4()),
        "user_id": user_id,
        "points_balance": random.randint(100, 1000)
    }

# Function to generate fake portfolio items data
def generate_fake_portfolio_item(portfolio_id, stock_ticker):
    return {
        "portfolio_item_id": str(uuid.uuid4()),
        "portfolio_id": portfolio_id,
        "stock_ticker_id": stock_ticker,
        "quantity": random.randint(1, 100)
    }

# Function to generate fake transactions data
def generate_fake_transaction(user_id, stock_ticker):
    transaction_type = random.choice(["buy", "sell"])
    timestamp = datetime.now() - timedelta(days=random.randint(1, 90))

    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": user_id,
        "stock_ticker_id": stock_ticker,
        "quantity": random.randint(1, 10),
        "transaction_type": transaction_type,
        "timestamp": timestamp.isoformat()
    }

# Function to generate fake earnings data
def generate_fake_earnings(user_id):
    timestamp = datetime.now() - timedelta(days=random.randint(1, 90))

    return {
        "earning_id": str(uuid.uuid4()),
        "user_id": user_id,
        "points": random.randint(10, 100),
        "code": fake.lexify(text='?????'),
        "timestamp": timestamp.isoformat()
    }

# Function to push data to Supabase
def push_to_supabase(table, data):
    response = requests.post(table, json=data, headers=HEADERS)
    if response.status_code == 201:
        print(f"Successfully inserted into {table}")
    else:
        print(f"Error inserting into {table}: {response.status_code}, {response.text}")

# Insert predefined stocks into the Stocks table
for stock_name, ticker in STOCKS.items():
    stock_data = generate_fake_stock(ticker)
    push_to_supabase(STOCKS_TABLE, stock_data)

# Insert fake users into the Users table
all_users = []  # List to store all users' data

for _ in range(10):  # Create 10 fake users
    user_data = generate_fake_user()
    push_to_supabase(USERS_TABLE, user_data)
    all_users.append(user_data)  # Store user data for later use

user_portfolios = []  # List to store portfolios

for user_data in all_users:
    # Generate a blank portfolio (no items yet)
    portfolio_data = generate_fake_portfolio(user_data["user_id"])
    
    # Insert portfolio into the Portfolios table
    push_to_supabase(PORTFOLIOS_TABLE, portfolio_data)
    user_portfolios.append(portfolio_data)  # Store portfolio data for later use

user_portfolio_items = []  # List to store portfolio items

for portfolio_data in user_portfolios:
    # For each portfolio, add portfolio items (stocks)
    for ticker in STOCKS.values():
        # Generate portfolio item data for a specific stock
        portfolio_item_data = generate_fake_portfolio_item(portfolio_data["portfolio_id"], ticker)
        
        # Insert portfolio item into the PortfolioItems table
        push_to_supabase(PORTFOLIO_ITEMS_TABLE, portfolio_item_data)
        user_portfolio_items.append(portfolio_item_data)

# Insert random transactions for each user
user_transactions = []  # List to store transactions

for user_data in all_users:
    for _ in range(random.randint(1, 5)):  # Each user has 1 to 5 transactions
        transaction_data = generate_fake_transaction(user_data["user_id"], random.choice(list(STOCKS.values())))
        push_to_supabase(TRANSACTIONS_TABLE, transaction_data)
        user_transactions.append(transaction_data)  # Store transaction data for later use

# Insert fake earnings for each user
user_earnings = []  # List to store earnings data

for user_data in all_users:
    earnings_data = generate_fake_earnings(user_data["user_id"])
    push_to_supabase(EARNINGS_TABLE, earnings_data)
    user_earnings.append(earnings_data)  # Store earnings data for later use

# Insert fake stock price history for each stock
stock_price_history_data = []  # List to store price history data

for ticker in STOCKS.values():
    for _ in range(10):  # 10 random price history entries for each stock
        price_history_data = generate_fake_stock_price_history(ticker)
        push_to_supabase(STOCK_PRICE_HISTORY_TABLE, price_history_data)
        stock_price_history_data.append(price_history_data)  # Store price history data

