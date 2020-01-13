# Randomized Recipe Game
# A service orientated project 
## Installation
### *Prerequisites:* Ansible, 3 VMs, one for jenkins and one for the app to deploy one as well as a SQL server
* Start by changing the IP addresses in the inventory to those of your own servers
* Run the playbooks by executing the _all.yml with "ansible-playbook - i inventory playbooks/_all.yml" in the bash terminal
* You will now have 2 VMs with docker & docker-compose, both with jenkins users 
* Your jenkins VM will have jenkins installed and your app VM will be initialized as a swarm master 
* Connect to your jenkins IP and add :8080 to the end like so: [YOUR IP ADDRESS]:8080
* You should now be able to enter your jenkins password displayed within the ansible readout (Look for [Installing Jenkins] title)
* 
