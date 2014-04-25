#!/usr/bin/python

import unittest
from getComments import getComments

target_comments1 = [
      {'comment_str': u"Enjoyed hanging out with friends here. It's a lively place with nice view of the bay and so many restaurants to choose from. Pier 39 is worth a visit.", 'comment_id': 1, 'uid': 1},
      {'comment_str': u'The animals are so cute! They were pushing each other. One of them looked like Chan! Haha', 'comment_id': 2, 'uid': 1},
      {'comment_str': u'My favorites were the piano stairs and the Mirror Maze upstairs.', 'comment_id': 3, 'uid': 1}
]

class TestGetComments(unittest.TestCase):

   def setUp(self):
      self.comments1 = getComments("1")
      self.comments2 = getComments("2")
      self.comments5 = getComments("5")     # out of range

   def test_commets_1(self):
      # make sure the comments in checkin #1 are all correct
      result_comments = self.comments1

      # test 'comments' (list, order doesn't matter)
      # test length first
      self.assertEqual(len(target_comments1), len(result_comments))
      match_cnt = 0
      for target_comment in target_comments1:
         for result_comment in result_comments:
            if target_comment['comment_id'] == result_comment['comment_id']:
               self.assertEqual(target_comment['uid'], result_comment['uid'])
               self.assertEqual(target_comment['comment_str'], result_comment['comment_str'])
               match_cnt += 1
      self.assertEqual(len(target_comments1), match_cnt)

   def test_commets_2(self):
      # checkin #2 has no comments, return empty list
      self.assertEqual([], self.comments2)
      
   def test_commets_5(self):
      # out of range, should return empty list
      self.assertEqual([], self.comments5)
      
if __name__ == '__main__':
    unittest.main()
