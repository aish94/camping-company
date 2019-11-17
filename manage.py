#!/usr/bin/env python
import os
import sys
from utils import count_words_at_url
from rq import Queue
from worker import conn

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "camping.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    q = Queue(connection=conn)
    result = q.enqueue(count_words_at_url, 'http://heroku.com')
    execute_from_command_line(sys.argv)
