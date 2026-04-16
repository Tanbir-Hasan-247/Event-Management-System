import os
import django
import random
from faker import Faker

# ১. Django এনভায়রনমেন্ট সেটআপ (খুবই গুরুত্বপূর্ণ)
# 'your_project_name' এর জায়গায় আপনার প্রজেক্টের আসল নাম দিন
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings') 
django.setup()

# ২. মডেল ইম্পোর্ট করা
from django.contrib.auth.models import User
# 'your_app_name' এর জায়গায় আপনার অ্যাপের নাম দিন
from events.models import Event, Category 

fake = Faker()

def populate(N=10):
    print("ডেটাবেস পপুলেট করা শুরু হচ্ছে...")

    # কিছু ডিফল্ট ক্যাটাগরি তৈরি করা
    category_names = ['Technology', 'Music', 'Art', 'Sports', 'Education', 'Business']
    category_objs = []
    
    for name in category_names:
        # get_or_create ব্যবহার করা হয়েছে যাতে একই ক্যাটাগরি বারবার তৈরি না হয়
        cat, created = Category.objects.get_or_create(
            name=name,
            defaults={'description': fake.text()}
        )
        category_objs.append(cat)

    # কিছু টেস্ট ইউজার তৈরি করা
    users = []
    for _ in range(5):
        try:
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.email(),
                password='password123' # সব ইউজারের ডিফল্ট পাসওয়ার্ড
            )
            users.append(user)
        except Exception as e:
            pass # ইউজারনেম মিলে গেলে স্কিপ করবে

    # ডেটাবেসে আগে থেকে থাকা ইউজারদেরও নিয়ে আসা
    all_users = list(User.objects.all())

    # ইভেন্ট তৈরি করা
    for _ in range(N):
        # একটি র‍্যান্ডম ক্যাটাগরি নির্বাচন
        random_category = random.choice(category_objs)
        
        event = Event.objects.create(
            name=fake.sentence(nb_words=4)[:-1], # শেষের ডট বাদ দেওয়ার জন্য
            description=fake.paragraph(nb_sentences=5),
            date=fake.future_date(end_date="+30d"), # আগামী ৩০ দিনের মধ্যে যেকোনো তারিখ
            time=fake.time_object(),
            location=fake.address(),
            category=random_category
            # image ফিল্ডটি ডিফল্ট নেবে, তাই ম্যানুয়ালি দেওয়া হয়নি
        )

        # ১ থেকে ৫ জন র‍্যান্ডম ইউজারকে পার্টিসিপেন্ট হিসেবে যুক্ত করা
        if all_users:
            num_participants = random.randint(1, min(5, len(all_users)))
            random_participants = random.sample(all_users, num_participants)
            event.participants.add(*random_participants)

    print(f"সফলভাবে {N} টি ইভেন্ট, ইউজার এবং ক্যাটাগরি তৈরি করা হয়েছে!")

if __name__ == '__main__':
    # আপনি চাইলে এখানে সংখ্যা পরিবর্তন করে আরও বেশি ডেটা তৈরি করতে পারেন
    populate(20)