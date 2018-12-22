import unittest

from prayer_times import *


class TestPrayerTimes(unittest.TestCase):
    
    def test_get_ip(self):
        ip = get_ip_address()
        
        self.assertIsNotNone(ip)


if __name__=='__main__':
    unittest.main()