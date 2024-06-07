from django.shortcuts import render
from os import getenv
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()

url: str = getenv("SUPABASE_URL")
key: str = getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Create your views here

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        observation = request.POST.get('observation')
        now = str(datetime.now(pytz.timezone('Europe/Bucharest')))
        print(name, price, observation, now)
        data, count = supabase.table('spends').insert({"name": name, "price": price, "observation": observation, "created_at": now}).execute()
    return render(request, 'index.html')