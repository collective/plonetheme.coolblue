===================
plonetheme.coolblue
===================


Introduction
============

*plonetheme.coolblue* package is an installable Plone_ Theme using the **theming** and **packaging** 
features available in `plone.app.theming`_ to make the `Styleshout`_ theme `Coolblue`_ easily
available in `Plone`.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============


Add Plone site
--------------

Install Plone 4.x with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/screenshot2.png


Zipfile
-------

If you are an **end user**, you might enjoy installation via zip file import.

1. Download the `zip file <https://github.com/collective/plonetheme.coolblue/raw/master/coolblue.zip>`_.
2. Import the theme from the Diazo theme control panel.

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/screenshot4.png

Buildout
--------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.coolblue`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.coolblue


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.coolblue',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable`` 
on ``Codapress`` theme from the Diazo control panel. 

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/screenshot3.png

That's it!

You should see the layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/plonetheme.coolblue/raw/master/plonetheme/coolblue/theme/coolblue/preview.png

Contribute
==========

- Issue Tracker: https://github.com/collective/plonetheme.coolblue/issues
- Source Code: https://github.com/collective/plonetheme.coolblue

Help
----

Obviously there is more work to be done. If you want to help, pull requests accepted! Some ideas:

* Add a diazo rule to import Plone editing styles
* Configure styles to use portal_css
* Improve styles


License
=======

This work is licensed under a `Creative Commons Attribution-ShareAlike 3.0 Unported License`_.


Credits
-------

- Alex Clark (aclark at clark dot net).
- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).

.. _`Plone`: http://plone.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Diazo`: http://diazo.org
.. _`Coolblue`: http://www.styleshout.com/templates/preview/CoolBlue10/index.html
.. _`Styleshout`: http://www.styleshout.com
.. _`Creative Commons Attribution-ShareAlike 3.0 Unported License`: http://creativecommons.org/licenses/by-sa/3.0/
