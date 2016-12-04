import json
import logging
import recipients
import datetime
import boto3 # Make sure you have installed locally
from jinja2 import Template # Install from requirements.txt

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# This must be a verified address in AWS SES
FROM_ADDRESS='staff@thewoofgarden.com'
REPLY_TO_ADDRESS='staff@thewoofgarden.com'


# In the AWS SES sandbox you can only send to/from verified emails
# Remember to do this before adding your emails here

EMPLOYEES = recipients.recipients['employees']
# Content stored in this order: [email, first_name, last_name]
CLIENTS = recipients.recipients['clients']
# Content stored in this order: [email, first_name, last_name, pet_name]

def get_template(template_file='./template.html'):
    # Load and return html template
    try:
        with open(template_file) as t_file:
            raw_template = t_file.read()
        template = Template(raw_template)
    except Exception as e:
        logger.info('failed to load template')
        raise e
    return template

def render_messages(title, message):
    datetime.date
    html_email = get_template().render(
                title = title, 
                salutation = salutation, 
                message = message
                )
    plain_text_email = 'Hello' + message

    return html_email, plain_text_email
    

def send_email_reminder(title, salutation, message, recipient):
    # Sends an email to
    try:
        ses = boto3.client('ses')
        response = ses.send_email(
            Source=FROM_ADDRESS,
            Destination={
                'ToAddresses': recipient,
                'CcAddresses': [],
                'BccAddresses': []
            },
            Message={
                'Subject': {
                    'Data': title,
                },
                'Body': {
                    'Text': {
                        'Data': plain_text_email
                    },
                    'Html': {
                        'Data': html_email
                    }
                }
            },
            ReplyToAddresses=[
                REPLY_TO_ADDRESS,
            ]
        )
    except Exception as e:
        logger.info("Failed to send message via SES")
        logger.info(e.message)
        raise e

def send_pickup_your_pet_reminder():




def send_daily_tasks_reminder():

DAILY_TASKS = {
    'Monday': '1. Clean the dog areas\n',
    'Tuesday': '1. Clean the cat areas\n',
    'Wednesday': '1. Feed the aligator\n',
    'Thursday': '1. Clean the dog areas\n',
    'Friday': '1. Clean the cat areas\n',
    'Saturday': '1. Relax! Play with the puppies! It\'s the weekend!',
    'Sunday': '1. Relax! Play with the puppies! It\'s the weekend!'
}

.format(TODAY, DAILY_TASKS[TODAY])


DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Gets an integer value from 0 to 6 for today (Monday - Sunday)
# Keep in mind this will run in GMT and you will need to adjust runtimes accordingly 
TODAY = DAYS[datetime.date.today().weekday()]






for client in clients:




###### FIGURE THIS SHIT OUT




def handler(event,context):
    event_trigger = event['resources'][0]
    print 'event triggered by ' + event_trigger
    if 'Morning' in event_trigger:
        # s3 get html template for morning
    elif 'Afternoon' in event_trigger:
        # s3 get afternoon
    elif 'Pickup' in event_trigger:
        # s3 get pickup
    else:
        return 'No template for this trigger!'


class Context:
    def __init__(self, **entries):
        self.__dict__.update(entries)

if __name__ == "__main__":
    event = {}
    context = Context(dict())
    send_finance_kpis(event, **context)