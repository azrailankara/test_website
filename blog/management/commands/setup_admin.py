from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials'

    def handle(self, *args, **options):
        if not User.objects.filter(username='alper').exists():
            User.objects.create_superuser(
                username='alper',
                email='alper@gmail.com',
                password='alperyceer06'
            )
            self.stdout.write(self.style.SUCCESS('Admin kullanıcısı başarıyla oluşturuldu')) 