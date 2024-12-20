import uuid
from datetime import datetime
from app import app, db
from app.models import Location

# Generate random locations
def generate_random_locations(n):
    locations = []
    for _ in range(n):
        location_uuid = str(uuid.uuid4())
        location_name = f"Location {location_uuid[:8]}"
        created_at = datetime.utcnow()
        locations.append(Location(uuid=location_uuid, name=location_name, created_at = created_at))
    return locations

with app.app_context():
    # Create the database and the database table
    db.create_all()
    print("Database created")
    # Insert randomly generated data
    random_locations = generate_random_locations(10)
    db.session.bulk_save_objects(random_locations)
    db.session.commit()
    print("Migration completed: 10 random locations added.")