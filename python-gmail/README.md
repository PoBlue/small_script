# Python Gmail

Send mail with Python

参考 [send Gmail using python](http://stackabuse.com/how-to-send-emails-with-gmail-using-python/) 最后一个思路，决定不使用 Gmail 发邮件。因为 Gmail 为了安全 stmp 管理比较严格，比较难用。

取而代之，使用其他专门的程序发邮件的供应商 [MailGun](https://www.mailgun.com/) (名字够 Cool!)。 具体使用参考[官网](https://www.mailgun.com/)，挺容易配置好的（10～20min）


## 使用

1. 新建文件 `data.py`, 复制粘贴下面的信息
2. 打开 [MailGun domains](https://app.mailgun.com/app/domains)，根据图片所示，填写下面内容
```
# api key
mail_gun_api = "填写 API"

# domain
mail_domain = "填写domain"

# 接收邮件的地址
to_mail = "xxxxx@gmail.com"

# 邮件的主题
subject = "任意内容"

# 邮件内容模板
message_template = "hello, world!"

# mail gun 提供的 api url
gun_base_url = "填写api base url"

# 不用改
gun_url = gun_base_url + "/messages"
```

<img width="1080" alt="示意图" src="https://user-images.githubusercontent.com/9304701/43195338-61b94c82-9037-11e8-885f-a9bec7a97154.png">


3. 终端上输入命令 `python utils.py`