from lamson.routing import route, stateless
from config.settings import relay, forward_mapping


@route("(address)@(host)", address=".+")
@stateless
def FORWARD(message, address=None, host=None):
    target = address.lower() + "@" + host.lower()
    to = []
    for i in range(len(forward_mapping)):
        alias = forward_mapping[i][0].lower()
        real = forward_mapping[i][1]
        if target == alias:
            to.append(real)
    if len(to) > 0:
        relay.deliver(message, To=to)
    else:
        raise Exception("Not forwarding email: %s not an accepted email address" % target)

