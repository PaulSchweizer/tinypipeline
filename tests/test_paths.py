import re
import unittest

from tinypipeline.core.paths import Paths
from tinypipeline.core import config


class TestPaths(unittest.TestCase):
    """Test the Paths class."""

    def test_get(self):
        """Get various paths."""
        regex = re.compile(r'\{(.*?)\}')
        for name, pattern in config.patterns.items():
            kwargs = {p: 'REPLACED' for p in regex.findall(pattern)}
            path = getattr(Paths, name)(**kwargs)
            self.assertTrue(path.startswith(config.root))
            self.assertEqual(path.count('REPLACED'), len(kwargs.keys()))
        # end for

        with self.assertRaises(AttributeError):
            Paths.does_not_exist(var='a')
        # end with
    # end def test_get
# end class TestPaths


if __name__ == '__main__':
    unittest.main()
# end if
