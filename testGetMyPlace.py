#!/usr/bin/python

import unittest
from getMyPlaces import getMyPlaces

target_places = [
      {'time': 1402846860, 'place_id': 4, 'place_name': u'Golden Gate Bridge', 'photo_url': u'http://media-cdn.tripadvisor.com/media/daodao/photo-s/05/80/ee/59/caption.jpg', 'cid': 4},
      {'time': 1402838220, 'place_id': 3, 'place_name': u'Ghirardelli Square', 'photo_url': u'http://media-cdn.tripadvisor.com/media/photo-s/01/bf/63/01/ghirardelli.jpg', 'cid': 3},
      {'time': 1402830120, 'place_id': 2, 'place_name': u"Fishermen's Wharf", 'photo_url': u'http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg', 'cid': 2},
      {'time': 1402828440, 'place_id': 1, 'place_name': u'Pier 39', 'photo_url': u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f2/99/pier-39.jpg', 'cid': 1}]

class TestGetMyPlace(unittest.TestCase):

   def setUp(self):
      self.user1_places = getMyPlaces("1")
      self.user2_places = getMyPlaces("2")
      self.user3_places = getMyPlaces("3")

   def test_user1_places(self):
      # test the lenth of the result list of user1 should be equal to the target list
      self.assertEqual(len(target_places), len(self.user1_places))

      # test the places in user1's checkin list, order matters
      i = 0
      for result_place in self.user1_places:
         # test each field in the place
         target_place = target_places[i]
         # test 'cid'
         self.assertEqual(target_place['cid'], result_place['cid'])
         # test 'time'
         self.assertEqual(target_place['time'], result_place['time'])
         # test 'place_id'
         self.assertEqual(target_place['place_id'], result_place['place_id'])
         # test 'place_name'
         self.assertEqual(target_place['place_name'], result_place['place_name'])
         # test 'photo_url'
         self.assertEqual(target_place['photo_url'], result_place['photo_url'])
         i += 1

   def test_user2_places(self):
      # test the user2's checkin list should be empty
      self.assertEqual([], self.user2_places)

   def test_user3_places(self):
      # test the user2's checkin list should be empty
      self.assertEqual([], self.user3_places)
      
if __name__ == '__main__':
    unittest.main()
