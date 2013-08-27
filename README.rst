=================================
django_js_utils - Django JS Utils
=================================

django_js_utils is a small utility library that aims to provide JavaScript/Django developers with
a few utilities that will help the development of RIA on top of a
Django Backend.

Reversing Django Urls from Javascript
-------------------------------------
Why is this useful
******************
One of the pillars of Django is DRY principle and hardcoding your urls in Javascript is violating that principle.

Moreover, building parametrized urls on the fly is error-prone and ugly.

What is included
****************
A snippet of Javascript implementation of Django reverse function that can be found in django_js_utils.js

A view jsurls to generate a list of all of your Django urls.

Installation and usage
**********************
1. Install the application from pip::

    pip install django_js_utils

2. Add django_js_utils to your python path and add the django_js_utils application to your INSTALLED_APPS

3. Add the jsurls view to your URL patterns, e.g.,

::

    (r'^jsurls.js$', 'django_js_utils.views.jsurls', {}, 'jsurls'),

4. Load the static django_js_utils.js (which contains the reverse function) and the dynamically-generated jsurls.js from every web page where you plan to use the reverse function (likely just your base.html template). Example:

::

    <script type="text/javascript" src="{% staticfile 'django_js_utils.js' %}"></script>
    <script type="text/javascript" src="{% url jsurls %}"></script>

5. In your JavaScript code, reverse URLs as follows:

::

    django_js_utils.urls.resolve('dashboard')
    django_js_utils.urls.resolve('time_edit', { project_id: 1, time_id: 2 })

For more information about usage, see example.html


TO-DO
------
1. Handle the unnamed Django urls that result in <> in urls.js file, but are not handled in Javascript resolver.

2. Write unit tests

3. Promote the code 