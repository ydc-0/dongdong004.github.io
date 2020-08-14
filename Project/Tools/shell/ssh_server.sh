apt-get update && apt-get install openssh-server vim
# apt install iproute2 sudo
# sudo passwd # 设置 root 密码
# adduser pi sudo
# usermod -aG root pi
vim /etc/ssh/sshd_config
service ssh restart