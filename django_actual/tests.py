from django.core.management import call_command
from django.test import TestCase


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import sys
import random


class TestSecretKeyGenerator(TestCase):
    def setUp(self):
        super().setUp()

    def test_generate_secret_key(self):
        """ Test generation of a secret key """
        out = StringIO()
        sys.stdout = out

        for i in range(10):
            random_number = random.randrange(10, 100)
            call_command('generate_secret_key', length=random_number, stdout=out)
            secret_key = self._get_secret_key(out.getvalue())

            out.truncate(0)
            out.seek(0)

            assert len(secret_key) == random_number

    def _get_secret_key(self, result):
        """ Get only the value of a SECRET_KEY """
        for index, key in enumerate(result):
            if key == ':':
                return str(result[index + 1:]).strip()


class TestScaffoldGenerator(TestCase):
    def setUp(self):
        super().setUp()

    def test_generate_forum_scaffold(self):
        pass