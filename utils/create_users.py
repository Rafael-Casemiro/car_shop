import os
import sys
from pathlib import Path
import django
from django.conf import settings
from django.contrib.auth.hashers import make_password

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker
    from user.models import User

    # Clear existing users
    print("Deleting existing users...")
    User.objects.all().delete()

    fake = faker.Faker('pt_BR')
    django_contacts = []
    
    # 1. Create a set to track emails we have already generated
    seen_emails = set()

    # 2. Use a standard password for performance (hashing 1000 times is slow)
    default_password = make_password('mypassword')

    print("Generating user data...")

    # 3. Use a while loop to ensure we get exactly 1000 UNIQUE users
    while len(django_contacts) < NUMBER_OF_OBJECTS:
        profile = fake.profile()
        email = profile['mail']

        # 4. If this email was already generated, skip this iteration
        if email in seen_emails:
            continue

        seen_emails.add(email)

        name_parts = profile['name'].split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        phone = fake.phone_number()

        django_contacts.append(
            User(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=default_password,
                is_active=True
            )
        )

    if len(django_contacts) > 0:
        print(f"Inserting {len(django_contacts)} users into the database...")
        User.objects.bulk_create(django_contacts)
        print("Done!")