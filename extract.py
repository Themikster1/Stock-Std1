from config import key 
import requests 
import datetime
import csv


stocks = ['AAPL', 'GS', 'INTC', 'IBM', 'JPM'] 
for s in stocks: 
    url = f"https://api.polygon.io/v2/aggs/ticker/{s}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    r = requests.get(url)
    data = r.json()
    results = data["results"]

    formatted = []
    for day in results: 
    
        c = day["c"]
        t = day["t"] / 1000.0 
        t = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
        daydic = {}
        daydic["date"]  = t 
        daydic["closing price"]  = c 
        formatted.append(daydic) 

    with open(f"{s}.csv", "w", newline='') as outfile:
        writer = csv.DictWriter(outfile,fieldnames=['date' , 'closing price'])
        writer.writeheader() 
        writer.writerows(formatted) 