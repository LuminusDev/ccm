from unittest import TestCase
import os

class Tester(TestCase):

    def __init__(self, *argv, **kwargs):
        super(Tester, self).__init__(*argv, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        if hasattr(self, 'cluster'):
            for node in self.cluster.nodelist():
                self.assertItemsEqual(node.grep_log_for_errors(), [])

            test_path = self.cluster.get_path()
            self.cluster.remove()
            if os.path.exists(test_path):
                os.remove(test_path)
