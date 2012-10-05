=============
Documentation
=============

Denigma is not just a Engima which starts with D, the Denigma project is a DDD 
(Documentation-Drived Development). Its source code is documented from the 
very beginning. Every decision is documented as well as every issue 
encountered including the corresponding found solution to it.

In contrast to papers and reviews, in Denigma *the ink is never dry*.
It changes continously until it gets it absoluty right.


Deploying Denigma
=================

To deploy Denigma in the clouds the Amazone Web Service (AWS) is used.

1. Launch an Ubuntu AMI:

   Preferable a maverick build such as the ami-975a6de3 (called Giter; which 
   ships a GIT repository) or the ami-fd7b4089 (called Daily which is 
   up-to-date and does not require updating/upgrading or more precise minimal 
   updating/upgrading). Set up of Giter takes approximately 7 minutes and the 
   Daily takes 3 minutes due to the already installed updates (However the 
   inclusion of additional third-party libraries increased this time slightly).

2. Create and mount an seperate EBS Volume to it.

3. ssh into the machine with the DNS and keypairs aquired from the Amazone 
Control Center (use bash ami.sh). On the machine: ::

$ sudo su
$ cd ..
$ aptitude install git # Only on Daily, not necessary on Giter. 
$ git clone https://github.com/hevok/denigma
$ bash denigma/configure.sh


Developmental Notes
===================


Serving Media
-------------

The media/static files for the Admin Interface were intially not used and there
it was unstyled. To solve this issue:

1. Add the following line to the Apache config file (/etc/apache2/http.conf):

   Alias /django/contrib/admin/media/ /home/denigma/env/lib/python2.6/site-packages/django/contrib/admin/media/

2. Set in the settings.py:

   ADMIN_MEDIA_PREFIX = '/django/contrib/admin/media/'

Similiar Pinax static files were also not used right after deploying.
Copying of the static files from the pinax_theme_botstrat/static/ into project/site/media solved this problem: ::

$ cp -rf /home/denigma/env/lib/python2.6/site-packages/pinax_theme_bootstrap/static/. /home/denigma/denigma/media

However removing this files again does not abolish the styling, immediatly 
but with some delay. Possible the cookies forget about it or something (reload 
cookies with Ctrl + F5).


'bool' object has no attribute 'status code'
--------------------------------------------

