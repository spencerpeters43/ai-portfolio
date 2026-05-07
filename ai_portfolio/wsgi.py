import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio.settings')

application = get_wsgi_application()

# Serve media files (screenshots, resume, etc.) via WhiteNoise in production
BASE_DIR = Path(__file__).resolve().parent.parent
application = WhiteNoise(application, root=str(BASE_DIR / 'media'), prefix='media')
