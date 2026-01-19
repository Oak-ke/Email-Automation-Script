import os
import json
import tweepy
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_current_eat_time():
    # EAT is UTC+3
    utc_now = datetime.now(timezone.utc)
    eat_now = utc_now + timedelta(hours=3)
    return eat_now

def get_current_slot():
    eat_now = get_current_eat_time()
    hour = eat_now.hour
    
    # Scheduled for 8 AM and 6 PM EAT
    # Allowing a small window (e.g., within the hour)
    if hour == 8:
        return "Morning"
    elif hour == 18:
        return "Evening"
    return None

def post_to_x(text):
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_KEY_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_token_secret]):
        print("Error: X API credentials missing in environment variables.")
        return False

    try:
        # Using Tweepy Client for v2 API
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        response = client.create_tweet(text=text)
        print(f"Successfully posted tweet! ID: {response.data['id']}")
        return True
    except Exception as e:
        print(f"Failed to post tweet: {e}")
        return False

def publish_joke():
    slot = get_current_slot()
    if not slot:
        # For testing purposes, we can override the slot via env var
        slot = os.getenv("FORCE_SLOT")
        if not slot:
            print(f"Current time {get_current_eat_time().strftime('%H:%M')} EAT is not a scheduled slot. Use FORCE_SLOT=Morning/Evening to test.")
            return

    print(f"Target slot: {slot}")

    if not os.path.exists("jokes_queue.json"):
        print("Error: jokes_queue.json not found.")
        return

    with open("jokes_queue.json", "r", encoding="utf-8") as f:
        jokes_data = json.load(f)

    joke_to_post = None
    selected_country_index = -1
    selected_joke_index = -1

    # Find the first unposted joke for the current slot
    for c_idx, country_entry in enumerate(jokes_data):
        for j_idx, joke_entry in enumerate(country_entry["jokes"]):
            if joke_entry["slot"] == slot and not joke_entry.get("posted", False):
                joke_to_post = joke_entry["text"]
                selected_country_index = c_idx
                selected_joke_index = j_idx
                break
        if joke_to_post:
            break

    if joke_to_post:
        print(f"Preparing to post {slot} joke for {jokes_data[selected_country_index]['country']}...")
        success = post_to_x(joke_to_post)
        
        if success:
            # Mark as posted
            jokes_data[selected_country_index]["jokes"][selected_joke_index]["posted"] = True
            with open("jokes_queue.json", "w", encoding="utf-8") as f:
                json.dump(jokes_data, f, indent=4, ensure_ascii=False)
            print("jokes_queue.json updated.")
    else:
        print(f"No unposted jokes found for the {slot} slot.")

if __name__ == "__main__":
    publish_joke()
