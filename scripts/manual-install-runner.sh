#!/bin/bash

cd
curl -o actions-runner-linux-x64-2.316.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.316.1/actions-runner-linux-x64-2.316.1.tar.gz
tar xzf ./actions-runner-linux-x64-2.316.1.tar.gz
sudo yum install libicu -y
#runner_name=`date +%s`
./config.sh --unattended --url https://github.com/runsap/runsap-aws-1 --name runner2 --token BG527ZUWXK3HJXVSFE6REUTG32UXU --labels Linux,X86,rhel-9,runsap
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status


sudo dnf install python3-pip wget unzip git -y
python3 -m pip install ansible botocore boto3 jmespath ansible-lint

wget https://releases.hashicorp.com/terraform/1.4.4/terraform_1.4.4_linux_386.zip \
&& sudo unzip terraform_*.zip -d /usr/bin/