#!/usr/bin/python

import unittest
from getPlaceDetail import getPlaceDetail

target_place1 = {
   'place_id': 1,
   'name': u'Pier 39',
   'time': 1402828440,
   'perm': 0,
   'cid': 1,
   'host_uid': 1,
   'lat': 37.808673,
   'long': -122.409821,
   'users': [
      {'pic_url': u'http://placehold.it/42x42', 'uid': 1, 'name': u'Wendy'},
      {'pic_url': u'http://placehold.it/42x42', 'uid': 2, 'name': u'Chan'},
      {'pic_url': u'http://placehold.it/42x42', 'uid': 3, 'name': u'JT'}
   ],
   'photo_urls': [
      u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f2/99/pier-39.jpg',
      u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f0/f7/the-boys.jpg',
      u'http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg'
   ],
   'comments': [
      {'comment_str': u"Enjoyed hanging out with friends here. It's a lively place with nice view of the bay and so many restaurants to choose from. Pier 39 is worth a visit.", 'comment_id': 1, 'uid': 1},
      {'comment_str': u'The animals are so cute! They were pushing each other. One of them looked like Chan! Haha', 'comment_id': 2, 'uid': 1},
      {'comment_str': u'My favorites were the piano stairs and the Mirror Maze upstairs.', 'comment_id': 3, 'uid': 1}
   ]
}

target_place2 = {
   'place_id': 2,
   'name': u"Fishermen's Wharf",
   'time': 1402830120,
   'perm': 0,
   'cid': 2,
   'host_uid': 1,
   'lat': 37.808673,
   'long': -122.409821,
   'users': [{'pic_url': u'http://placehold.it/42x42', 'uid': 1, 'name': u'Wendy'}],
   'photo_urls': [u'http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg'],
   'comments': []
}


class TestGetMyPlace(unittest.TestCase):

   def setUp(self):
      self.place_detail1 = getPlaceDetail("1")
      self.place_detail2 = getPlaceDetail("2")
      self.place_detail5 = getPlaceDetail("5")     # out of range

   def test_places_detail_1(self):
      # make sure the data in each field of place 1 is correct
      result_detail = self.place_detail1

      # test 'place_id'
      self.assertEqual(target_place1['place_id'], result_detail['place_id'])
      # test 'name'
      self.assertEqual(target_place1['name'], result_detail['name'])
      # test 'time'
      self.assertEqual(target_place1['time'], result_detail['time'])
      # test 'perm'
      self.assertEqual(target_place1['perm'], result_detail['perm'])
      # test 'cid'
      self.assertEqual(target_place1['cid'], result_detail['cid'])
      # test 'host_uid'
      self.assertEqual(target_place1['host_uid'], result_detail['host_uid'])
      # test 'lat'
      self.assertEqual(target_place1['lat'], result_detail['lat'])
      # test 'long'
      self.assertEqual(target_place1['long'], result_detail['long'])

      # test 'users' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place1['users']), len(result_detail['users']))
      match_cnt = 0
      for target_user in target_place1['users']:
         for result_user in result_detail['users']:
            if target_user['uid'] == result_user['uid']:
               self.assertEqual(target_user['name'], result_user['name'])
               self.assertEqual(target_user['pic_url'], result_user['pic_url'])
               match_cnt += 1
      self.assertEqual(len(target_place1['users']), match_cnt)

      # test 'photo_urls' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place1['photo_urls']), len(result_detail['photo_urls']))
      match_cnt = 0
      for target_photo_url in target_place1['photo_urls']:
         for result_photo_url in result_detail['photo_urls']:
            if target_photo_url == result_photo_url:
               match_cnt += 1
      self.assertEqual(len(target_place1['photo_urls']), match_cnt)

      # test 'comments' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place1['comments']), len(result_detail['comments']))
      match_cnt = 0
      for target_comment in target_place1['comments']:
         for result_comment in result_detail['comments']:
            if target_comment['comment_id'] == result_comment['comment_id']:
               self.assertEqual(target_comment['uid'], result_comment['uid'])
               self.assertEqual(target_comment['comment_str'], result_comment['comment_str'])
               match_cnt += 1
      self.assertEqual(len(target_place1['comments']), match_cnt)

      
   def test_places_detail_2(self):
      # make sure the data in each field of place 2 is correct
      result_detail = self.place_detail2

      # test 'place_id'
      self.assertEqual(target_place2['place_id'], result_detail['place_id'])
      # test 'name'
      self.assertEqual(target_place2['name'], result_detail['name'])
      # test 'time'
      self.assertEqual(target_place2['time'], result_detail['time'])
      # test 'perm'
      self.assertEqual(target_place2['perm'], result_detail['perm'])
      # test 'cid'
      self.assertEqual(target_place2['cid'], result_detail['cid'])
      # test 'host_uid'
      self.assertEqual(target_place2['host_uid'], result_detail['host_uid'])
      # test 'lat'
      self.assertEqual(target_place2['lat'], result_detail['lat'])
      # test 'long'
      self.assertEqual(target_place2['long'], result_detail['long'])

      # test 'users' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place2['users']), len(result_detail['users']))
      match_cnt = 0
      for target_user in target_place2['users']:
         for result_user in result_detail['users']:
            if target_user['uid'] == result_user['uid']:
               self.assertEqual(target_user['name'], result_user['name'])
               self.assertEqual(target_user['pic_url'], result_user['pic_url'])
               match_cnt += 1
      self.assertEqual(len(target_place2['users']), match_cnt)

      # test 'photo_urls' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place2['photo_urls']), len(result_detail['photo_urls']))
      match_cnt = 0
      for target_photo_url in target_place2['photo_urls']:
         for result_photo_url in result_detail['photo_urls']:
            if target_photo_url == result_photo_url:
               match_cnt += 1
      self.assertEqual(len(target_place2['photo_urls']), match_cnt)

      # test 'comments' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_place2['comments']), len(result_detail['comments']))
      match_cnt = 0
      for target_comment in target_place2['comments']:
         for result_comment in result_detail['comments']:
            if target_comment['comment_id'] == result_comment['comment_id']:
               self.assertEqual(target_comment['uid'], result_comment['uid'])
               self.assertEqual(target_comment['comment_str'], result_comment['comment_str'])
               match_cnt += 1
      self.assertEqual(len(target_place2['comments']), match_cnt)


   def test_places_detail_5(self):
      # out of range, should return empty info
      self.assertEqual({}, self.place_detail5)
      
if __name__ == '__main__':
    unittest.main()
