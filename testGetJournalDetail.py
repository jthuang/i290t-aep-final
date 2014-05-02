#!/usr/bin/python

import unittest
from getJournalDetail import getJournalDetail

target_journals = [
      {
         'jid': 1,
         'name': u'A day in downtown SF',
         'desp': u'My first time being in San Francisco. Only spending a day in downtown SF and checked out some of the most famous tourist spots.',
         'time': 1402829440,
         'uid': 1,
         'perm': 0,
         'checkins': [
            {'host_uid': 1, 'cid': 1, 'place_id': 1, 'perm': 0, 'time': 1402828440,
             'photo_urls': [
                u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f2/99/pier-39.jpg',
                u'http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f0/f7/the-boys.jpg',
                u'http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg'
             ]
            },
            {'host_uid': 1, 'cid': 2, 'place_id': 2, 'perm': 0, 'time': 1402830120,
             'photo_urls': [u'http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg']
            }
         ]
      },
      {
         'jid': 2,
         'name': u'Things to do in Golden Gate Park',
         'desp': u"The Golden Gate Park is not just a big park. There are wonderful museums to check out! Don't miss them.",
         'time': 1402830440,
         'uid': 1,
         'perm': 0,
         'checkins': [
            {'host_uid': 1, 'cid': 3, 'place_id': 3, 'perm': 0, 'time': 1402838220,
             'photo_urls': [u'http://media-cdn.tripadvisor.com/media/photo-s/01/bf/63/01/ghirardelli.jpg']
            },
            {'host_uid': 1, 'cid': 4, 'place_id': 4, 'perm': 0, 'time': 1402846860,
             'photo_urls': [u'http://media-cdn.tripadvisor.com/media/daodao/photo-s/05/80/ee/59/caption.jpg']
            }
         ]
      }
]

class TestGetJournalDetail(unittest.TestCase):

   def setUp(self):
      self.jid1_info = getJournalDetail("1")
      self.jid2_info = getJournalDetail("2")
      self.jid10_info = getJournalDetail("10")

   def test_journal_info1(self):
      target_journal = target_journals[0]
      result_journal = self.jid1_info
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

      # test the detail field of the checkins in the journal, order matters
      # test the lenth of the result chekcins of journal1 should be equal to the target checkins
      self.assertEqual(len(target_journal['checkins']), len(result_journal['checkins']))
      i = 0
      for result_checkin in result_journal['checkins']:
         # test each field in checkin
         target_checkin = target_journal['checkins'][i]
         # test 'cid'
         self.assertEqual(target_checkin['cid'], result_checkin['cid'])
         # test 'time'
         self.assertEqual(target_checkin['time'], result_checkin['time'])
         # test 'place_id'
         self.assertEqual(target_checkin['place_id'], result_checkin['place_id'])
         # test 'host_uid'
         self.assertEqual(target_checkin['host_uid'], result_checkin['host_uid'])
         # test 'perm'
         self.assertEqual(target_checkin['perm'], result_checkin['perm'])

         # test photo_urls
         # test 'photo_urls' (list, order doesn't matter)
         # test length first
         self.assertEqual(len(target_checkin['photo_urls']), len(result_checkin['photo_urls']))
         match_cnt = 0
         for target_photo_url in target_checkin['photo_urls']:
            for result_photo_url in result_checkin['photo_urls']:
               if target_photo_url == result_photo_url:
                  match_cnt += 1
         self.assertEqual(len(target_checkin['photo_urls']), match_cnt)

         i += 1

   def test_journal_info2(self):
      target_journal = target_journals[1]
      result_journal = self.jid2_info
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

      # test the detail field of the checkins in the journal, order matters
      # test the lenth of the result chekcins of journal1 should be equal to the target checkins
      self.assertEqual(len(target_journal['checkins']), len(result_journal['checkins']))
      i = 0
      for result_checkin in result_journal['checkins']:
         # test each field in checkin
         target_checkin = target_journal['checkins'][i]
         # test 'cid'
         self.assertEqual(target_checkin['cid'], result_checkin['cid'])
         # test 'time'
         self.assertEqual(target_checkin['time'], result_checkin['time'])
         # test 'place_id'
         self.assertEqual(target_checkin['place_id'], result_checkin['place_id'])
         # test 'host_uid'
         self.assertEqual(target_checkin['host_uid'], result_checkin['host_uid'])
         # test 'perm'
         self.assertEqual(target_checkin['perm'], result_checkin['perm'])

         # test photo_urls
         # test 'photo_urls' (list, order doesn't matter)
         # test length first
         self.assertEqual(len(target_checkin['photo_urls']), len(result_checkin['photo_urls']))
         match_cnt = 0
         for target_photo_url in target_checkin['photo_urls']:
            for result_photo_url in result_checkin['photo_urls']:
               if target_photo_url == result_photo_url:
                  match_cnt += 1
         self.assertEqual(len(target_checkin['photo_urls']), match_cnt)

         i += 1


   def test_journal_info10(self):
      # out of range, should return empty info
      self.assertEqual({}, self.jid10_info)
      
if __name__ == '__main__':
    unittest.main()
