![alt text](images/home.png)

[![Release](https://img.shields.io/badge/dynamic/json?color=blue&label=Release&prefix=v&query=tag_name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpreludeorg%2Foperator-support%2Freleases%2Flatest)](https://github.com/preludeorg/operator-support/releases)
# Operator

### This repository is the spot to report bugs or submit feature requests.

Operator is production-ready infrastructure for continuously testing your security environment. Operator is free & open-source, and provides everything you need to perform realistic offensive security assessments against your cyber defenses.

> Watch our quick [introduction video](https://www.youtube.com/watch?v=Hz8K-jdqpBY)

You can download the latest copy of the application [here](https://www.prelude.org/download/current), for either MacOS, Windows or Linux.

> Did you know that the team at Prelude runs free red team training programs as part of our open-source outreach? We teach IT/InfoSec/DevOps/defenders/software engineers how to red team, so they can apply practical techniques to their day jobs. Check out the [Pink Badge](https://www.prelude.org/training/pinkbadge) for more details.

## Community

When you start Operator, your app loads in our [community](https://github.com/preludeorg/community) resources in order to populate your environment with hundreds of open-source TTPs, payloads, agents, tools, training modules and more. We encourage contributions, so if you'd like to add TTPs for other Operator members, publish your own agents or come up with a new training flag for any of the programs - submit a pull request!

## Resources 

The Prelude development & security teams run several supporting resources for the community:

- A [Discord server](https://discord.gg/NWURE99JzE) to interact with the team.
- A [YouTube video library](https://www.youtube.com/preludeorg) containing tutorials and use cases.
- A [blog](https://feed.prelude.org), where we post on general security and specific Operator topics.
- Details about our [weekly and out-of-band TTP releases](https://chains.prelude.org).

## Operator Terminology

- Tactic, Technique and Procedure (TTP) - A TTP is a specific ATT&CK technique implementation (procedure). Each TTP defines an independent ability a chain could contain, along with classification details describing what operating systems it will work on. Prelude natively supports Windows, Linux and MacOS (darwin) platforms and a series of shell and non-shell executors (i.e., the things that run the commands).
- Chains - A chain is an unordered collection of procedures files. Think of a chain in video game terms; it is an empty profile or shell, and it gets more powerful as you add specific abilities to it. 
- Agent - An agent, often referred to as a Remote Access Trojan, is a process running on a remote computer which can run commands while under the control of a bad actor. Agents beacon into Operator periodically to ask for instructions to run. Each agent is automatically grouped into a range. Agents communicate to Operator through one of several network protocols, such as TCP, UDP, or HTTP.
- Redirector - A redirector is a Linux server running a headless version of Operator. Your local Operator instance will connect to the redirector which acts as a proxy for interating with agents. This allows you to manage agents hosted outside your network, without having to expose your local Operator instance.
- Pneuma - Our most popular open-source agent is called Pneuma, a Go agent which supports all major operating systems and 3 different protocols (TCP, UDP, HTTP). Pneuma is capable of executing nearly all TTPs and chains loaded into Operator, along with built-in support for reverse shells (when connected over TCP). [Source code is available here.](https://github.com/preludeorg/pneuma)

## Quick Start

Whether you are using Operator for the first time or you are checking out the new release, below is a quick rundown of how to get started.

## Installation

> Operator is a multi-platform compiled Electron/NodeJS app.

1. Head to https://www.prelude.org/download/current and download a copy of Operator for your operating system.
2. Double-click the downloaded executable to install Operator the same as any other desktop app.
3. Open Operator. Operator will open to the starting page, where you can get started deploying a chain.

## Deploying a chain

> When running an operation, keep an eye on the "View Queue" button. Clicking this will show you the procedures from your chain that are awaiting execution by the agent. If any TTPs are skipped or queued, they might be waiting for other TTPs to complete or for a specific fact to be present.

1. Select the default agent. 
2. Click "Launch Chain".
3. Type the name of a Chain in the "Find an attack chain to deploy" (File Hunter is a great chain to get started with, as it supports multiple operating systems.) 
4. Click "Deploy". This will send the chain to the selected agent.
5. Within a few seconds you should see results starting to stream into your agent's result log. Click on any row to view additional information on the result.
    
![alt text](images/deploy.png)

## Selecting an Agent for your Operation.

> Using an agent other than ThirdEye (which is baked into Operator) can allow access to additional features (Other protocol support, reverse shells, etc...).

1. You can download one of Prelude's other agents by clicking the "Add Agents" button in Operator

![Download Button](images/download.png)

2. Launch the agent. (Operator runs on localhost by default, most agents are designed to automatically connect to Operator when executed)
3. Your agent should now show up in the list of agents on the main page.

> If you would like to have Operator listen for connections from other computers on the network you can follow these optional steps

4. (optional) Change Operator's IP address from 127.0.0.1 (localhost) to your computer's local IP address. You can make this change by clicking Settings (bottom left), then clicking the General Tab at the top of that page, look for the IP field under the API heading. Doing so will allow other computers on your network to reach Operator's listening posts at ports 2323 (TCP), 4545 (UDP) and 3391 (HTTP).

![Changing the IP](images/IP.png)

> Connecting an agent to the IP you just changed
   
5. (optional) Download a copy of the Pneuma agent from Operator as detailed above or build it from [source](https://github.com/preludeorg/pneuma).
6. (optional) Copy Pnuema to another computer with access to the IP you changed in step 4.
7. (optional) Start Pneuma with these parameters, replacing **IP** with the IP address from step 4. ```./pneuma-darwin -name boogeyman -range red -address IP:2323```.

> The following step is for connecting an Agent to Operator from anywhere on the internet.

8. (optional) Deploy a redirector and connect Operator to it by clicking the [Connect Button](https://www.youtube.com/watch?v=St1GvE40-9Q).
9. (optional) Copy Pneuma to a computer that can access the redirector from step 8, then run the following command, replacing the **IP** with the public DNS hostname from your redirector. ```./pneuma-darwin -name boogeyman -range red -address IP:2323```

## Where to go from here?

1. Create your own TTPs or create your own chain using one of the 200+ open-source TTPs or utilize one of the 450+ TTPs available with our professional subscription. 
2. Click on the Train section to take the free, interactive training program built into Operator. 
3. Pop into our [Discord server](https://discord.gg/NWURE99JzE) where we have an active Operator community.
