
#!/usr/bin/env bash
# run the app in a virtualenv (development)
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
