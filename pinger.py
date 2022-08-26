import credentials # create a separate credentials.py file to store the token, chatID and host variables
import os
import requests
import time

hostname = credentials.host

# function to send the message to telegram
def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()


while True:
  response = os.system('ping -c 1 ' + hostname)
  if response == 0:
    time.sleep(60)
    continue
  else:
    telegram_bot_sendtext(
      '🔴 *Host ' + hostname + ' is down!* Will check again in 5 minutes.')
    time.sleep(300)
    response = os.system('ping -c 1 ' + hostname)
    # TODO: the script should continue pinging even when the host is down but without sending any messages to telegram
    if response == 0:
      telegram_bot_sendtext(
        '🟢 *Host ' + hostname + ' is back up again!* Connection re-established')
      continue
    else:
      telegram_bot_sendtext(
        '🔴 *REMINDER - Host ' + hostname + ' is still down!* Please check connection. This script will now end - please make sure you reboot it once connection is re-established')
      break

