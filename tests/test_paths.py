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
            kwargs = {p: 'REPLACED' for p in regex.findall(pattern) if 'version' not in p}
            kwargs['version'] = 1
            path = getattr(Paths, name)(**kwargs)
            self.assertTrue(path.startswith(config.root))
            self.assertGreaterEqual(path.count('REPLACED'), len(kwargs.keys())-1)
        # end for

        with self.assertRaises(AttributeError):
            Paths.does_not_exist(var='a')
        # end with
    # end def test_get

    def test_version_padding(self):
        """Make the padding dynamic."""
        config.patterns['test'] = '{version:0>{padding}}'
        config.padding = 4
        self.assertTrue(Paths.test(padding=4, version=1).endswith('0001'))
    # end def test_version_padding
# end class TestPaths


if __name__ == '__main__':
    unittest.main()
# end if
