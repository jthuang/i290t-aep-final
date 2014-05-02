#!/usr/bin/python

import unittest
from getMyJournals import getMyJournals

target_journals = [
      {
         'jid': 2,
         'name': u'Things to do in Golden Gate Park',
         'desp': u"The Golden Gate Park is not just a big park. There are wonderful museums to check out! Don't miss them.",
         'time': 1402830440,
         'uid': 1,
         'perm': 0,
         'checkins': [
            {'lat': 37.808673, 'place_id': 3, 'long': -122.409821, 'cid': 3}, 
            {'lat': 37.808673, 'place_id': 4, 'long': -122.409821, 'cid': 4}
         ]
      },
      {
         'jid': 1,
         'name': u'A day in downtown SF',
         'desp': u'My first time being in San Francisco. Only spending a day in downtown SF and checked out some of the most famous tourist spots.',
         'time': 1402829440,
         'uid': 1,
         'perm': 0,
         'checkins': [
            {'lat': 37.808673, 'place_id': 1, 'long': -122.409821, 'cid': 1},
            {'lat': 37.808673, 'place_id': 2, 'long': -122.409821, 'cid': 2}
         ],
      }
]

class TestGetMyJournals(unittest.TestCase):

   def setUp(self):
      self.user1_journals = getMyJournals("1")
      self.user2_journals = getMyJournals("2")
      self.user10_journals = getMyJournals("10")

   def test_user1_journals(self):
      # test the lenth of the result list of user1 should be equal to the target list
      self.assertEqual(len(target_journals), len(self.user1_journals))

      # test the journals in user1's journal list, order matters
      i = 0
      for result_journal in self.user1_journals:
         # test each field in the journal
         target_journal = target_journals[i]
         # test 'jid'
         self.assertEqual(target_journal['jid'], result_journal['jid'])
         # test 'name'
         self.assertEqual(target_journal['name'], result_journal['name'])
         # test 'desp'
         self.assertEqual(target_journal['desp'], result_journal['desp'])
         # test 'time'
         self.assertEqual(target_journal['time'], result_journal['time'])
         # test 'uid'
         self.assertEqual(target_journal['uid'], result_journal['uid'])
         # test 'perm'
         self.assertEqual(target_journal['perm'], result_journal['perm'])
         
         # test 'checkins', order matters
         # test the lenth of the result checkins, should be equal to the target checkins
         self.assertEqual(len(target_journal['checkins']), len(result_journal['checkins']))
         j = 0
         for result_checkin in result_journal['checkins']:
            target_checkin = target_journal['checkins'][j]
            # test cid
            self.assertEqual(target_checkin['cid'], result_checkin['cid'])
            # test place_id
            self.assertEqual(target_checkin['place_id'], result_checkin['place_id'])
            # test lat
            self.assertEqual(target_checkin['lat'], result_checkin['lat'])
            # test long
            self.assertEqual(target_checkin['long'], result_checkin['long'])
            j+= 1

         i += 1


   def test_user2_journals(self):
      # test the user2's journal list should be empty
      self.assertEqual([], self.user2_journals)

   def test_user10_journals(self):
      # there is no user 10, the journal list should be empty
      self.assertEqual([], self.user10_journals)
      
if __name__ == '__main__':
    unittest.main()
