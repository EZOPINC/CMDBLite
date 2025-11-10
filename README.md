sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git docker.io docker-compose ufw lsof git iputils-ping -y
sudo apt install vim net-tools telnet -y
sudo usermod -aG docker ubuntu


git clone https://github.com/EZOPINC/CMDBLite.git
cd CMDBLite

create .env file

docker-compose up -d

check manually:
cd backend

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
sudo /home/ubuntu/CMDBLite/backend/venv/bin/python manage.py runserver 0.0.0.0:8000


check 
sudo ufw status
sudo lsof -i -P -n | grep 8000

access from server:
curl http://localhost:8000

test with port 80
sudo python manage.py runserver 0.0.0.0:80
 open in browser:
 http://<your-public-ip>

 sudo lsof -i -P -n | grep 8000
sudo ufw status
sudo ufw allow 80,443,8000/tcp
sudo ufw reload

check if port 80 is listening:
sudo lsof -i -P -n | grep :80

check public ip from backend:
curl ifconfig.me

check from server:
curl ifconfig.me
ping 8.8.8.8
curl -v http://<public ip>

https://marcinmitruk.link/posts/how-to-open-ports-80-and-443-on-an-oracle-cloud-instance/
check state:
sudo netstat -tuln | grep -E '(:80|:443)'

vi  /etc/iptables/rules.v4
add the below:
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT

iptables-restore < /etc/iptables/rules.v4
===> the app is running now in port 80 
Lets configure for gunicorn and Nginx and SSL

sudo apt update
sudo apt install nginx python3-pip python3-venv -y

inside backend:
pip install gunicorn
check gunicorn:
gunicorn --bind 0.0.0.0:8000 cmdb.wsgi
http://<public-ip>:8000

configure gunicorn as a service
sudo apt install nano
sudo nano /etc/systemd/system/cmdb.service

sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d 40.233.109.3


Reload and enable service:

sudo systemctl daemon-reload
sudo systemctl restart cmdb
sudo systemctl enable cmdb
sudo systemctl restart nginx
sudo systemctl enable nginx


