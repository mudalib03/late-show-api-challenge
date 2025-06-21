from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

app = create_app()

with app.app_context():
    print("Clearing existing data...")
    db.drop_all()
    db.create_all()

    print("Seeding users...")
    user1 = User(username="admin")
    user1.set_password("password123")
    db.session.add(user1)

    print("Seeding guests...")
    guest1 = Guest(name="John Doe", occupation="Comedian")
    guest2 = Guest(name="Jane Smith", occupation="Musician")
    db.session.add_all([guest1, guest2])

    print("Seeding episodes...")
    episode1 = Episode(date=date(2024, 1, 1), number=1)
    episode2 = Episode(date=date(2024, 1, 8), number=2)
    db.session.add_all([episode1, episode2])

    print("Seeding appearances...")
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=3, guest=guest1, episode=episode2)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print("Seeding complete!")
