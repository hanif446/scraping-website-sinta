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
apt install python3-pip -y <br>
pip install selenium <br>
pip3 install webdriver-manager<br>
pip3 install flask<br>
pip3 install beautifulsoup4

# Konfigurasi Firewall
ufw enable -y <br>
ufw allow 5000 <br>

# Install tmux
apt install tmux <br>
Masuk Tmux <br>
# Tmux
Jalankan script di background <br>
python3 sinta_fix.py <br>
Keluar dari Tmux <br>
CTRL + B kemudian klik D
