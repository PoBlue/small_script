#!/usr/bin/env python
#-*- coding: utf-8 -*-
from data import user_account, password, to_mail, stmp_code
from smtplib import SMTP_SSL
from email.mime.text import MIMEText


def send_qq_mail(_user, _stmp_code, _to_mail, _msg):
    #Auth and Login
    smtp_server = 'smtp.qq.com'
    smtp_auth_username = _user   # QQ号，非邮箱
    smtp_auth_password = _stmp_code       #! 换成自己的SMTP授权码，而不是QQ登录密码

    smtp = SMTP_SSL(smtp_server)
    smtp.login(smtp_auth_username, smtp_auth_password)

    smtp.set_debuglevel(1) 
    # Send mail
    from_addr = '{qq}@qq.com'.format(qq=_user)      #实际用来发送的邮箱
    smtp.sendmail(from_addr, _to_mail, _msg)
    smtp.quit()


def create_msg(_msg, _subject, _user):
    msg = '''\
From: {user}@qq.com
Subject: {subject}

{content}
    '''.format(user=_user,
               subject=_subject,
               content=_msg)
    return msg


def main():
    content = "test"
    subject = "fix 2"
    msg = create_msg(content, subject, user_account)
    send_qq_mail(user_account, stmp_code, to_mail, msg)
    pass

if __name__ == '__main__':
    main()
