# GRPC Translator

This is a simple example of how an agent can send gRPC beacons to a proxy server which will translate the payload into
a protocol that Operator accepts, in this case HTTP.

## Get started

1. Start `server.py` on a server you control, which is reachable over port 50051 from the computers you want to test.  
2. Run the [Pneuma](https://github.com/preludeorg/pneuma) agent with the gRPC contact on a compromised host. You should get a beacon inside Operator.
3. Deploy an adversary against your agent.

> If running server.py on a different computer than Operator, you will need to pass in the -O parameter with the IP of your Operator instance.
