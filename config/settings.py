# This file contains python variables that configure Lamson for email processing.
import logging

# You may add additional parameters such as `username' and `password' if your
# relay server requires authentication, `starttls' (boolean) or `ssl' (boolean)
# for secure connections.
relay_config = {'host': 'localhost',
                'port': 8825,
                'username': None,
                'password': None,
                'ssl': False,
                'starttls': False}

receiver_config = {'host': 'localhost', 'port': 8823}

handlers = ['app.handlers.forward']

router_defaults = {'host': '.+'}

template_config = {'dir': 'app', 'module': 'templates'}

# Address to which all accepted emails are forwarded
forward_address = 'replacethiswith@yourown.emailaddress'

# Only email to these addresses are accepted (use lower case)
receive_addresses = ['oneacceptable@email.address']

# the config/boot.py will turn these values into variables set in settings

# Load local settings
try:
    from local_settings import *
except ImportError:
    pass
