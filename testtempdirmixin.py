import tempfile
import shutil

class TestTempDirMixin:
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        super().setUp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)


# Example usage:
# (Note because of the MRO, you must inherit the mixin first)

# import unittest
# import os
# class TestFoo(TestTempDirMixin, unittest.TestCase):
#     def test_blah(self):
#         with open(os.path.join(self.tempdir, 'scratchfile.txt'), 'w') as sink:
#             sink.write('something')
