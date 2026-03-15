# Flask App — Setup & Run

## Project Structure
```
flask-app/
├── app.py                  # Flask server (Python)
├── requirements.txt        # Python dependencies
├── netlify.toml            # Netlify config
├── templates/
│   └── index.html          # Jinja2 HTML template
└── static/
    ├── styles.css          # All CSS
    └── main.js             # All JavaScript
```

## Run Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the server:
   ```
   python app.py
   ```

3. Open your browser at: http://localhost:5000

## Deploy to Netlify

1. Push this folder to a GitHub repository
2. Go to https://app.netlify.com → "Add new site" → "Import from Git"
3. Netlify will auto-detect the config from `netlify.toml`
4. Click Deploy

## How It Works

- `app.py` is the brain — it serves pages and handles requests
- `templates/index.html` is rendered by Flask using Jinja2 (the `{% for %}` loop generates the option cards from Python data)
- When a user clicks an option, `main.js` sends it to the `/select` route in `app.py`
- To change the options, edit the `OPTIONS` list in `app.py`