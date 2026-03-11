# from supabase import create_client, Client
# from app.config.settings import settings

# supabase: Client = create_client(
#     settings.supabase_url,
#     settings.supabase_key
# )

import os
from supabase import create_client

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print("---- DEBUG ----")
print("SUPABASE_URL:", url)
print("SUPABASE_KEY exists:", key is not None)
print("SUPABASE_KEY length:", len(key) if key else None)
print("----------------")

supabase = create_client(url, key)