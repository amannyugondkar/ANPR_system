import os
from supabase import create_client, Client
import datetime

# Fetch from environment variables
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(url, key)
import psycopg2

# Replace with your actual Supabase DB credentials
host = "db.your-project-id.supabase.co"
database = "postgres"
user = "postgres"
password = "your-database-password"
port = "5432"

try:
    # Connect to Supabase (PostgreSQL)
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )

    print("Connected to Supabase!")

    # Create cursor (like Statement in Java)
    cur = conn.cursor()

    # Execute query
    cur.execute("SELECT * FROM your_table_name")

    # Fetch results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close connection
    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
            while (rs.next()) {
                System.out.println(rs.getString(1));
            }

            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
