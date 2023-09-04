#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}


  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu$(lsb_release -cs)/stable"



netsh interface portproxy add v4tov4 listenport=420 listenaddress=0.0.0.0 connectport=420 connectaddr
ess=(wsl hostname -I)