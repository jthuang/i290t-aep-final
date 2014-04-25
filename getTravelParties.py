#!/usr/bin/python

import sys
import sqlite3

GET_TRAVEL_PARTIES_EXPR = "SELECT uid FROM travel_parties WHERE (cid = ?);"
GET_USER_EXPR = "SELECT name, pic_url FROM users WHERE (uid = ?);"

# input  : cid
# output : travel_parties[]
def getTravelParties(cid):
	travel_parties = []

	conn = sqlite3.connect('traceshare_test.db')
	c = conn.cursor()

	# get uids of travel parties
	uids = []
	for u in c.execute(GET_TRAVEL_PARTIES_EXPR, cid):
		uids.append(u[0])

	# get name and pic_url of each user
	for u in uids:
		user = {}
		user['uid'] = u
		c.execute(GET_USER_EXPR, str(u))
		(user['name'], user['pic_url']) = c.fetchone()
		travel_parties.append(user)

	conn.close()

	return travel_parties


def printTravelParties(travel_parties):
	print travel_parties
	print "======================================================"
	for user in travel_parties:
		print user['uid'], user['name'], user['pic_url']

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "please enter the 'cid'."
	else:
		travel_parties = getTravelParties(sys.argv[1])
		printTravelParties(travel_parties)
