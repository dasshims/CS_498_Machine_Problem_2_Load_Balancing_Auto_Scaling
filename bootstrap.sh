#!/bin/bash
sudo apt-get update
sudo apt-get install stress-ng -y
sudo apt-get install htop -y
sudo apt-get install python3-pip -y
pip install flask
sudo apt-get install git -y
cd /home/ubuntu
git clone https://github.com/dasshims/CS_498_Machine_Problem_2_Load_Balancing_Auto_Scaling.git
cd /home/ubuntu/CS_498_Machine_Problem_2_Load_Balancing_Auto_Scaling
python3 serve.py