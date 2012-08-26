===============
Denigma Project
===============

Denigma is the digital Engima destined to decipher life.
This repository is planting its seed.


Setting up Denigma
==================

In order to set up Denigma locally just do the following 
(Ubuntu or at least a UNIX environment is recommended):

1. Git in:

   Go to the GIT bootcamp (sign up if you haven't already): https://github.com/

   In brief on UNIX: ::

    $ sudo su # Get full control about your machine. 

    $ apt-get install git # Get (g)it!

   Configure Git with your name and e-mail: ::

    $ git config --global user.name "FULL NAME"

    $ git config --global user.email email@address.com

2. Fork Denigma: ::

    $ git clone https://github.com/hevok/denigma

3. Get the Might to Create Virtual Environments: ::

    $ curl http://python-distribute.org/distribute_setup.py | python

    $ easy_install virtualenv

    $ cd denigma

    $ virtualenv env

    $ . env/bin/activate

4. Start Denigma: ::

    $ apt-get install python-dev libmysqlclient16-dev # Database-backend.

    $ pip install -r denigma/requirements/project.txt

    $ denigma/manage.py syncdb --all

    $ denigma/manage.py migrate --fake

    $ denigma/manage.py runserver

5. Change Denigma: ::

    $ git commit -am "Brief description of the change."

    $ git push origin master

6. Keep Denigma Updated: ::

    $ git checkout master # Update to the latest version.

    $ git pull # Pull it from master.