#!/usr/bin/env python3
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Ensure at least one user exists
        if not User.objects.exists():
            User.objects.create_user(username="host1", email="host1@example.com", password="password123")

        host = User.objects.first()

        # Create 10 sample listings
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                price_per_night=random.randint(50, 500),
                host=host
            )

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully!"))
