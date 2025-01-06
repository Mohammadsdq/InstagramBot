from instagrapi import Client
from datetime import datetime
import time

# Instagram account information
username = "Your_Instagram_UserName"  
password = "Your_Instagram_Pass"  
fixed_text = "Your_Custom_Bio"  

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

# Function to update Instagram biography
def update_bio_daily():
    current_date = get_current_date()
    bio_text = f"{current_date}\n{fixed_text}"
    try:
        cl.account_edit(biography=bio_text)
        print(f"✅ Bio updated:\n{bio_text}")
    except Exception as e:
        print(f"❌ Error updating bio: {e}")

# Running the robot by checking every minute
def run_daily_update():
    last_updated_date = None
    while True:
        current_date = datetime.now().date()
        if current_date != last_updated_date:  # If the date has changed
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