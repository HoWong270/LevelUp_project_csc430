import requests

MAILGUN_API_KEY = "6548d4f66f803865f0eb4c4eafae8ae7-a908eefc-b6fa72f7"
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox0d8ba2a382254687951bab6f2afc2239.mailgun.org/messages"
FROM_EMAIL_ADDRESS="postmaster@sandbox0d8ba2a382254687951bab6f2afc2239.mailgun.org"

def send_email(to_address: str, subject: str, message: str):
    resp=requests.post(
        MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": to_address,
            "subject": subject,
            "text": message,
        }
    )

    if resp.status_code == 200:
        print("Success! Email sent.")

send_email("egor.gusev2018@gmail.com","This is a test email.","This is a test message.")
    