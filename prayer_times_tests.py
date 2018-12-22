import unittest

from prayer_times import *


class TestPrayerTimes(unittest.TestCase):
    
    def test_get_ip(self):
        ip = get_ip_address()
        
        self.assertIsNotNone(ip)
     
    def test_get_address_from_ip(self):
        ip = '67.174.76.53'
        address = get_address_from_ip(ip)
        
        self.assertIn('city', address)
        self.assertIn('state', address)
        self.assertIn('country', address)
        
        
if __name__=='__main__':
    unittest.main()