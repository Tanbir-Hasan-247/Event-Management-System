import os
import django
from faker import Faker
import random
import datetime

# ⚠️ WARNING: 'event_management.settings' এর জায়গায় আপনার আসল প্রোজেক্ট ফোল্ডারের নাম দিন
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

# ⚠️ WARNING: 'events' এর জায়গায় আপনার আসল অ্যাপের নাম দিন
from events.models import Category, Event, Participant

def populate_db():
    print("Populating database with fake data...")
    fake = Faker()

    # 1. Create Categories (Minimum 3)
    categories = []
    category_names = ['Tech Conference', 'Music Festival', 'Art Workshop', 'Business Meetup']
    
    for name in category_names:
        # get_or_create ব্যবহার করা হয়েছে যাতে ২ বার রান করলে error না দেয়
        category, created = Category.objects.get_or_create(
            name=name,
            defaults={'description': fake.paragraph()}
        )
        categories.append(category)
    print(f"✅ Created/Verified {len(categories)} Categories.")

    # 2. Create Events (Minimum 5)
    events = []
    for _ in range(5):
        event = Event.objects.create(
            name=fake.sentence(nb_words=4)[:-1],  # Remove the trailing dot
            description=fake.text(),
            date=fake.future_date(end_date='+30d'),
            time=datetime.time(random.randint(9, 18), random.choice([0, 15, 30, 45])), # Random time between 9 AM - 6 PM
            location=fake.address(),
            category=random.choice(categories)
        )
        events.append(event)
    print(f"✅ Created {len(events)} Events.")

    # 3. Create Participants (Minimum 10)
    participants = []
    for _ in range(10):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.unique.email()
        )
        
        # ManyToMany ফিল্ডে ডেটা অ্যাড করা (১ থেকে ৩ টি র‍্যান্ডম ইভেন্টে অ্যাসাইন করা)
        # আপনার মডেলে ManyToMany ফিল্ডের নাম 'event' (singular), তাই participant.event.set() ব্যবহার করা হয়েছে
        random_events = random.sample(events, random.randint(1, 3))
        participant.event.set(random_events)
        
        participants.append(participant)
    print(f"✅ Created {len(participants)} Participants.")

    print("🎉 Database successfully populated with dummy data!")

if __name__ == '__main__':
    populate_db()