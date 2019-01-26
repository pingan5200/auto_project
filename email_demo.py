#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# email_demo.py
# 发送邮件示例
# author: De8uG

# 套路：先建立连接，生成邮件对象，然后在邮件对象内添加内容，关闭连接
# 发件人，邮件服务器在MailMaster类的初始化函数内
# 只需输入收件人邮箱
# 发件内容和附件可以编辑
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def get_password():
    """第三方客户端授权码"""
    return "rliwvskvthhzbhab"


class MailMaster:
    """邮箱大师"""
    def __init__(self, password, smtp_server='smtp.qq.com', email_addr='pingan5200@foxmail.com'):
        """初始化安全加密对象，邮件服务器，发件人，登录第三方客户端，收件人"""
        self.smtp = SMTP_SSL(smtp_server)
        self.smtp.set_debuglevel(1)
        self.smtp.ehlo(smtp_server)
        self.smtp.login(email_addr, password)
        self.email_from = email_addr
        self.email_to = []

    def add_email_to_list(self, addr):
        """添加收件人"""
        self.email_to.append(addr)

    def notice(self, username, text, subject='注册成功'):  # 发送邮件入口
        """发送通知邮件入口"""
        self.send_email_all(subject, f'{username}\n' + text)

    def send_email_all(self, subject, body, mailtype='plain', attachment=None):   # 默认不添加附件，添加附件的话notic添加参数attachment
        """发送邮件通用接口
        subject: 邮件标题
        body: 邮件内容
        mailtype： 邮件类型，默认是文本，发html时候指定为html
        attachment： 附件
        """
        # 生成邮件对象
        msg = MIMEMultipart()                               # 构造一个MIMEMultipart对象代表邮件本身

        msg["Subject"] = Header(subject, "utf-8")
        msg["from"] = self.email_from
        
        # 判断是否有收件人
        try:  
            if len(self.email_to) > 0:
                to_mail = self.email_to  
                msg['To'] = ','.join(to_mail)
            else:
                print('还没添加发送人呢，使用add_email_to_list进行填加')
        # 添加'html'文本内容
            msg.attach(MIMEText(body, mailtype, 'utf-8'))   # 追加文本内容，mailtype代表邮件类型，纯文本或html等

        # 是否添加附件，如果不添加附件，后面直接发送纯文本
            if attachment:
                # 二进制方式模式文件  
                with open(attachment, 'rb') as f:  
                    # MIMEBase表示附件的对象  
                    mime = MIMEBase('text', 'txt', filename=attachment)  
                    # filename是显示附件名字  
                    mime.add_header('Content-Disposition', 'attachment', filename=attachment)  
                    # 获取附件内容  
                    mime.set_payload(f.read())  
                    encoders.encode_base64(mime)  
                    # 作为附件添加到邮件  
                    msg.attach(mime)                      # 追加附件
        # 发送邮件
            self.smtp.sendmail(self.email_from, to_mail, msg.as_string())
            self.smtp.quit()
            print('send success')
        except smtplib.SMTPException as e:  
            print(e)  


def main():
    html = """
    <h1>第8哥的邮件啊</h1>
    <h2>须有html格式, 比如写个表格</h2>
    <table border="1">
        <tr>
            <th>姓名</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>第8哥</td>
            <td>北京</td>
        </tr>
    </table>
    """

    mail = MailMaster(password=get_password())
    add_des = True
    # 手动添加收件人
    while add_des:
        destination = input('请输入收件人:')   # 输入pingan5200@qq.com
        mail.add_email_to_list(destination)    # 添加收件人
        add_des = input('是否继续添加 Y/N:') == 'Y'
    # 1.发送纯文本内容和附件邮件
    # mail.send_email_all('测试主题', '测试附件all', attachment=r'D:\Users\T00006843\日常值班表.txt')
    
    # 2.发送html内容邮件
    mail.send_email_all('html邮件主题', html, 'html')
    
    # 3.发送通知邮件
    # mail.notice('de8ug', '欢迎来到http://edu.51cto.com/学习，祝学习愉快')

if __name__ == '__main__':
    main()