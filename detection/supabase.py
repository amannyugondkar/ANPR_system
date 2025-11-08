from supabase import create_client, Client
import datetime

# Connection details from your Supabase dashboard
url = "https://mwqyrveotnnhmfusirjl.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im13cXlydmVvdG5uaG1mdXNpcmpsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxNjA5NzgsImV4cCI6MjA3NzczNjk3OH0.bHjcVVN3RiksN54lsd65t-lifjSP3eeONjgPcnJUqBg"

supabase: Client = create_client(url, key)

def log_plate_to_supabase(plate, event_type, camera_location, confidence, image_url=None):
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
    print("Inserted:", res)

# In your detection loop:
if stable_text:
    log_plate_to_supabase(
        plate=stable_text,
        event_type="entry",  # or "exit"
        camera_location="Gate Entrance",  # or logic for exit/entrance
        confidence=conf,
        image_url=None  # set if saving image crop
    )

