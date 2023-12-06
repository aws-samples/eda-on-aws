# Simulate the credentials store
credentials_store: list = []

# A function to store new credentials that can lack password
def store_credentials(user: str, password: str = None):
    tmp_credentials: dict = {'user': user, 'password': password}

    credentials_store.append(tmp_credentials)

    # If the password is missing, return a reference to update it later
    if not password:
        print(f'Warning: Please update the password for user \'{user}\' as soon as you can\n')

        return tmp_credentials
    else:
        print(f'Info: Credentials for user \'{user}\' saved\n')

        return None

# Create complete credentials, we don't get a reference to update the password
complete_credentials = store_credentials('user1', 'password1')

# Watch the reference and the credentials store
print(f'Credentials reference: {complete_credentials}\nStore: {credentials_store}\n')

# Create incomplete credentials, we get a reference to update the password
incomplete_credentials = store_credentials('user2')

# Watch the reference and the credentials store
print(f'Credentials reference: {incomplete_credentials}\nStore: {credentials_store}\n')

# Update the password
incomplete_credentials['password'] = 'password2'

# Watch the reference and the credentials store
print(f'Credentials reference: {incomplete_credentials}\nStore: {credentials_store}\n')
