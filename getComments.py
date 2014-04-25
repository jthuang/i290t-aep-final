#!/usr/bin/python

import sys
import sqlite3

GET_COMMENTS_EXPR = "SELECT comment_id, uid, comment_str FROM comments WHERE (cid = ?);"

# input  : cid
# output : comments[]
def getComments(cid):
	comments = []

	conn = sqlite3.connect('traceshare_test.db')
	c = conn.cursor()

	# get comments
	for (comment_id, uid, comment_str) in c.execute(GET_COMMENTS_EXPR, (cid,)):
		comment = {}
		comment['comment_id'] = comment_id
		comment['uid'] = uid
		comment['comment_str'] = comment_str
		comments.append(comment)

	conn.close()

	return comments


def printComments(comments):
	print comments
	print "======================================================"
	for comment in comments:
		print comment['comment_id'], comment['uid'], comment['comment_str']

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "please enter the 'cid'."
	else:
		comments = getComments(sys.argv[1])
		printComments(comments)
