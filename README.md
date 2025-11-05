sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git docker.io docker-compose -y
sudo apt install ufw lsof python3 -y
sudo usermod -aG docker ubuntu


git clone https://github.com/<yourusername>/<your-repo>.git
cd <your-repo>

create .env file

docker-compose up -d

check manually:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000


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

