# Randomized Recipe Game
# A service orientated project
The second project I made as part of QA Consulting training
## Installation
### *Prerequisites:* Ansible, 3 VMs, one for jenkins and one for the app to deploy one as well as a SQL server (all online and running)
* Start by changing the IP addresses in the inventory to those of your own servers
* Change the name in resources/daemon.json to match that of your intended jenkins VM
* Run the playbooks by executing the _all.yml with "ansible-playbook - i inventory playbooks/_all.yml" in the bash terminal
* You will now have 2 VMs with docker & docker-compose, both with jenkins users 
* Your jenkins VM will have jenkins installed and your app VM will be initialized as a swarm master 
* Connect to your jenkins IP and add :8080 to the end like so: [YOUR IP ADDRESS]:8080
* You should now be able to enter your jenkins password displayed within the ansible readout (Look for [Installing Jenkins] heading)
* Create a new freestyle project and copy copy this github and select master branch. Select execute build and copy the contents of documentation/jenkins.txt into it. Save your project
* [Follow this guide for whitelisting your application VM and your SQL database VM](https://cloud.google.com/sql/docs/mysql/connect-compute-engine)
* Select build project in jenkins
* You should now be able to connect to your application VM via it's external IP address (or localhost if its your local machine)

## entity relation diagram 
An entity relationship diagram consisting of 1 Table for Recipes containing different ingredients and a method of cooking
![ERD](https://imgur.com/PcTS0I4.png)
## Final Trello
![TRELLO](https://imgur.com/I6SKF9L.png)
## Use Case Scenario
Add me 
## Risk Assessment 
![RA](https://imgur.com/ML0kmHp.png)
