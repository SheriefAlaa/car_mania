Setup:

pip install mezzanine
sudo mkdir /srv/www/example.com/apache/apache.wsgi
sudo mkdir /srv/www/example.com/
cd /srv/www/example.com/
git clone git@github.com:SheriefAlaa/car_mania.git
python manage.py createdb

cd /srv/www/example.com/car_mania/
python manage.py collectstatic

systemctl restart apache2.service
