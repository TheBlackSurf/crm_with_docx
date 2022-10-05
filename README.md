VERY IMPORTANT

Change your path in core/views.py 

from 
                'header-html': '/home/tbs/projects/nowe_do_testu/pdf_nowe2/core/templates/core/header.html',
                'footer-html': '/home/tbs/projects/nowe_do_testu/pdf_nowe2/core/templates/core/footer.html',
to your path

## Django form model to PDF

### Install App:
Linux 🚀
Go to catalog where you want install your app
#### ➕ Create a virtual envairment:  python3 -m venv venv
#### ➕ Active virtual env: source venv/bin/activate
#### ➕ Install all requirements: pip install -r requirements.txt
#### ➕ python3 manage.py makemigrations
#### ➕ python3 manage.py migrate



look for port 8000, this port is your public port app. if yout want, change it
#### ➕ python3 manage.py runserver 0.0.0.0:8000


Now is sqlite database and its fine for small crm, but you want mysql 
go to pdf/setting.py and change 
Very Important: 
Change database only if you want. This app normal working without external database


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

to 

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'my_database',  
        'USER': 'root',  
        'PASSWORD': 'your_password',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  

Now install:
pip install mysqlclient  
now remove db.sqlite3 in your catalog
and  run
python3 manage.py makemigrations
python3 manage.py migrate 

Now install binary file to wkhtmltopdf - this is libary to generate pdf 

Ubuntu 22: 
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb

Ubuntu20
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb

and run command

ubuntu 22
sudo apt install ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
ubuntu 20
sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb

if you have older version linux go to https://wkhtmltopdf.org/downloads.html 

support: gregory.kalmus@gmail.com
