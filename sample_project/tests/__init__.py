from unittest import TestCase


class BaseTestCase(TestCase):
    def setUp(self):
        """
            setup function that gets executed before any test
        """
        # self.db = utils.init_db() for example
        pass
