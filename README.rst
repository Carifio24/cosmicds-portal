.. These are examples of badges you might want to add to your README:
please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/cosmicds-portal.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/cosmicds-portal
    .. image:: https://readthedocs.org/projects/cosmicds-portal/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://cosmicds-portal.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/cosmicds-portal/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/cosmicds-portal
    .. image:: https://img.shields.io/pypi/v/cosmicds-portal.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/cosmicds-portal/
    .. image:: https://img.shields.io/conda/vn/conda-forge/cosmicds-portal.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/cosmicds-portal
    .. image:: https://pepy.tech/badge/cosmicds-portal/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/cosmicds-portal
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/cosmicds-portal

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

===============
CosmicDS Portal
===============

Front-end user portal for users and educators to setup classes and data stories.

Starting the Server
===================

To run the portal locally, there are a series of steps needed to setup the local instance:

1. Clone the repo locally, then change to the package directory. Install the portal package using

.. code-block::

   $ pip install .

2. Start the Solara portal app (ask @nmearl for the required access tokens if needed)

.. code-block::

   $ SOLARA_SESSION_SECRET_KEY="SECRETTESTKEY" SOLARA_OAUTH_CLIENT_ID="..." SOLARA_OAUTH_CLIENT_SECRET="..." SOLARA_OAUTH_API_BASE_URL="..." SOLARA_OAUTH_SCOPE="openid profile email" SOLARA_SESSION_HTTPS_ONLY=false solara run cosmicds_portal.pages --port=8865



