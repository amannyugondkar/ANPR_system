import os
from supabase import create_client, Client
import datetime

# Fetch from environment variables
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(url, key)

def log_plate_to_supabase(plate, event_type, camera_location, confidence, image_url=None):
    try:
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        data = {
            "plate": plate,
            "timestamp": now,
            "event_type": event_type,
            "camera_location": camera_location,
            "confidence": confidence,
            "image_url": image_url
        }

        res = supabase.table("plate_logs").insert(data).execute()

        if res.data:
            print("✅ Inserted:", res.data)
        else:
            print("⚠️ No data returned. Response:", res)
    except Exception as e:
        print("❌ Error inserting:", e)
