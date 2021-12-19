![alt text](images/home.png)

[![Release](https://img.shields.io/badge/dynamic/json?color=blue&label=Release&prefix=v&query=tag_name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpreludeorg%2Foperator-support%2Freleases%2Flatest)](https://github.com/preludeorg/operator-support/releases)
# Operator

### This repository is the spot to report bugs or submit feature requests.

Operator is an autonomous red team C2 platform, built by [Prelude](https://prelude.org). It is designed for red, purple and blue teamers to conduct realistic threat assessments. Using the desktop application, you can deploy agents on remote computers and launch custom adversary profiles against them to identify the holes that antivirus programs & vulnerability scanners are not designed to locate.

> Watch our quick [introduction video](https://www.youtube.com/watch?v=Hz8K-jdqpBY)

You can download the latest copy of the application [here](https://www.prelude.org/download/current), for either MacOS, Windows or Linux.

> Did you know that the team at Prelude runs free red team training programs as part of our open-source outreach? We teach IT/InfoSec/DevOps/defenders/software engineers how to red team, so they can apply practical techniques to their day jobs. Check out the [Pink Badge](https://www.prelude.org/training/pinkbadge) for more details.

## Community

When you start Operator, your app loads in our [community](https://github.com/preludeorg/community) resources in order to populate your environment with hundreds of open-source TTPs, payloads, agents, tools, training modules and more. We encourage contributions, so if you'd like to add TTPs for other Operator members, publish your own agents or come up with a new training flag for any of the programs - submit a pull request!

## Resources 

The Prelude development & security teams run several supporting resources for the community:

- A [Discord server](https://discord.gg/NWURE99JzE) to interact with the team.
- A [YouTube video library](https://www.youtube.com/channel/UCZyx-PDZ_k7Vuzyqr4-qK9A) containing tutorials and use-cases.
- A [blog](https://feed.prelude.org), where we post on general security and specific Operator topics.
- Details about our [weekly TTP releases](https://chains.prelude.org).

## Quick start

Ready to kick the tires with Operator? Operator contains a built-in capture the flag training program to teach you all the bells & whistles but the guide below will walk you through the basics.

### Installation

> Operator is a multi-platform compiled Electron/NodeJS app.

1. Head to https://prelude.org and download a copy of Operator for your operating system.
2. Double-click the download to install Operator the same as any other desktop app.
3. Open Operator. You'll be created with the main dashboard where you'll deploy adversaries and watch the results stream in. 

### Terminology detour

- Agents are the Remote Access Trojans (RATs) which ship with Operator. Prelude supports several agents, written in several different languages, and there are additional open-source variants online. You can also write your own.
- ThirdEye is a NodeJS agent that is built into Operator itself. Every time you open the platform you'll be greeted by your ThirdEye agent, which is named after your computer's hostname. 
- A range is a collection of agents. 
- Tactics, Techniques and Procedures (TTPs) - often referred to as just "procedures" inside Operator - are the individual attacks you can send to your agents in order to test the security of an endpoint. 
- Chains are sets of TTPs which represent a subset of a real adversary kill chain. Prelude's Professional license includes a subscription to "TTP Tuesday", which is weekly chain release. 
- Adversaries are sets of chains, often emulating specific threat actors. 
- A link is the result (beacon) which the agent sends to Operator after running a TTP. A link contains properties like request, response, PID and status (code).
- An operation is the full set of links after deploying a chain/adversary against a range of agents.

### Deploy an agent (local)

> When running an operation, keep an eye on the "skipped" button. Clicking this will show you the procedures from your chain that weren't sent to your agent. Clicking on each skipped row will explain why.

1. Using the filter at the top-left, select any available chain. 
2. Click the edit icon to view the procedures within the selected chain. 
3. Click deploy. This will send the chain to all agents in your "home" range, which is just your local ThirdEye agent right now.
4. Within a few seconds you should see links starting to stream into your agent's dashboard. Click on any row to view the link's properties. 

![alt text](images/deploy.png)

### Deploy an agent (remote)

> Operator acts as a server for remote agents (not on localhost) to send links. By default, Operator serves on localhost only.

1. Change Operator's IP address from localhost to your computer's local IP address. You can make this change by clicking into the network settings (wireless icon). Doing so will allow other computers's on your network to reach Operator's listening posts at ports 2323 (TCP), 4545 (UDP) and 3391 (HTTP).
2. Download a copy of the Pneuma agent by clicking on the agent icon from the operate section. [Pneuma](https://github.com/preludeorg/pneuma) is Prelude's default open-source agent.
3. (optional) Copy Pnuema to any other computer with internet access.
4. (optional) If you did the step above you'll need to ensure Operator can receive links from agents over the internet. You can do this by clicking into the [Connect section](https://www.youtube.com/watch?v=St1GvE40-9Q) and deploying a redirector.
5. Start Pneuma like this, replacing IP with either the IP address from step 1 or your redirector's hostname from step 4: ```./pneuma-darwin -name boogeyman -range red -address IP:2323```. 
6. Inside Operator click the "ranges" drop down. You should see a new "red" range. Select it and you should see your new agent.
7. Deploy any chain against your new agent.

![alt text](images/download.png)

### Where to go from here?

1. Check out the Editor section. This is an Integrated Development Environment for building your own procedures or adversaries. 
2. Drop into the Train section to take any of the free, interactive training programs built into Operator. 
3. Head into the Connect plugin to provision redirectors and test ranges to practice against. 
4. Advanced user? Go to the Plugins section to build your own extensions to the platform.
5. Pop into our [Discord server](https://discord.gg/NWURE99JzE) where we have an active Operator community.

