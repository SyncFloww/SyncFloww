# This migration is kept for history compatibility.
# User and Profile models were consolidated into 0001_initial.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        # No operations needed — User model is now defined in 0001_initial.
    ]
