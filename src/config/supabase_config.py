import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Supabase URL and Key from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create a Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
# Check if the client is created successfully
if supabase:
    print("Supabase client created successfully.")