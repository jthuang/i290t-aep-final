import os
import unittest
import flask
from flask import request
from getPlaceDetail import getPlaceDetail

app = flask.Flask(__name__)

@app.route('/placedetail', methods=["GET"])
def get_place_detal():
   
   cid = request.args.get('cid', "")
   place_info = getPlaceDetail(cid)

   resp = flask.make_response(flask.render_template(
            'placedetail.html',
            place_info=place_info))
   return resp

class FlaskrTestCase(unittest.TestCase):
   
   def setUp(self):
      self.client = app.test_client()
      self.place1_resp = self.client.get('/placedetail?cid=1')
      self.place2_resp = self.client.get('/placedetail?cid=2')
      self.place10_resp = self.client.get('/placedetail?cid=10')

   def test_place1_info(self):
      response_html = self.place1_resp.data
      # place 1 should have 3 photos
      self.assertIn('http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f2/99/pier-39.jpg', response_html)
      self.assertIn('http://media-cdn.tripadvisor.com/media/photo-s/05/a6/f0/f7/the-boys.jpg', response_html)
      self.assertIn('http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg', response_html)

      # place 1 should have 3 travel parties
      self.assertIn('<span class="user-profile-name">Wendy</span>', response_html)
      self.assertIn('<span class="user-profile-name">Chan</span>', response_html)
      self.assertIn('<span class="user-profile-name">JT</span>', response_html)

      # place 1 shoudl have 3 comments
      self.assertIn('<p>Enjoyed hanging out with friends here. It&#39;s a lively place with nice view of the bay and so many restaurants to choose from. Pier 39 is worth a visit.</p>', response_html)
      self.assertIn('<p>The animals are so cute! They were pushing each other. One of them looked like Chan! Haha</p>', response_html)
      self.assertIn('<p>My favorites were the piano stairs and the Mirror Maze upstairs.</p>', response_html)


   def test_place2_info(self):
      response_html = self.place2_resp.data
      # place 2 should have 1 photo
      self.assertIn('<img class="detail-large-img" src="http://media-cdn.tripadvisor.com/media/photo-s/05/8d/d5/8b/fisherman-s-wharf.jpg"/>', response_html)

      # place 2 should have 1 travel party
      self.assertIn('<span class="user-profile-name">Wendy</span>', response_html)

      # place 2 should have no comments
      self.assertIn('''<div class="place-comments">
          <ul class="table-view">
            
          </ul>''', response_html)
   
   def test_place10_trace(self):
      # out of ragne, should return error
      response_html = self.place10_resp.data
      self.assertIn('unable to complete your request', response_html)



      

if __name__ == '__main__':
    unittest.main()
