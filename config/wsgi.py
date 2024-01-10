"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# 追加
sys.path.append('/home/ec2-user/Django/gptapp2/config')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.append('/home/ec2-user/Django/env/lib/python3.11/site-packages')

application = get_wsgi_application()

site.addsitedir('/home/ec2-user/Django/env/lib/python3.11/site-packages')