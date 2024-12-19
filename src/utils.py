import requests, pandas as pd
from .soup import Soup
from .models import School
import datetime

def get_html(url : str):
    r = requests.get(url)
    print(r.status_code)
    return Soup(r.text)

def save_to_xlsx(schools : list[School], filename : str):
    date = datetime.datetime.now().strftime("%d_%B_%Y")
    df = pd.DataFrame(schools)
    df.to_excel(f"{date}-{filename}")