import os
import unittest
import flask
from flask import request
from getMyPlaces import getMyPlaces
from getMyJournals import getMyJournals

app = flask.Flask(__name__)

@app.route('/mytrace', methods=["GET"])
def get_my_trace():
   uid = request.args.get('uid', "")
   places = getMyPlaces(uid)
   journals = getMyJournals(uid)

   resp = flask.make_response(flask.render_template(
            'mytrace.html',
            places=places,
            journals=journals))
   return resp

class FlaskrTestCase(unittest.TestCase):
   
   def setUp(self):
      self.client = app.test_client()
      self.user1_resp = self.client.get('/mytrace?uid=1')
      self.user2_resp = self.client.get('/mytrace?uid=2')
      self.user10_resp = self.client.get('/mytrace?uid=10')

   def test_user1_trace(self):
      response_html = self.user1_resp.data
      # user 1 should have 4 places
      self.assertIn('href="placedetail?cid=4"', response_html)
      self.assertIn('Golden Gate Bridge', response_html)
      self.assertIn('href="placedetail?cid=3"', response_html)
      self.assertIn('Ghirardelli Square', response_html)
      self.assertIn('href="placedetail?cid=2"', response_html)
      self.assertIn('Fishermen&#39;s Wharf', response_html)
      self.assertIn('href="placedetail?cid=1"', response_html)
      self.assertIn('Pier 39', response_html)
      # user 1 should have 2 journals
      self.assertIn('href="journaldetail?jid=2"', response_html)
      self.assertIn('Things to do in Golden Gate Park', response_html)
      self.assertIn('href="journaldetail?jid=1"', response_html)
      self.assertIn('A day in downtown SF', response_html)
      
   def test_user2_trace(self):
      response_html = self.user2_resp.data
      # user 2 should have empty place list
      self.assertIn('Empty place list', response_html)
      # user 2 should have empty journal list
      self.assertIn('Empty journal list', response_html)

   def test_user10_trace(self):
      # out of ragne, should return error
      response_html = self.user10_resp.data
      self.assertIn('unable to complete your request', response_html)


if __name__ == '__main__':
    unittest.main()
