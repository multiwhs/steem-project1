# coding:utf-8
# created by   https://steemit.com/@tradingideas   2018/1/14
#
from steem import Steem
from steem.blog import Blog

import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# 글을 받아볼 작가 등록
TARGET_USERS = ['tradingideas', 'tmkor' ]

fromEmail = '보내는 사람의 메일'
fromEmailPW = 'gmail 암호'
toEmail  = '받을 분의 메일'

steemitURL = 'https://steemit.com'
maxNumberOfPostsToCheck = 10

def sendEmail(emailSubject, emailContents, fromEmail, fromEmailPW, toEmail):
    msg = MIMEText(contents, _charset='euc-kr')
    msg['subject']= subject
    msg['from']=fromEmail
    msg['To']=toEmail

    server = smtplib.SMTP('SMTP.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromEmail,fromEmailPW)

    sendOK = 1
    try:
        server.sendmail(fromEmail,toEmail,msg.as_string())
    except:
        print("메일 보내기 실패 ")
        sendOK = 0

    server.quit()
    return sendOK

def getNewPosts(s, users, numLimitPost) :
    summary = ''
    try:
      for user in users:
        summary += "< User:  %s >\n"  % user
        summary += "------------------\n"

        blog = s.get_blog(user, -1, numLimitPost)  # 최신 글(-1) 부터 numLimitPost개만

        for bg in blog:
          p = bg["comment"]

          p_date = p['created']  # 날짜T시간 으로 구성
          createdDate = p_date.split('T')  # T 로 구분하여 list 만듬

          today = datetime.today().date()   # 오늘 날짜 구하기
          if (createdDate[0] == str(today)) :
            json_meta = p['json_metadata']
            summary += "%s  " % p['title']  # 글의 주제

            # 글의 URL 만듬
            summary += steemitURL + '/' + p['parent_permlink'] + '/@' + p['author'] + '/' + p['permlink']

            summary += " Votes: %s" % p['net_votes']  # vote한 사람 수
            summary +=  "\n"   # 새로운 라인

        summary +=  "\n"
    except:
        print ('Something went wrong in getNewPosts...')

    return summary

# variables and constants
ACCOUNT_NAME = 'tradingideas'
nodes = [ 'https://api.steemit.com', 'https://node.steem.ws']

stm = Steem(nodes)

subject = '[Steemit] Daily post summary: ' + datetime.today().strftime('%Y-%m-%d')

# 등록한 사용자의 오늘자 글 가져오기
contents = getNewPosts(stm, TARGET_USERS, maxNumberOfPostsToCheck)

# 등록된 이메일로 보내기
ret = sendEmail(subject, contents, fromEmail, fromEmailPW, toEmail)