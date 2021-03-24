# -*- coding: utf-8 -*-

# app name
app_name = 'Miksu!'

# secret key
secret_key = ''

#hCaptcha settings:
hCaptcha_sitekey = ''
hCaptcha_secret = ''


# domain (used for api, avatar, etc)
domain = 'miksu.pw'

# mysql credentials
mysql = {
    'db': '',
    'host': '',
    'user': '',
    'password': '',
}

# path to gulag root (must have leading and following slash)
path_to_gulag = '/home/gunnest663/gulag/'

# enable debug (disable when in production to improve performance)
debug = False

# disallowed names (hardcoded banned usernames)
disallowed_names = {
    'cookiezi', 'rrtyui',
    'hvick225', 'qsc20010'
}

# disallowed passwords (hardcoded banned passwords)
disallowed_passwords = {
    'password', 'minilamp'
}

# enable registration
registration = True

# social links (used throughout gulag-web)
github = 'https://github.com/Yo-ru/gulag-web'
discord_server = 'https://discord.gg/eFeBudnX'
youtube = 'https://youtube.com/c/Gunnest663'
twitter = 'https://twitter.com/Sensokaku'
instagram = 'https://instagram.com/'
