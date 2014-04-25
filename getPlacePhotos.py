#!/usr/bin/python

import sys
import sqlite3

GET_PLACE_PHOTO_URLS_EXPR = "SELECT photo_url  FROM photos WHERE (cid = ?);"

# input  : cid
# output : place_photos
def getPlacePhotos(cid):
	place_photos = []

	conn = sqlite3.connect('traceshare_test.db')
	c = conn.cursor()

	# get place photo_url
	for photo_url in c.execute(GET_PLACE_PHOTO_URLS_EXPR, (cid,)):
		place_photos.append(photo_url[0])

	conn.close()

	return place_photos


def printPlacePhotos(place_photos):
	print place_photos
	print "======================================================"
	for photo_url in place_photos:
		print photo_url

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "please enter the 'cid'."
	else:
		place_photos = getPlacePhotos(sys.argv[1])
		printPlacePhotos(place_photos)
