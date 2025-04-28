import requests

def real_time_breach_alerts(telegram_channel):
    try:
        bot_token = input("Enter your Telegram Bot Token: ").strip()  # Get bot token from user
        chat_id = telegram_channel.strip()  # Use the chat ID (could be channel or group ID)

        message = "Security alert: Potential breach detected!"  # Customize the alert message

        # Send message to the specified Telegram chat
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        params = {
            'chat_id': chat_id,
            'text': message
        }

        response = requests.post(url, data=params)

        if response.status_code == 200:
            print(f"[+] Alert sent to {chat_id}")
        else:
            print(f"[-] Failed to send alert: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"[-] Error while sending alert: {str(e)}")
