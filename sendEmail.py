import yagmail
import yaml

stream = open("config.yaml", 'r')
config = yaml.load(stream, Loader=yaml.FullLoader)

def sendEmail(receiver, filename):
    body = "A random quote, carved on a random art piece."

    f = open(config["product"]["secret"])
    password = f.read()

    yag = yagmail.SMTP("reproductionofanything@gmail.com", password=password)
    yag.send(
        to=receiver,
        subject="Reproduction of Anything : Your Daily Quote",
        contents=body,
        attachments=filename,
        )