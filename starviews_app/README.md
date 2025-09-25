
# Starviews — Demo OTT Web Application


## Overview
Starviews is a simple demo OTT (over-the-top) web application built with Flask. It displays movie titles, posters, ratings and movie details.

## How to run (development)
1. Create a Python virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # on Windows use `venv\Scripts\activate`
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open a browser and visit `http://localhost:5000`

## Project structure
```
starviews_app/
├── app.py
├── data/
│   └── movies.json
├── templates/
│   ├── index.html
│   └── movie.html
├── static/
│   └── css/
│       └── style.css
├── requirements.txt
└── README.md
```

This is a demo project and uses sample data. You can extend it by connecting to an external API like TMDB, adding user accounts, search, filters, and playback features.
