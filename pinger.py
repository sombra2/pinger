import credentials # create a separate credentials.py file to store the token, chatID and host variables
import os
import requests
import time
import datetime

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

hostname = credentials.host

# function to send the message to telegram
def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()

telegram_bot_sendtext('📡 Monitoring of host *{}* started.\nTimestamp {}'.format(hostname, now))
while True:
  response = os.system('ping -c 1 ' + hostname)
  if response == 0:
    time.sleep(60)
    continue
  else:
    telegram_bot_sendtext(
      '🔴 *Host ' + hostname + ' is down!* Will check again in 10 minutes.\nTimestamp {}'.format(hostname, now))
    time.sleep(600)
    response = os.system('ping -c 1 ' + hostname)
    # TODO: the script should continue pinging even when the host is down but without sending any messages to telegram
    if response == 0:
      telegram_bot_sendtext(
        '🟢 *Host {} is back up again!* Connection re-established\nTimestamp {}'.format(hostname, now))
      continue
    else:
      telegram_bot_sendtext(
        '🔴 *REMINDER - Host {} is still down!* Please check connection. This script will now end - please make sure you reboot it once connection is re-established\n Timestamp {}'.format(hostname, now))
      break

