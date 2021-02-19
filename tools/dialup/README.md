# DialUP

You can run Prelude Operator in headless mode, which installs and runs the desktop application on a remote Vagrant image and forwards the GUI to the host. 

You may want this if you:

- Want a quick & dirty way to test Operator without installing it on your own computer
- Support a cyber range where you need an automated way to spin an offensive tools up & down
- Want to launch an automated red team through a CI pipeline tool like Jenkins

> This process should also work for installing Operator on a cloud server, such as AWS/EC2 however you'll need to execute the Vagrantfile instructions manually as we have not yet scripted the process.

## Prerequisites

To do this, ensure you have Vagrant and VirtualBox installed. 

> If on a MacOS, you will also need xquartz installed, which can be done via ```brew install xquartz```

## Installation 

Now you can start Vagrant normally:
```
vagrant up
vagrant ssh-config
```
Finally, start Operator any time:
```
ssh -XC -p 2222 vagrant@localhost operator
```
> The default password is ```vagrant```

## Advanced usage

If you followed the above steps, you noticed you were required to log in to the Operator instance when it "popped" on screen. If you want to deploy an adversary automatically after Operator is provisioned, you'll want to:

1. Copy the settings.yml file from your laptop's Operator instance to the ```operator-support/tools/vagrant/config``` directory. Then change the local.workspace property to: /home/vagrant/.config/Operator/workspace. 
2. Optionally include any adversary profiles you want in the ```operator-support/tools/vagrant/adversary``` directory.
3. Optionally include a schedules.yml in ```operator-support/tools/vagrant/config```, which will automatically schedule your adversaries to execute.
