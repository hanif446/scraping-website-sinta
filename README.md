# scraping-website-sinta

#!/bin/bash
# Login
sudo su
# Install upgrade
apt update <br>
apt upgrade -y

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt-get -f install -y
dpkg -i google-chrome-stable_current_amd64.deb

# Install dependencies
apt install python3-pip -y
pip install selenium
pip3 install webdriver-manager
pip3 install flask
pip3 install beautifulsoup4

# Konfigurasi Firewall
ufw enable -y
ufw allow 5000

# Install tmux
apt install tmux
Masuk Tmux
# Tmux
Jalankan script di background
python3 sinta_fix.py
Keluar dari Tmux
CTRL + B kemudian klik D
