cd flask_recipe
python sitebuilder.py build
rsync -avz --del build/ 192.168.9.6:/webdir/www.renedohmen.nl/recepten
