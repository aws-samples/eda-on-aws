# Store the full message to be accessed from where we need information of it
full_message: dict = {
    'user': 'JeffBezos',
    'name': 'Jeff',
    'last_name': 'Bezos',
    'age': 55,
    'website_preferences': 'classic'
}

# Extract only the information the website configuration needs
website_configuration: dict = {
    key: full_message[key] for key in full_message.keys()
    & {'user', 'website_preferences'}
}

# Extract only the information the profile needs
profile_info: dict = {
    key: full_message[key] for key in full_message.keys()
    & {'name', 'last_name', 'age'}
}

# Watch how we can get the full message when we need it
print(f'Full message: {full_message}')

# Watch we can get only the website configuration when we need it
print(f'Website configuration: {website_configuration}')

# Watch we can get only the profile information when we need it
print(f'Profile information: {profile_info}')
