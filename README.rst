===============
django-minipoll
===============

Django-MiniPoll is a django application who allow you to put 
a mini poll or survey on your website.

You create a question, you give it some choices, you publish and 
yours visitors can answer to the question.

Installation
============

After having put minipoll in your *PYTHON_PATH*, you only have to register **minipoll** 
in your *INSTALLED_APPS* section. And register this bundle of urls in project's urls. ::

  (r'^polls/', include('minipoll.urls')),


Synchronize your database, publish a poll and this is it.

Tags
====

Django-MiniPoll provides 3 templatetags for displaying the polls on your website.

* display_poll_form

  This tag if for publishing a poll form for user submissions.

* display_poll_result
  
  You can display the results of the poll by putting this tag on your pages.

* display_last_poll

  For simply including the latest poll in your website. If an user as already vote,
  the results are displayed else the poll form.

