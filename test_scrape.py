import unittest
from scrape import get_total_records,current_target_url,get_json_data
from crud import selectFromBand,selectFromDiscography,selectFromMember
from crud import deleteFromMember,deleteFromDiscography,deleteFromBand,updateMemberName,updateDiscographyName,updateBandName



class travis(unittest.TestCase):


    def test_current_target_url(self):
        self.assertIsNot(current_target_url('https://www.metal-archives.com/',1191),'https://www.metal-archives.com/')


    def test_select_fromBand(self):
        self.assertIsNot(selectFromBand(''),'Name: Cristoffer Matlak ,Band:Jhator,Location: Alingsås,Status: Active,Formed In: N/A,Genre: Death n Roll')

    def test_select_fromDiscografia(self):
        self.assertIsNot(selectFromDiscography(''),'Name: Christer "Grendel" Olsson,Country: Sweden,Location: N/A,Status: Unknown,Genre: Atmospheric Black Metal')

    def test_select_fromMember(self):
        self.assertIsNot(selectFromMember(''),'Name: 12 Gauge Dead,Country: Sweden,Location: Linköping,Status: Split-up,Formed In: 2004,Years Active: 2004-2007')

    def test_deletes(self):
        self.assertIsNone(deleteFromMember(' 1 iron maiden'))
        self.assertIsNone(deleteFromDiscography(' 2 Ton Predator'))
        self.assertIsNone(deleteFromBand(' 2 Ton Predator'))

    def test_updates(self):
        self.assertIsNone(updateMemberName(' Christer "Grendel" Olsson',' Cristoffer Matlak'))
        self.assertIsNone(updateDiscographyName(' Magnus Nilsson',' Tobbe'))
        self.assertIsNone(updateBandName('Ton Predator','Ton Predator'))
        
            
if __name__ =='__main__':
    
    unittest.main()
