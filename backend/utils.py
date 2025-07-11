# utils.py
team_abbr = {
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians",
    "RCB": "Royal Challengers Bangalore",
    "KKR": "Kolkata Knight Riders",
    "SRH": "Sunrisers Hyderabad",
    "RR": "Rajasthan Royals",
    "PBKS": "Punjab Kings",
    "DC": "Delhi Capitals",
    "GT": "Gujarat Titans",
    "LSG": "Lucknow Super Giants",
    "GL": "Gujarat Lions",
    "RPS": "Rising Pune Supergiants"
}

import re

def normalize_query(query):
    for abbr, full in team_abbr.items():
        query = re.sub(r'\b' + abbr + r'\b', full, query, flags=re.IGNORECASE)
    return query
