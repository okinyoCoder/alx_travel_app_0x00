from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from datetime import date, timedelta
import uuid
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        # Create sample listings
        for i in range(5):
            listing = Listing.objects.create(
                listing_id=uuid.uuid4(),
                name=f"Sample Listing {i+1}",
                description="This is a sample description for the listing.",
                location="Nairobi",
                pricepernight=random.uniform(50, 200)
            )

            # Create a booking for each listing
            booking = Booking.objects.create(
                booking_id=uuid.uuid4(),
                listing=listing,
                start_date=date.today(),
                end_date=date.today() + timedelta(days=3),
                total_price=listing.pricepernight * 3,
                status='confirmed'
            )

            # Create a review for each listing
            Review.objects.create(
                review_id=uuid.uuid4(),
                listing=listing,
                rating=random.randint(1, 5),
                comment="This is a sample review."
            )

        self.stdout.write(self.style.SUCCESS("✅ Seeded Listings, Bookings, and Reviews."))
