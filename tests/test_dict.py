import unittest
from utils import dicts


class TestDict(unittest.TestCase):


    def test_get(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs"), "mercurial")
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), "mercurial")
        self.assertEqual(dicts.get_val({}, "vcs", "git"), "git")
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), "bazaar")

