# -*- coding: utf-8 -*-
# try something like



def mainlist():
		return dict(complaints=db((db.complaints.id>0) & (db.users.id==db.complaints.user_id)).select())

def resolvedlist():
    return dict(unresolved=db(db.complaints.complaint_status=='0').select(db.complaints.id,db.complaints.user_id,db.complaints.username,db.complaints.title,db.complaints.description,db.complaints.complaint_type,db.complaints.concerned_user,db.complaints.complaint_status),comments=db(db.complaints.complaint_status=='0').select(db.complaints.comments),comment_user=db(db.complaints.complaint_status=='0').select(db.complaints.comment_user),upvote_users=db(db.complaints.complaint_status=='0').select(db.complaints.upvote_users),downvote_users=db(db.complaints.complaint_status=='0').select(db.complaints.downvote_users))


def unresolvedlist():
    return dict(unresolved=db(db.complaints.complaint_status=='1').select(db.complaints.id,db.complaints.user_id,db.complaints.username,db.complaints.title,db.complaints.description,db.complaints.complaint_type,db.complaints.concerned_user,db.complaints.complaint_status),comments=db(db.complaints.complaint_status=='1').select(db.complaints.comments),comment_user=db(db.complaints.complaint_status=='1').select(db.complaints.comment_user),upvote_users=db(db.complaints.complaint_status=='1').select(db.complaints.upvote_users),downvote_users=db(db.complaints.complaint_status=='1').select(db.complaints.downvote_users))


def complaint():
    x=request.args[0]
    if (db.complaints.id==x):
        u=db.complaints.user_id
        v=db.complaints.concerned_user
        return dict(complaints=db((db.complaints.id==x) & (db.users.id==u) & (db.users.id==v)).select())
    else:
        return 0


def upvotes():
    return "chill"

def downvotes():
    return "chill"

def new():
    import cgi
    x = request.vars
    return dict(x)

def post_comment():
    import cgi
    x = request.vars
    return dict(x)
