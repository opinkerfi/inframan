About Inframan
==============

Inframan was created as a "hello world" tutorial for Django. Its current features are to maintain a list of HP ILO and display information like serial numbers and health state.

Install Instructions
====================

If you want to help develop inframan. Here are the steps you required to get inframan running on your own development computer:

```
easy_install python-hpilo
git clone https://github.com/opinkerfi/inframan
cd inframan
python manage.py syncdb
python manage.py runserver
```

After that, log in to http://localhost:8000 and start browsing

Help us improve inframan
========================

To send us patches to Inframan simply do the following:

* Commit any changes you make to inframan
```
git commit -a -m "Something meaningful about what you changes"
```

* Create github account
* Open https://github.com/opinkerfi/inframan and click "fork" button
* Push your code changes to your repo (username means the user you created)
```
cd inframan
git push https://github.com/username/inframan
```

* Open your fork of inframan on github.com and click the "pull request" button
