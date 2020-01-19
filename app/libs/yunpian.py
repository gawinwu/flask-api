import requests
import json


class SendSms:
    def __init__(self, sms, mobile):
        self.sms = sms
        self.mobile = mobile
        self.url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_single_sms(self):
        # 发送单条短信
        api_key = "801f341cf86b65142705e63058803bef"
        text = "【发现电商】您的验证码是{}。如非本人操作，请忽略本短信".format(self.sms)

        _res = requests.post(self.url, data={
            "apikey": api_key,
            "mobile": self.mobile,
            "text": text
        })
        re_json = json.loads(_res.text)
        return _res  # 测试用
        # return res_json


if __name__ == "__main__":
    res = SendSms("123456", "18824150722").send_single_sms()
    print(res)
    import json

    res_json = json.loads(res.text)
    code = res_json["code"]
    msg = res_json["msg"]
    if code == 0:
        print("发送成功")
    else:
        print("发送失败: {}".format(msg))
    print(res.text)