It appears that the pinax.middleware.security.HideSensitiveFieldsMiddleware in 
the MIDDLEWARE_CLASSES of the settings.py is causing an error which propagates 
and makes debuging nearly impossible
[http://comments.gmane.org/gmane.comp.python.django.pinax.devel/104].

Deactivating it by commenting out abrogates this problem. Consider to inlcude 
it with an if statement only in debuging mode.


Missing Markup
--------------

In the Wiki view.html the load markup tag raised an error. Including the 
"django.conrib.markup" in the settings.py fixed it 
[http://stackoverflow.com/questions/6399649/django-markup-templatetags-error].


CSRF Problem
------------

Submit forms such as those in the Wiki edit and search need to be tagged with a
{% csrf_token %}. This worked fine for the edit form 
[findhttp://jordanmessina.com/2010/05/24/django-1-2-csrf-verification-failed/]. 
However it failed on the search form. Deactivating by commenting out the django.middleware.csrf.CsrfViewMiddleware in the MIDDLEWARE_CLASSES resolved 
this problem, but is only a suboptimal solution. Adding a RequestContext 
handler to the render_to_response in the search view which was already present 
in the edit view resolved this issue 
[http://stackoverflow.com/questions/3197321/csrf-error-in-django].


mysql in virtual env 
--------------------

For interfacing with mysql of the purpose of database evolution 
libmysqlclient16-dev library is required 
[http://stackoverflow.com/questions/8868545/installing-mysql-for-python-within-virtual-environment].
Note that the Ubuntu 12.04 repository does not contain these specific library 
anymore, but rather that provides libmysqlclient-dev 
[http://askubuntu.com/questions/137788/problem-with-deleting-libmysqlclient16-dev-from-repository-of-12-04].

::

$ aptitude install libmysqlclient16-dev

$ pip install MySQL-python


Depricated Constants
--------------------

Runnig python denigma/manage.py migrate --list just returns that ENGINE is 
depriciated [http://jira.osqa.net/browse/OSQA-712].


mysql-ebs
---------
 
Prepare db for snapshot: ::

$ mysql -u root
$ FLUSH TABLES WITH READ LOCK;
$ SHOW MASTER STATUS;
$ SYSTEM sudo xfs_freeze -f /vol


Create Snapshot: ::

$ SYSTEM sudo xfs_freeze -u /vol
$ UNLOCK TABLES; # Release lock.
$ EXIT


Clean up: ::

$ sudo /etc/init.d/mysql stop
$ sudo umount /etc/mysql /var/lib/mysql /var/log/mysql /vol


Restoring a snapshotted database
--------------------------------

::

$ cd ..
$ sudo su
$ aptitude install git
$ git clone https://github.com/hevok/denigma
$ bash denigma/reconnect-ebs.sh
$ bash denigma/open-port.sh
$ sudo bash ./denigma/aws-django -n denigma -d https://github.com/hevok/denigma/raw/master/denigma.tgz -s "/s" -H <DNS> -D denigma -U denigma -P <PASSWORD>


Transferring data onto EC2
--------------------------

It is considered to transfer the Denigma database directly onto an EC2 
instance. SFTP (secruity file transfer protocol) can be used via port 22 to 
directly exchange data with the EC2 instance. FileZilla can be used for this 
purpose [http://www.turnkeylinux.org/forum/support/20100413/how-do-you-get-data-and-out-ec2].
Add the keypair via settings [http://www.codestore.net/store.nsf/unid/BLOG-20111012-0812].
Settings in Ubuntu are at the terminal bar 
[http://superuser.com/questions/159846/change-filezilla-settings-in-ubuntu-linux-so-view-edit-uses-gedit].
Convert the keypair from .pem to .pkk 
[http://www.onebloke.com/2011/06/filezilla-sftp-and-amazon-ec2/].

::

$ sudo aptitude install filezilla

> Open the Site Manage
Host: <DNS>
Port: 22
Logon Type: Norma
User: Ubuntu 

> Edit > Settings
SFTP > Add keyfile...
Convert key

It is noted that when FileZilla transferes data to a EC2 instance it results 
into a block of the internet connection. Possible another port such as 21 has 
to be prefered for connecting to an EC2 instance via sFTP.


Customizing Django Admin
------------------------

Creating a admin folder in project template directory and modifying the 
original admin templates in this folder allows to do basic customization of the
admin interface. In this way for instance the title can be changed 
[http://overtag.dk/wordpress/2010/04/changing-the-django-admin-site-title/].


Database Renaming
-----------------

There are several ways on how to rename a database. The simplist appears to use
a script which renames all tables in conjuction with another database table 
[http://stackoverflow.com/questions/67093/how-do-i-quickly-rename-a-mysql-database-change-schema-name].


Tagging
-------

Django tagging impairs south schema migration. It raises an NoMigration 
exception similiar as reported for django.contrib.auth 
[http://stackoverflow.com/questions/2845697/south-migration-error-nomigrations-exception-for-django-contrib-auth].
The django tagging tables are now in Denigma but the app is not installed nor 
appear the tables to be probably linked. There seems to be only a relationship 
field in link table. This tables and the link relation should probaly be 
removed via raw sql statements before it is intended to implment tagging.

django-taggit, an alternative to django-tagging also some has issues. For 
instance, tags cannot direclty be added to the admin list filter but it works 
by adding tag__name instead of tags [https://groups.google.com/forum/?fromgroups=#!topic/django-taggit/9FwdigQDrJ4]. A patch was proposed for this issue 
[https://groups.google.com/forum/?fromgroups=#!topic/django-taggit/9FwdigQDrJ4].


sqlite
------

sqlite is a leightweight sql database variant. There are two versions of 
sqlite3:

One is a python module, the other is a executable application.
The manage.py dbshell uses the latter one and complains if it is not installed 
[https://groups.google.com/forum/?fromgroups#!topic/django-users/4YMFm1C14tk[1-25]].


Domain Forwarding/Redirection
-----------------------------

The frame redirection causes that numerous external links are not functional and sub 
folders are not displayed.

How to set up domain forwarding so that it
only replaces the base address?

Just to explain the problem:

Let's assume you have a server address (http://myserver.com) and you have
full root control over the server. You also have a domain (e.g. from 1&1) which
you can set up either to http or frame forwarding (http://mydomain.org).

If you do http-forwarding http://mydomain.com just redirects to the server
address (http://myserver.com) and subfolders
(http://myserver.com/subfolder/) are displayed correctly.

So if you made a frame forwarding to http://myserver.com and it works as it
displays http://mydomain.org in the address bar and the content of
http://myserver.com but if you when navigate on the site tree it does not show
any "subfolder", e.g. http://myserver.com/subfolder/. Rather than it
just converts everything to http://mydomain.org in the address bar.

So now the question is how to set it up that it displays the domain name
and the subfolders, e.g. http://mydomain.org/subfolder/, and only
replaces the base address of the server?
#
A possibility would be to edit the .htaccess file
[http://support.lunarpages.com/knowledge_bases/article/549].

The .htaccess file: [http://en.wikipedia.org/wiki/Htaccess].


Enabling user of .htaccess
[https://help.ubuntu.com/community/EnablingUseOfApacheHtaccessFiles].
Using .htaccess [http://www.joeldare.com/wiki/linux:using_.htaccess_on_ubuntu].
DNS setup: the full story: http://support.webvanta.com/support_article/615695-dns-setup-the-full-story#Makingthebasedomainnamework

Same issue: http://stackoverflow.com/questions/10112953/url-subfolders-not-shown-while-using-yahoo-maked-forwarding

Exactly the same problem: http://stackoverflow.com/questions/2208728/forwarding-from-domain-names-whithout-using-frames?rq=1

http://www.tonybhimani.com/2008/01/26/domain-redirection-using-apache-mod_rewrite-and-htaccess/

http://www.widexl.com/tutorials/mod_rewrite.html

Changing domain names with mod_rewrite: http://www.webmasterworld.com/forum92/152.htm
Name-based Virtual Host Support:  http://httpd.apache.org/docs/2.2/vhosts/name-based.html

redirect subdomains bar one: http://stackoverflow.com/questions/9712352/redirect-subdomains-bar-one

The solution to this dilema is to set up an A-Record in the DNS configuration 
of the domain provider. The nameserver of the provider can be used and the 
elastic IP address inserted into the configuration.


UNIX
----

Take the opportinuty to venture in to the wonderful land of UNIX. It will make 
your life much, much easier. If you havve the option, install Linux beside your 
Windows in a dual boot setting and after that, Django and ALL Django app 
godness is just one command away.

Most hosting environents use Linux, that's why it is better to use Linux for 
development too.

Linux + nginx + uwsgi = awesome


To run the server locally on a specific port, pass the ip to the manage.py by 
running it: ::

$ ./manage.py runserver 0.0.0.0:8001

or ::

$ ./manage.py runserver localhost:8002


HTML
----

Severel ways exist to change the color of a hyperlink. For instance it is 
possible toe add a style attribute and insert a color property.

<a herf="change-hyperlink-color.html", style="color: #CC0000">change hyperlink color</a>


Usage Considerations
====================

Storage of data on an EBS snapshot is cheap 
[https://forums.aws.amazon.com/message.jspa?messageID=172925].
Pricing for EBS snapshots:
- Daily: bytes*24
- Monthly:bytes*24*dayes of the months


Pinax
-----

Pinax is a framework build on top of Django that aims to provide several 
reusable apps. The latest development version is 0.9b1.dev10. The basic website 
tab is defined in templates/site_base.html and the actual text is localizable 
resource files like locale/LC_MESSAGES/django.po.
The django.po files are autogenerated via: ::

$ ./manage.py makemessages -l en

Gettext need to be installed to get this commadn work:
sudo aptitude install gettext


BitNami
-------

BitNami provides a DjangoStack for deplyoing projects in the cloud. It might 
be intersting to try their images. However it is not recommanded to use any 
stack as it restricts choices and overloads the server with application which 
might be not used as well as takes of the implementation details and limits 
customation.


Django
------

The high-level python-based web framework Django encourages rapid development 
and clean, pragmatic design. It was innitially developed by a fast-moving 
online-news operation. It was designed to hadle two challanges:

1. intensive deadlines of a newsroom

2. stringent requirements of expierenced Web developers.

Django allowas to build high-performing, elegant Web applications quickly.


Generic forms
-------------

A generic detail form as well as the admin form can not have a modifable 
created and updated field which are defined in the database model as 
auto_now_add and auto_now.


Auto-log out and failed rendering
---------------------------------

Some views such as the Wiki and the experts invoke auto-log out and wrong 
rendering of the branding etc. It appears that adding the request context to 
the render_to_response fixes this issue. It might be because things like user site name is used in the upper most templates. Inclusion of the RequestContext is sufficient to eliminate 
this issue entierly.


Overflow
--------

Longer pages lead to the inlcusion of a scroll bar which provokes a shift of 
the header to the left site.

It can be avoided by enforcing the scrollbar for all pages 
[http://www.daniweb.com/web-development/web-design-html-and-css/threads/336106/thirteen-ore-more-rows-in-a-table-makes-my-header-shift].

<style>body { overflow:scroll; }</style>

There are alternative solutions 
[http://hicksdesign.co.uk/journal/forcing-scrollbars-now-even-better].


Comments in CSS
---------------

The synthax for commenting in CSS code is enclosing slash-asterisk:

/* comment */

/* multiline 
comment */

For details on the synthax and base data types in CSS see 
[http://www.w3.org/TR/CSS2/syndata.html].

Ctrl + F5 reloads the cached style in the browser.


EMAIL
-----

There are two major possibilities to set up an email server.
First Configure the email server yourself or use a third party provider.
There are for instance AWS SES Google Apps' gmail 
[http://stackoverflow.com/questions/5123098/aws-ses-vs-google-apps-gmail].

The Amazon Simple Email Service (SES) can be used under the Free Tier 
[http://aws.amazon.com/ses/].

Django can easily be configured to use the SES service 
[http://hmarr.com/2011/jan/26/using-amazons-simple-email-service-ses-with-django/] via django-SES.

First of all a Email address was added to the SES account and verified.

django-ses was added to the requirements/project.txt and installed locally.

Both the Email address of ADMINS and CONTACT_EMAIL was set to the Email 
address, but neither one appeared to be cruical.
AWS access and secret keys were defined in key.py as well as email backend 
(nothing else):

AWS_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'

AWS_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'

EMAIL_BACKEND = 'django_ses.SESBackend'

This setup was tested locally by running the server (this was not critical) and going into the

::

$ ./manage.py shell

::

>>> from django.core.mail import send_mail
>>> send_mail("Subject", "Text", 'name@xyz.com', ['name@xyz.com'], fail_silently)

Testing now wether the server need to run to get it working.

Messaging via pasted items only works by placing DEFAULT_FROM_EMAIL constant 
into the settings.

A restriction of SES is that it only allows sending Emails, but not retrieving. 
For this purpose gmail is suitable 
[http://stackoverflow.com/questions/10640507/how-to-configure-email-accounts-like-supportxyz-com-or-feedbackxyz-com-on-aws].
In such AWS SES will be used to send mail and mail will be recieved by the 
domain's Gmail user.

After creating by account by Google APPs, domains can be added by visiting 
www.google.com/a/domain.tld. Following the instruction a html Email 
conformation can bea ccomplished. Then MX records if the domain provider need 
to be changed as instructed. This may take up to 24 hours.

DNS stands for Domain Name System (Internet address book). CNAME are for 
subdomain [http://support.google.com/a/bin/answer.py?hl=en&answer=53340].

Evolution can be configured to access Email handled by gmail 
[https://help.ubuntu.com/community/UsingGmailWithEvolution].

Office can also be configured to directly use the domain by changing the MX 
records
[http://onlinehelp.microsoft.com/en-us/office365-enterprises/gg584186.aspx].

SES can alternatively also be used with Postman and Postix
[ Using Amazon SES in Python with Postman and Postfix], but here Django will be used.

For sending Emails via gmail account a few settings need to be declared
[http://stackoverflow.com/questions/6914687/django-sending-email].

Gmail can be used to send Emails of a specfific domain via SES. However,
the Email address of this domain can not be addressed via SES as it is sayed to be blacklisted. Fortunately, it is not necessary to send Emails from Denigma to Denigma so far.  


Django Verbose names
--------------------

The representative name of a model in admin can be ovewritten via a meta class:

class Meta:
    verbose_name = "foo"
    verbose_name_plural = "foobars"


user access in models methods
-----------------------------

To access current user information in the models.py for templated views the request.user should be passed to the e.g. models methods. For the Admin interface the request user can be passed in the admin.py under the method save [http://stackoverflow.com/questions/10991460/django-get-current-user-in-model-save].


Database Charset
----------------
The default charset in MySQL is latin1, which is suboptimal as it only provides
a very limited character set. utf8 is the apperent best coding format. To
convert a table. To convert a given table to utf8 command this: ::
    ALTER TABLE <table_name> CONVERT TO CHARACTER SET utf8;

The whole database should better have utf8 as default set and therefore a total
conversion is required.


Admin Bootstrap
---------------
TO install bootstrap look for the admin interface: ::
    $ git clone https://github.com/gkuhn1/django-admin-templates-twitter-bootstrap/
    $ pip install -e git+https://github.com/gkuhn1/django-admin-templates-twitter-bootstrap/#egg=django-admin-templates-twitter-bootstrap


UnicodeError
------------

Some text raise UniCodeError when tried to print to terminal.
The follwing transformation solves this problem:
text = text.encode('ascii', 'ignore') 
[http://stackoverflow.com/questions/3224268/python-unicode-encode-error].


Favicon
-------
The small icon in the address bar is called favicon.ico [1].
There are eat least three different ways to implement it [2].
1. On apache server by adding this to the httpd.conf [2,3]: ::
    LoadModule alias_module modules/mod_alias.so
    <LocationMatch "^/favicon.ico">
        SetHandler default
    </LocationMatch>
    alias /favicon.ico /home/denigma/denigma/media/img/favicon.ico
2. On URLconf [2,4-5]: ::
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',
       {'url': '/media/img/favicon.ico'}), # Site icon
3. In the base template header (such as theme_base.html) [2,5]: ::
    <link rel="shortcut icon" type="image/x-icon" href="/media/img/favicon.ico">
    <link href="/media/img/favicon.ico" rel="icon" type="image/x-icon">

All three were implemented but only third approach seems to work.
The respective icon was generate with GIMP by using a png to start with
If transparency is desired an alpha layer (if not allready there) and
the background color removed. The ong was scaled to 16x16 pixel (px) [6,7].

[1] http://en.wikipedia.org/wiki/Favicon
[2] http://community.webfaction.com/questions/774/create-an-icon-for-a-django-app
[3] http://www.pkshiu.com/loft/archive/2008/08/serving-favicon-in-an-django-app-using-apache
[4] http://www.netboy.pl/2011/10/add-favicon-ico-robots-txt-to-a-django-project/
[5] http://www.codekoala.com/blog/2008/setup-faviconico-django/
[6] http://www.aha-soft.com/faq/make_website_icon.htm
[7] http://tools.dynamicdrive.com/favicon/

Admin Favicon
-------------
In Django-1.4 the Favicon did not appear in the admin for unknown
reason as it worked well in Django-1.3. Several ways allow to put
an favicon into the admin [http://jaredforsyth.com/blog/2010/apr/6/giving-django-admin-favicon/].


Forms
-----

Bootstrap forms
~~~~~~~~~~~~~~~
To inlcude a bootstrap form to the following [1]: ::
   {% load bootrap_tags %}
   ...
   <form>
      <legend>A Form</legend>
      {% csrf_token %}
      {{ form|as_boostrap }}
      <div class="form-actions">
        <a href="form-actions">
        <button type="submit" class="btn btn-primary">Save changes</button>
     </div>
   </form>

Dropdown should better be triggered by hover [2-4].

[1] https://github.com/pinax/pinax-theme-bootstrap
[2] https://github.com/chrisdev/pinax-theme-foundation/pull/19
[3] http://stackoverflow.com/questions/8878033/how-to-make-twitter-bootstrap-menu-dropdown-on-hover-rather-than-click
[4] http://jsfiddle.net/ekjxu/
#234567891123456789212345678931234567894123456789512345678961234567897123456789


Crispy
~~~~~~
The best way to have DRY django form is `django-crispy` form which allow to define the form in python and provides tag
and filter to quickly render forms in a div format while providing an eneromous amount of capability to configure and 
control rendered HTML [https://github.com/maraujop/django-crispy-forms]. `crispy-forms` is very well documented:
[http://django-crispy-forms.readthedocs.org/en/d-0/index.html].


Deployment
----------
The requirements are not installed on the local env.
On installing the requirements locally, it was found that MySQL-python-1.2.4b3 could not be installed
because distribute was only version 0.6.24, but version 0.6.28 is required. The same version is
installed on the global pip on deployment. It was also noted that MySQL-python had to be installed
extra during deployment. Therefore, the most rational explaination might be that pip failed during
deployment. virtualenv & distribute shall be always kept up-to-date: ::

    . env/bin/activate
    pip install --upgrade distribute

Need ot figure out how to update virtualenv.


Getting a querysets for template forms
--------------------------------------
In order to obtain a queryset from template forms for many-to-many relationships,
the `.getlist('field') can be used on the request.POST method.


Notifications
-------------
[https://github.com/yourcelf/btb/issues/3]


Customizing Styles
-----------------
The bootstrap hero-unit was modified to have less margin: ::

}
.hero-unit {
  padding: 6px; /* 60 */
  margin-bottom: 30px; /* 3 */
  background-color: #f5f5f5; /* f5f5f5; 993399 FF99CC */ FFEEEE ffeeff
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
}

Citations
---------
If you want to build a ship, do not drum up the men to gather the wood, divide the work and give orders.
Instead teach them to yearn for the vast and endless sea. - Antoine de Saint-Exupery

If you want to construct an Enigma do not drum up the mean to gather the pieces, divide the work and give orders.
Instead teach them to yearn the vast and endless possibilities of Denigma. - Hevok


Scalability
-----------
A scalable system doesn't need to change when the size of the problem changes.
* Accommodate increased usage
* Accommodate increased data
* Maintainable.

There are two kinds of scalabality:
* Vertical scalability: buying more powerful hardware, replacing what you already own.
* Horizontal scalability: buying additional hardware, supplementing what you already own.

Horizontal scalability is the ability ro increase a system's capacity by adding more
processing units (services)