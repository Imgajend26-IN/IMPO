from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from supabase import create_client

db_url = "https://glqnssavveotpgtnolip.supabase.co"
db_key = "sb_publishable_ZcinWT4tTbOggBWLhicMqw_3omluRw5"

db = create_client(db_url,db_key)

app = FastAPI()

@app.get("/contacts")
def get_all():
    contacts = db.table("contact").select("*").execute()
    data  = contacts.data
    return data

@app.get("/contact")
def get_single(ID):
    contact = db.table("contact").select("*").eq("id",ID).execute()
    data = contact.data
    return data

@app.post("/contact/detail")
async def post_contacts(request: Request):
    data = await request.json()
    result = db.table("contact").insert(data).execute()
    return result


@app.put("/update/{c_id}")
async def update(c_id: int, request: Request):
    data = await request.json()
    result = db.table("contact").update(data).eq("id", c_id).execute()
    return result


@app.delete("/delete/{m_id}")
async def update(m_id: int, request: Request):
    data = await request.json()
    result = db.table("contact").delete(data).eq("id", m_id).execute()
    return result