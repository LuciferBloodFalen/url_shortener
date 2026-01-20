from django.db import models

import string
import random

class UrlMapping(models.Model):
    original_url = models.TextField()
    short_code = models.CharField(max_length=7, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.BigIntegerField(default=0)

    def generate_short_code(self):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(6))
    
    def save(self, *args, **kwargs):
        if not self.short_code:
            while True:
                code = self.generate_short_code()
                if not UrlMapping.objects.filter(short_code=code).exists():
                    self.short_code = code
                    break
        super().save(*args, **kwargs)
    
    # Improvements
    # transaction.atomic
    # IntegrityError
