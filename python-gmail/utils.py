import requests
import data

# Try running this locally.
# You can see a record of this email in your logs: https://app.mailgun.com/app/logs
# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10,000 emails/month for free.
def send_simple_message(subject, msg, domain, to_mail, url, api):
    return requests.post(
        url,
        auth=("api", api),
        data={"from": domain,
              "to": to_mail,
              "subject": subject,
              "text": msg})

def main():
    """
    main function for testing to send mail
    """
    print("sending")
    responce = send_simple_message(data.subject, data.message_template
                            , data.mail_domain, data.to_mail
                            ,data.gun_url, data.mail_gun_api)

    print(responce)
    print("send sucessfully")

if __name__ == '__main__':
    main()
