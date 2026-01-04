from fastapi import FastAPI, Request
from fastapi import HTMLResponse, JSONResponse, RedirectResponse
from supabase import create_client

# db_url = "https://abostfpuhcecmfbknafx.supabase.co"
# db_key = "sb_publishable_9YhEQjcy63_1TA1o8GSmbw_GYHZuuOu"

# db = create_client(db_url,db_key)
app = FastAPI()