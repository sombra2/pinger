# Uptime monitor
Quick and simple script to check if a host is up and otherwise send an alert to telegram.

___
## Creation of a ```credentials.py``` file

You will have to create a separate `credentials.py` file once you clone the repository. In this file you must include the following variables:

  `bot_token` - this is the ID of the bot you plan on using as alert, full information on Telegram Bots and API can be found [here](https://core.telegram.org/bots)
  
  `bot_chatID` - this is the ID of the group chat you plan the bot to alert you on, full information on Telegram Bots and API can be found [here](https://core.telegram.org/bots)
  
  `host` - this is the host on which you plan to ping on

The script will call these 3 variables
___

## How does it work

The script will ping the host set in the ``credentials.py`` file every 60 seconds (or whatever you set it to), as long as it's up. The moment the ping doesn't come back it will send an alert message such as this:

![](https://i.imgur.com/5dhLipK.png)

After 5 minutes (or whatever you set it to) it will ping again. If the host is back up you will receive a message such as this:

![](https://i.imgur.com/DIrC6oG.png)

Should the host doesn't come back up in the waiting 5 minutes you will receive another message saying that the host is still down and the script will stop (to prevent continous pinging and sending messages)
___
## Deployment
So far, and due to my limited knowledge, I am deploying this script through the ``screen`` command in my monitoring server and then dettaching it to leave it running. I don't see the need for a cron task but if you have a better idea please do let me know.
___
### Things that need doing

Since I am not an Python expert, if anyone knows a way of having the script not stopping while the host is down but also not sending messages and waiting dormant until the host is up, I'll be happy to hear it. Please feel free to let me know or use the code as you wish. This is only a tiny learning project for me nonetheless.