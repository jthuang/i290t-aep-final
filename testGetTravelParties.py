#!/usr/bin/python

import unittest
from getTravelParties import getTravelParties

target_travel_parties1 = [
      {'pic_url': u'http://placehold.it/42x42', 'uid': 2, 'name': u'Chan'},
      {'pic_url': u'http://placehold.it/42x42', 'uid': 3, 'name': u'JT'}
]

travel_parties2 = []

class TestGetTravelParties(unittest.TestCase):

   def setUp(self):
      self.travel_parties1 = getTravelParties("1")
      self.travel_parties2 = getTravelParties("2")
      self.travel_parties5 = getTravelParties("5")    # out of range

   def test_travel_parties_1(self):
      # make sure the travel party members in checkin #1 is correct
      result_travel_parties = self.travel_parties1

      # test 'travel_parties' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_travel_parties1), len(result_travel_parties))
      match_cnt = 0
      for target_user in target_travel_parties1:
         for result_user in result_travel_parties:
            if target_user['uid'] == result_user['uid']:
               self.assertEqual(target_user['name'], result_user['name'])
               self.assertEqual(target_user['pic_url'], result_user['pic_url'])
               match_cnt += 1
      self.assertEqual(len(target_travel_parties1), match_cnt)

      
   def test_travel_parties_2(self):
      # checkin #2 has no travel parties, return empty list
      self.assertEqual([], self.travel_parties2)


   def test_travel_parties_5(self):
      # out of range, should return empty list
      self.assertEqual([], self.travel_parties5)
      
if __name__ == '__main__':
    unittest.main()
