from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = " "
AUTH_TOKEN = " "
FROM_NUMBER = "whatsapp:6283494493"  # Twilio Sandbox
TO_NUMBER = "whatsapp:+918283098310"   # Your verified WhatsApp number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp(message):
    try:
        client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
        print(f"Sent WhatsApp: {message}")
    except Exception as e:
        print(f"WhatsApp sending failed: {e}")