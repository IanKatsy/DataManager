# DataManager

A minimal Flask API to extract a Steam profile’s avatar image from a public profile URL.

## Features

- `/api/steam?steam-url=<url>`  
  Returns the second avatar image from a Steam profile as JSON.

## Usage

**Request:**
```
GET /api/steam?steam-url=https://steamcommunity.com/id/username
```
**Response:**
```json
{
    "image": "https://cdn.fastly.steamstatic.com/steamcommunity/public/images/items/...",
    "error": "none"
}
```
Deploying on Vercel
Clone this repo.
Install dependencies:
shpip install -r requirements.txt


Deploy to Vercel (import your repo, no extra config needed).
## Project Structure
```
DataManager/
├── api/
│   └── steam.py
├── requirements.txt
└── vercel.json
```

### Requirements
Python 3.8+
Flask
requests
beautifulsoup4
### License
MIT
