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


Obviously, set the MX records on your nameservers to point to the server on
which you are running this.


License
-------


Copyright (c) 2014 Jaakko Luttinen

MIT License