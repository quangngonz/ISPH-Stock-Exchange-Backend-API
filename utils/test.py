import dotenv, os, requests


dotenv.load_dotenv()
# Get the Supabase URL and API Key from the environment
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_API_KEY = os.getenv('SUPABASE_API_KEY')

HEADERS = {
    "Authorization": "Bearer " + SUPABASE_API_KEY,
    "apikey": SUPABASE_API_KEY,
    "Content-Type": "application/json",
}


print(SUPABASE_URL)
print(SUPABASE_API_KEY)

test_url = f"{SUPABASE_URL}/rest/v1/users"
response = requests.get(test_url, headers=HEADERS)

print(response.status_code, response.text)