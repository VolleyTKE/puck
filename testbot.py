from slackclient import SlackClient
from sys import argv

#using arg to pass in slack token
script,SLACK_BOT_TOKEN = argv

connection to slack API
sc = SlackClient(SLACK_BOT_TOKEN)
sc.rtm_connect()

#dummy data, need to add csv file handling
tickets=['38386','39338']

#bread and butter for puck sending updates
for ticket in tickets:
    sc.rtm_send_message("D8D8TCX3P",
     "https://technologypartners.zendesk.com/agent/tickets/" + ticket + " \n" + "Please review this ticket.")


#todo
#1, get csv file to puck
#2, read in csv
#3, parse csv to find tickets older than 2 days
#4, grab ticket numbers from the parsed csv
#5, handle getting puck to send to appropriate user
