import sys
import coverage
import unittest
from scrape import get_total_records,current_target_url,get_json_data
from crud import selectFromBand,selectFromDiscography,selectFromMember
from crud import deleteFromMember,deleteFromDiscography,deleteFromBand,updateMemberName,updateDiscographyName,updateBandName



class travis(unittest.TestCase):


    def test_current_target_url(self):
        self.assertIsNot(current_target_url('https://www.metal-archives.com/',1191),'https://www.metal-archives.com/')


    def test_select_fromBand(self):
        self.assertIsNot(selectFromBand(''),'nombre:cualquiera,country:chicago')

    def test_select_fromDiscografia(self):
        self.assertIsNot(selectFromDiscography(''),'nombre:cualquiera,country:chicago')

    def test_select_fromMember(self):
        self.assertIsNot(selectFromMember(''),'nombre:cualquiera,country:chicago')

    def test_deletes(self):
        self.assertIsNone(deleteFromMember('iron maiden'))
        self.assertIsNone(deleteFromDiscography('iron maiden'))
        self.assertIsNone(deleteFromBand('iron maiden'))

    def test_updates(self):
        self.assertIsNone(updateMemberName('iron maiden','iron maiden'))
        self.assertIsNone(updateDiscographyName('iron maiden','iron maiden'))
        self.assertIsNone(updateBandName('iron maiden','iron maiden'))
        
            
if __name__ =='__main__':
    
    unittest.main()
