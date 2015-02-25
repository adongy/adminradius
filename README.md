Adminradius
===========

A simple Django application to manage users in a FreeRADIUS database. It was designed to be light, and straightforward, meaning it is easy (and mainly the only things you can do) to access the raw data.

The RADIUS database used allows users to connect between specific dates. Each user can have its own start and end dates, and a password *can* be specified.

Database-wise, the password is stored using NTLM, a hash without a salt (thus, you must still be careful, as the passwords are subject to rainbow tables and other attacks). This was chosen because it is the *only* hash supported with PEAP/MSCHAPv2 authentication.

# Requirements and setup

The FreeRADIUS schema used is generated from the 3.0.6 version, available [here][fr].

Adminradius provides a `requirements.txt`. Using `pip`, installing dependencies is as easy as running `pip install -r requirements.txt`. It is recommended to use a `virtualenv`, which is not described here.

Please edit the `settings_private.py` file to your needs: a template is provided (named `settings_private.py.template`)

Migrations are provided to modify the RADIUS database. Besides the tables required by Adminradius, an `id` column is added to the `radusergroup` table. Run them using `python manage.py migrate`

Static files are included in this application. Don't forget to run `python manage.py collectstatic` before you run Adminradius.

# Notes

Adminradius uses well-known CDNs for Bootstrap and jQuery. Edit manually `admin_radius/templates/base.html` to use a static version if you like.

User authentication is pretty scarce: there are no permissions, just login and you are allowed to do nearly everything.

User creation javascript is inline, but it requires runtime-variable. We cannot outsource it.

# TODO

- Tests tests tests.
- Think about timezone-aware datetimes. Disable USE_TZ or use django.utils.timezone.make_aware?

[fr]: ftp://ftp.freeradius.org/pub/freeradius/freeradius-server-3.0.6.tar.gz