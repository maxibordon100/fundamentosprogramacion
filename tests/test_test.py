from unittest import TestCase
from src.facturador02 import *

class Test(TestCase):
    def test_exists_article(self):
            result=getData('a1')
            self.assertTrue(result!=None,'The result should be not None')
    def test_cost_by_zone(self):
         self.assertTrue(cost_by_zone['CABA'] == 1000 and cost_by_zone['INTERIOR']==5000 and cost_by_zone['AMBA']== 2000,'the cost by zone should be equal to definition')
    def test_update(self):
        result=update('a1',1)
        self.assertTrue(len(result)==2 and result[0]==True,'The result should have size 2 and should be true')