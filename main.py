from instagrapi import Client
from datetime import datetime
import time
import requests

# Instagram account information
username = "Your_Instagram_ID"  
password = "Your_Instagram_Pass"  
fixed_text = "Your_Personal_Bio_In_Instagrsm"  

# Log in to your Instagram account
cl = Client()

try:
    cl.login(username, password)
    print("✅ Logged in successfully!")
except Exception as e:
    print(f"❌ Error during login: {e}")
    exit()

# Function to get the date in AD
def get_current_date():
    return datetime.now().strftime("%A, %B %d, %Y")

# Function to get random fact from API
def get_random_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        response.raise_for_status()
        fact = response.json().get("text", "No fact available today.")
        return fact
    except Exception as e:
        print(f"❌ Error fetching fact: {e}")
        return "Couldn't fetch a fact today."

# Function to update Instagram biography
def update_bio_daily():
    current_date = get_current_date()
    random_fact = get_random_fact()
    bio_text = f"{current_date}\n{fixed_text}\n🧠 Fact: {random_fact}"
    try:
        cl.account_edit(biography=bio_text)
        print(f"✅ Bio updated:\n{bio_text}")
    except Exception as e:
        print(f"❌ Error updating bio: {e}")

# Run the robot by checking every minute
def run_daily_update():
    last_updated_date = None
    while True:
        current_date = datetime.now().date()
        if current_date != last_updated_date: 
            print("⏰ Updating bio for the new day...")
            update_bio_daily()
            last_updated_date = current_date
        else:
            print("✅ Bio already updated today. Waiting...")
        
        time.sleep(60)  # Check every minute

# ✅ Continuous execution of the robot
try:
    print("🚀 Starting the Instagram Bio Updater Bot...")
    update_bio_daily()  # Initial update
    run_daily_update()  # Perpetual loop implementation
except KeyboardInterrupt:
    print("🛑 Bot stopped manually!")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
