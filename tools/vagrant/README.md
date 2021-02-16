# Headless

You can run Prelude Operator in headless mode, which installs and runs the desktop application on a remote Vagrant image and forwards the GUI to the host. 

You may want this if you:

- Want a quick & dirty way to test Operator without installing it on your own computer
- Support a cyber range where you need an automated way to spin an offensive tools up & down
- Want to launch an automated red team through a CI pipeline tool like Jenkins

## Prerequisites

To do this, ensure you have Vagrant and VirtualBox installed. 

> If on a MacOS, you will also need xquartz installed, which can be done via ```brew install xquartz```

## Installation 

Now you can start Vagrant normally:
```
vagrant up
```
And start Operator any time:
```
ssh -XC -p 2222 vagrant@localhost operator
```
