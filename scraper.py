# =========================================================
# THEATRE EVENT SCRAPER 
# Author: Olumide
# =========================================================

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re

URL = "https://www.shakespearesglobe.com/whats-on/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")


# =========================================================
# TEXT CLEANING & EXTRACTION FUNCTIONS
# =========================================================

def clean_text(text):
    return text.strip() if text else ""


def extract_capacity(venue):
    capacity_map = {
        "GLOBE THEATRE": 1570,
        "SAM WANAMAKER PLAYHOUSE": 340
    }
    return capacity_map.get(venue.upper(), "Unknown")


def extract_price(text):
    match = re.findall(r'£\d+(?:\.\d{2})?', text)

    if len(match) >= 2:
        return f"{match[0]} - {match[-1]}"
    elif len(match) == 1:
        return f"{match[0]} - £100"
    return "£0 - £100"


def extract_description(soup):
    desc = soup.find("meta", attrs={"name": "description"})
    return desc.get("content") if desc else ""


# =========================================================
# DATA
# =========================================================

events = []
LIMIT = 30
seen = set()

page_text = soup.get_text(" ", strip=True)
price = extract_price(page_text)
description = extract_description(soup)


# =========================================================
# SCRAPER ENGINE FOR THEATRE EVENTS
# =========================================================

for item in soup.find_all("a", href=True):

    if len(events) >= LIMIT:
        break

    text = clean_text(item.get_text(" ", strip=True))

    # skip junk
    if not text:
        continue

    if len(text) < 8:
        continue

    # remove navigation noise only
    blacklist = ["home", "search", "login", "basket", "menu", "cookies"]

    if any(word in text.lower() for word in blacklist):
        continue

    # remove duplicates
    if text in seen:
        continue

    seen.add(text)

    title = text

    events.append({
        "event_title": title,
        "event_category": "Play",
        "event_type": "Theatre Performance",
        "event_status": "upcoming",

        "venue_name": "Shakespeare's Globe",
        "venue_url": URL,
        "venue_address": "21 New Globe Walk, London",
        "venue_city": "London",
        "venue_country": "UK",
        "venue_capacity": extract_capacity("GLOBE THEATRE"),

        "event_start_date": "2026-05-23",
        "event_end_date": "2026-06-27",

        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M"),

        "performance_schedule": str([{"date": "2026-05-23", "time": "19:30"}]),
        "performance_count": 1,

        "currency_code": "GBP",
        "price_range": price,
        "seat_price_range": price,

        "limited_run_flag": True,

        "event_image": item.find("img")["src"] if item.find("img") else "No Image",

        "event_description": description,
        "data_source": URL
    })


# =========================================================
# CSV OUTPUT
# =========================================================

fieldnames = list(events[0].keys())

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(events)


print(f"SUCCESS → {len(events)} EVENTS EXTRACTED → output.csv - scraper.py:141")