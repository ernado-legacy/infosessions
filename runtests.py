#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

from django.conf import settings
from django.test.utils import get_runner


def run():
    r = get_runner(settings)
    test_runner = r()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    run()