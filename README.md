Mail forwarder using Lamson
===========================


This is a simple lightweight mail server which receives emails to a set of
addresses and forwards them to a given address.


One possible use case: You have a domain (or domains) and you want to have email
addresses for those domains (for instance, webmaster@mydomain1.com and
firstname.lastname@mydomain2.com).  Instead of setting up complex mail servers
on your domains, you just want to forward those emails to your existing email
address.  If you want to send from these custom addresses, use your mail
application to write your custom address in the "from" field.


Installation
------------


Install Lamson. Create a file `config/local_settings.py` and set the following:

 * `relay_config`

 * `receiver_config`

 * `forward_address`

 * `receive_addresses`


Deploying
---------


Obviously, set the MX records on your nameservers to point to the server on
which you are running this.

For security, create a new user:

```
mailserver
su mailserver
```

In its home directory, clone the project:

```
cd /home/mailserver
git clone https://github.com/jluttine/mail-forwarder.git
```

Create a Python virtual environment:

```
cd mail-forwarder
virtualenv --python=/usr/bin/python2 ENV
source ENV/bin/activate
```

Install Lamson:

```
pip install lamson
```

Create a startup script `start` with the following content:

```
#!/bin/bash
cd /home/mailserver/mail-forwarder
source ENV/bin/activate
lamson stop
lamson start -FORCE True -uid 1001 -gid 1001
```

Note that the `uid` and `gid` values should be the user and group ID of the user
account `mailserver`.  You can check those values using:

```
id mailserver
```

Make the startup script executable:

```
chmod og+x start
```

Create a few required directories:

```
mkdir logs
mkdir run
```

The startup script must be executed as a root (if you are listening to port 25):

```
sudo ./start
```

You could add the script to root's crontab to start the server after every boot.


License
-------


Copyright (c) 2014 Jaakko Luttinen

MIT License