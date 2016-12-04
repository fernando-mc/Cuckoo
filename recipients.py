# Simple list of email addresses and basic info to merge into templates
# 
# In a more complete application we might loaded this in from a 
# database service such as DynamoDB
# 
# While in the AWS Email Sandbox you must verify emails or domains
# that you are sending emails to and from

recipients = {
    'clients' :
        [
            ['pluralsight.fernando@gmail.com', 'Fernando', 'Medina Corey', 'Riley'],
            ['zoe.on.the.firefly@outlook.com', 'Zoë', 'Washburne', 'Firefly II']
            # Add more contact info arrays here. Don't forget to add a comma!   ^
        ],
    'employees':
        [
            ['springfield.homer@yahoo.com', 'Homer', 'Simpson']
            # Add more contact info arrays here. Don't forget to add a comma!
        ]
}

