import urllib.request, time, json, requests, os
from urlextract import URLExtract
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import unittest
from scrape import get_total_records,current_target_url,get_json_data


class travis(unittest.TestCase):

    def test_current_target_url(self):
        self.assertIsNot(current_target_url('https://www.metal-archives.com/',1191),'https://www.metal-archives.com/')

'''
    def test_get_total_records(self):
        self.assertIsNot(str(get_total_records('https://www.metal-archives.com/browse/ajax-country/c/SE/json/1')),'dasda')


    
    def test_get_json_data(self):
        self.assertNotEqual(get_json_data('https://www.metal-archives.com/'),'')
        

'''
        
if __name__ =='__main__':
    
    unittest.main()
