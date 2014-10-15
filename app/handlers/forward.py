from lamson.routing import route, stateless
from config.settings import relay, forward_address, receive_addresses


@route("(address)@(host)", address=".+")
@stateless
def FORWARD(message, address=None, host=None):
    target = address.lower() + "@" + host.lower()
    if target in receive_addresses:
        relay.deliver(message, To=[forward_address])
    else:
        raise Exception("Not forwarding email: %s not an accepted email address" % target)

