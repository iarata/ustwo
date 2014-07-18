# Get ready
sudo apt-get update && sudo apt-get upgrade

# Packages
sudo apt-get install nginx python3-pip git uwsgi supervisor uwsgi-plugin-python uwsgi-plugin-python3 ruby npm rabbitmq-server

# NPM/Bower
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g bower

# MongoDB
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | sudo tee -a /etc/apt/sources.list
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install mongodb-10gen
sudo service mongodb start

# Virtualenv
pip3 install virtualenv
virtualenv -p python3 /env/ustwo --no-site-packages

# Sass
gem install sass

# Setup app
cd /srv
git clone https://github.com/publicscience/ustwo.git
cd /srv/ustwo
source /env/ustwo/bin/activate
pip install -r requirements.txt
bower install

# Celery
sudo mkdir /var/log/celery
sudo adduser --system celery --group

# Supervisor
sudo cp /srv/ustwo/setup/supervisor/*.conf /etc/supervisor/conf.d/

# Nginx
sudo sed -i '' 's/# server_names_hash_bucket_size/server_names_hash_bucket_size/g' /etc/nginx/nginx.conf
sudo cp /srv/ustwo/setup/nginx/*.conf /etc/nginx/conf.d/

# Restart
sudo service nginx restart
sudo service supervisor restart