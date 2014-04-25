#!/usr/bin/python

import unittest
from getPlacePhotos import getPlacePhotos

target_place_photos1 = [
      u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f2/99/pier-39.jpg',
      u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f0/f7/the-boys.jpg',
      u'http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg'
]
target_place_photos3 = [
      u'http://media-cdn.tripadvisor.com/media/photo-s/01/bf/63/01/ghirardelli.jpg'
]

class TestGetPlacePhotos(unittest.TestCase):

   def setUp(self):
      self.place_photos1 = getPlacePhotos("1")
      self.place_photos3 = getPlacePhotos("3")
      self.place_photos5 = getPlacePhotos("5")     # out of range

   def test_place_photos_1(self):
      # make sure the photo in checkin #1 are all correct
      result_place_photos = self.place_photos1

      # test 'photos' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place_photos1), len(result_place_photos))
      match_cnt = 0
      for target_photo_url in target_place_photos1:
         for result_photo_url in result_place_photos:
            if target_photo_url == result_photo_url:
               match_cnt += 1
      self.assertEqual(len(target_place_photos1), match_cnt)


   def test_place_photos_3(self):
      # make sure the photo in checkin #3 are all correct
      result_place_photos = self.place_photos3

      # test 'photos' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place_photos3), len(result_place_photos))
      match_cnt = 0
      for target_photo_url in target_place_photos3:
         for result_photo_url in result_place_photos:
            if target_photo_url == result_photo_url:
               match_cnt += 1
      self.assertEqual(len(target_place_photos3), match_cnt)


   def test_place_photos_5(self):
      # out of range, should return empty info
      self.assertEqual([], self.place_photos5)
      
if __name__ == '__main__':
    unittest.main()
