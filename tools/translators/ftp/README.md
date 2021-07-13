# FTP Translator

This is a simple example of how an agent can send FTP payloads to a proxy server which will translate the payload into
a protocol that Operator accepts, in this case HTTP.

## Get started

> The example agent will run shell commands only, through the 'sh' executor

1. Start `server.py` on a server you control, which is reachable over port 21 from the computers you want to test.  
2. Run `agent.py` on a compromised host. You should get a beacon inside Operator.
3. Deploy an adversary against your agent.

> If running server.py on a different computer than Operator, you will need to pass in the -O parameter with the IP of your Operator instance.
