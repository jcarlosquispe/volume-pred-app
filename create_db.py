from app import app, db
from app.models import Location


with app.app_context():
    # Create the database and the database table
    db.drop_all()
    print("Dropped all tables")

    db.create_all()
    print("Database created.")

    # Insert sample data
    #sample_location = Location(uuid="expected_qr_code_value", name="Sample Location")
    #db.session.add(sample_location)
    db.session.commit()
    print("Sample data added.")