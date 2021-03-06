=============
ckanext-ontario_theme
=============

Theme for Ontario ckan including:

* metadata schema
* forms
* templates and design


------------
Requirements
------------

.. list-table:: Related projects, repositories, branches and CKAN plugins
 :header-rows: 1

 * - Project
   - Github group/repo
   - Branch
   - Plugins
 * - CKAN
   - `ckan/ckan <https://github.com/ckan/ckan/>`_
   - ckan-2.8.x
   - N/A
 * - Scheming extension
   - `open-data/ckanext-scheming <https://github.com/open-data/ckanext-scheming>`_
   - master
   - scheming_datasets
 * - Fluent extension
   - `open-data/ckanext-fluent <https://github.com/open-data/ckanext-fluent>`_
   - master
   - fluent
 * - ckanapi-exporter
   - `ckanapi-exporter <https://github.com/ckan/ckanapi-exporter>`_
   - master
   - N/A


------------
Installation
------------

To install ckanext-ontario_theme for development, activate your CKAN 
virtualenv and do::

    git clone https://github.com/boykoc/ckanext-ontario_theme.git
    cd ckanext-ontario_theme
    python setup.py develop
    pip install -r dev-requirements.txt
    
    # Install ckanapi-exporter master from github to get around query limit 
    # of 1000 datasets in package_search.
    # TODO: Update to pip install after new release.
    git clone https://github.com/ckan/ckanapi-exporter.git
    cd ckanapi-exporter
    python setup.py develop
    pip install -r dev-requirements.txt

Set the dataset schema::

    # This relies on scheming and fluent, make sure these are already installed.
    # Note: This extension needs to be before scheming in the *.ini config file to let the form overrides work.
    # Specify the new schema for datasets.
    scheming.dataset_schemas = ckanext.ontario_theme:ontario_theme_dataset.json
    scheming.presets = ckanext.scheming:presets.json
                       ckanext.fluent:presets.json

-----------------
Development
-----------------

Follow the `CKAN style rules <http://docs.ckan.org/en/latest/contributing/css.html#formatting>`_.

Converting to Less for styling.

This is the current process until a cleaner setup can be created.

Install npm and less, then compile less files to css before pushing changes.::

    sudo apt install npm
    sudo npm install -g less
    ln -s /usr/bin/nodejs /usr/bin/node
    cd /ckanext-ontario_theme/ckanext/ontario_theme/fanstatic
    lessc ontario_theme.less ontario_theme.css

Styles should be broken down into small modules that do one thing and contain all necessary 
styling for that module. As an example, the smarties.less file should contain all styling
needed for smarties.

-----------------
Running the Tests
-----------------

To run the tests, make sure your ckan install is `setup for tests <https://docs.ckan.org/en/latest/contributing/test.html>`_, do::

    cd ckanext-ontario_theme # go to extension directory
    nosetests --nologcapture --with-pylons=test.ini # active vertual environment that has nosetests.

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.ontario_theme --cover-inclusive --cover-erase --cover-tests

Also, add scheming and fluent to ``/usr/lib/ckan/default/src/ckan/test-core.ini``::

    ckan.plugins = stats scheming_datasets fluent
    scheming.dataset_schemas = ckanext.extrafields:ontario_theme_dataset.json
    scheming.presets = ckanext.scheming:presets.json
                       ckanext.fluent:presets.json

