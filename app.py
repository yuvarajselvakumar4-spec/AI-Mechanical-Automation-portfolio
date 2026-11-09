import sys
import subprocess

# Flask மற்றும் Twilio லைப்ரரிகள் இல்லையென்றால் ஆட்டோமேட்டிக்காக இன்ஸ்டால் செய்து கொள்ளும் கோட்
for package in ['flask', 'twilio']:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing {package} automatically...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

from flask import Flask, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Twilio சாண்ட்பாக்ஸ் (Sandbox) விவரங்கள் (உன்னுடைய Twilio அக்கவுண்ட் விவரங்களை இங்கு கொடுக்கலாம்)
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_WHATSAPP_FROM = 'whatsapp:+14155238886' # Twilio அதிகாரப்பூர்வ சாண்ட்பாக்ஸ் நம்பர்

@app.route('/')
def home():
    return "MachinaPulse AI Backend Server with Twilio Alerts is Running! 🚀"

# 5 ஏஜெண்டுகளின் லைவ் டேட்டாவை வெப் டேஷ்போர்டுக்கு அனுப்பும் API
@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    data = {
        "status": "Online",
        "active_agents": 5,
        "agents": {
            "maintenance": {"status": "Optimal", "alert": "1 Loom Alert (Machine 03)"},
            "quality": {"status": "98.2%", "alert": "Batch 102 Rejected"},
            "supply_chain": {"status": "Restocking", "alert": "Spare Belts Ordered"},
            "financial": {"status": "₹1.5L Excess", "alert": "Dyeing Power Optimized"},
            "safety": {"status": "Secured", "alert": "Chemical Mixing Handled"}
        },
        "vibration_telemetry": [2.1, 2.5, 3.2, 2.8, 4.1, 5.0, 7.8]
    }
    return jsonify(data)

# வாட்ஸ்அப் அலர்ட் அனுப்பும் API
@app.route('/api/send-alert', methods=['GET'])
def send_whatsapp_alert():
    try:
        # உண்மையான Twilio கணக்கு இணைக்கப்படும்போது கீழே உள்ள கோடு ஒர்க்காகும்
        # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        # message = client.messages.create(
        #     body="🚨 MachinaPulse AI Alert: Machine 03 Vibration High (7.8mm/s)! Auto-shutoff triggered.",
        #     from_=TWILIO_WHATSAPP_FROM,
        #     to='whatsapp:+91your_phone_number'
        # )
        return jsonify({"status": "Success", "message": "WhatsApp Alert simulated and ready for dispatch!"})
    except Exception as e:
        return jsonify({"status": "Error", "error": str(e)}), 500

if __name__ == '__main__':
    print("==================================================")
    print("  MACHINAPULSE AI - BACKEND WITH TWILIO READY     ")
    print("==================================================")
    app.run(debug=True, port=5000)
