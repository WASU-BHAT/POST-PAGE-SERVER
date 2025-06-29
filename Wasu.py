from flask import Flask, render_template_string, session
from datetime import datetime
import os
import random
import string
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True

# 🔐 Approval config
APPROVAL_URL = "https://raw.githubusercontent.com/TOKEN-CHAKER/approved.json/main/approved.json"
OWNER_CONTACT = '917209101285'

# 🔑 Generate unique user key
def generate_user_key():
    parts = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(30)]
    return 'BROKEN-NADEEM-' + '-'.join(parts)

# ✅ Check if key is approved
def is_key_approved(key):
    try:
        res = requests.get(APPROVAL_URL)
        if res.status_code == 200:
            approved = res.json().get("approved", [])
            return key in approved
    except Exception as e:
        print(f"[❌ ERROR] While checking approval: {e}")
    return False

# 🔐 Approval check before every request
@app.before_request
def approval_required():
    if 'approved' not in session:
        if 'user_key' not in session:
            session['user_key'] = generate_user_key()
        key = session['user_key']
        if is_key_approved(key):
            session['approved'] = True
        else:
            return render_template_string('''
                <h2>🚫 Approval Required</h2>
                <p>Your Access Key:</p>
                <textarea rows="3" cols="60" readonly>{{ key }}</textarea><br><br>
                <a href="https://wa.me/{{ owner }}?text=Hello%20Broken%20Nadeem%2C%20Please%20approve%20my%20key%3A%20{{ key }}" target="_blank">
                    <button style="padding: 10px 20px; font-size: 16px; background: red; color: white; border: none; border-radius: 6px;">
                        CONTACT OWNER FOR APPROVAL
                    </button>
                </a>
                <meta http-equiv="refresh" content="5">
            ''', key=key, owner=OWNER_CONTACT)

# 🧠 HTML TEMPLATE
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>😚❤️ OFFLINE ALL SERVICES BY NADEEM ❤️😚</title>
  <style>
    body { font-family: sans-serif; background-color: #f4f4f4; text-align: center; padding: 20px; }
    h2 { color: #ff0000; }
    .timer { font-size: 20px; margin-bottom: 10px; }
    .date { font-weight: bold; margin-bottom: 20px; }
    .box { border: 2px solid #000; border-radius: 10px; padding: 15px; margin: 15px auto; width: 90%; max-width: 500px; background: #fff; }
    .btn { padding: 10px 20px; background: #000; color: white; border: none; border-radius: 6px; margin-top: 10px; display: inline-block; cursor: pointer; }
    .footer { margin-top: 40px; font-size: 14px; }
  </style>
</head>
<body>
  <h2>🎋 OFFLINE WEB SERVICE 🎋</h2>
  <div class="timer" id="timer">Loading timer...</div>
  <div class="date">📆 LIVE DATE::⪼ {{ current_date }}</div>

  {% for box in boxes %}
  <div class="box">
    <img src="{{ box.image }}" alt="img" width="100%" style="border-radius: 10px;">
    {% if box.text %}<h3>{{ box.text }}</h3>{% endif %}
    {% if box.link %}
      {% if loop.index0 == 0 %}
        <button class="btn" onclick="checkPassword('{{ box.link }}')">{{ box.button }}</button>
      {% else %}
        <a href="{{ box.link }}" class="btn">{{ box.button }}</a>
      {% endif %}
    {% endif %}
  </div>
  {% endfor %}

  <div class="footer">
    <p>
      <a href="/terms">Terms</a> | <a href="/privacy">Privacy</a>
    </p>
    <p>
      <a href="https://www.facebook.com/profile.php?id=61574766223435">Facebook</a> |
      <a href="http://fi9.bot-hosting.net:20566/">WhatsApp</a> |
      <a href="https://github.com/devixayyat/">GitHub</a>
    </p>
    <p>© 2025 BROKEN NADEEM  All RIGHTS RESERVED.</p>
    <p>MADE WITH BROKEN NADEEM BY <b>ALIYA</b></p>
  </div>

  <script>
    function updateTimer() {
      const now = new Date();
      const time = now.toLocaleTimeString();
      document.getElementById("timer").innerText = "⌛ LIVE TIMER::⪼ " + time;
    }
    setInterval(updateTimer, 1000);
    updateTimer();

    function checkPassword(link) {
      const pass = prompt("🎋🛡 ENTER PASSWORD TO ACCESS THIS SERVER 🎋🛡");
      if (pass === "NADEEMXALIYA") {
        window.location.href = link;
      } else {
        alert("❌ BROKEN NADEEM TERE KO REJECT KAR DIYA..😞❤️");
      }
    }
  </script>
</body>
</html>
'''

# 🖼️ ROUTE
@app.route('/')
def home():
    boxes = [
        {"image": "https://i.ibb.co/Q7dNqdNh/file-00000000ff8061f7a01431f6494b45dc.png", "text": "", "link": "https://post-serverx-9.onrender.com", "button": "⊲ PRIVATE SERVER ONLY ADMIN ⊳"},
        {"image": "https://i.ibb.co/bMKrvTwJ/file-00000000b67861f78acd701aea0eae98.png", "text": "", "link": "https://messenger-loader-9.onrender.com", "button": "⊲ NEW OFFLINE NON SERVER 1 ⊳"},
        {"image": "https://i.ibb.co/jP7sh1Qn/IMG-20250502-WA0170.jpg", "link": "https://page-server-fr9f.onrender.com", "button": "⊲ OFFLINE NONSTOP SERVER 2 ⊳"},
        {"image": "https://i.ibb.co/mVZgP9pw/IMG-20250502-WA0174.jpg", "link": "https://token-chaker-by-broken-nadeemx.onrender.com", "button": "⊲ CLICK HERE CHECK TOKEN ⊳"},
        {"image": "https://i.ibb.co/N2yGmhj7/IMG-20250503-WA0069.jpg", "link": "http://fi3.bot-hosting.net:22911/", "button": "⊲ FB CONVO FYT GROUP UID ⊳"},
        {"image": "https://i.ibb.co/jPSZghg0/IMG-20250503-WA0072.jpg", "link": "http://fi11.bot-hosting.net:20995/", "button": "⊲ FB OFFLINE POST SERVER ⊳"},
        {"image": "https://i.ibb.co/fVkpjX1J/IMG-20250503-WA0125.jpg", "link": "https://create-boy-beoken-nadeem.onrender.com", "button": "⊲ OFFLINE NONSTOP SERVER 3 ⊳"},
        {"image": "https://i.ibb.co/TxTt6pSx/IMG-20250525-WA0204.jpg", "link": "http://fi9.bot-hosting.net:22115/", "button": "⊲ FB TOKEN GENERATOR ⊳"},
        {"image": "https://i.ibb.co/bMKrvTwJ/file-00000000b67861f78acd701aea0eae98.png", "link": "http://fi9.bot-hosting.net:20566/", "button": "⊲ NEW OFFLINE NON SERVER ⊳"},
        {"image": "https://i.ibb.co/7dZFmH7M/IMG-20250502-WA0171.jpg", "link": None, "button": None}
    ]
    current_date = datetime.now().strftime("%d %B %Y").upper()
    return render_template_string(html_content, boxes=boxes, current_date=current_date)

# ▶️ RUN
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
