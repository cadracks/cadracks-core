Install cadracks_core
*********************

The simplest way to install **cadracks_core** is by creating a Docker image that sets up the required environment.

Note that the *./install_cadracks_core.sh* script maps the $HOME directory of the host machine to the $HOME folder of the Docker container. This means that the $HOME folder of the
host machine and the $HOME of the cadracks_core Docker container share the same files and folders.

Installation steps
------------------

- Install `Docker <https://docs.docker.com/install/>`_ for your platform

- *git clone https://github.com/cadracks/cadracks-core* somewhere under $HOME

- *cd cadracks-core*

- *./install_cadracks_core.sh*

- *./start_cadracks_core.sh*

Now you can execute examples from cadracks-core or write your own examples.


Development environment
-----------------------

After launching the cadracks_core Docker container (*./start_cadracks_core.sh* command) you can type the following command at the container prompt:

*export PYTHONPATH="${PYTHONPATH}:/home/<user>/path/to/cadracks_core/"*

This will allow you to have changes to the cadracks_core package code taken into account for tests and examples.