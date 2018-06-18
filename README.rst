======================
foglamp-south-sinusoid
======================

FogLAMP South Plugin for sinusoid. `read more <https://github.com/foglamp/foglamp-south-sinusoid/blob/master/python/foglamp/plugins/south/sinusoid/readme.rst>`_


***********************
Packaging for sinusoid
***********************

This repo contains the scripts used to create a foglamp-south-sinusoid package.

The make_deb script
===================

.. code-block:: console

  $ ./make_deb help
  make_deb help {x86|arm} [clean|cleanall]
  This script is used to create the Debian package of foglamp south sinusoid
  Arguments:
   x86      - Build an x86_64 package
   arm      - Build an armv7l package
   clean    - Remove all the old versions saved in format .XXXX
   cleanall - Remove all the versions, including the last one
  $


Building a Package
==================

Select the architecture to use, *x86* or *arm*.
Finally, run the ``make_deb`` command:


.. code-block:: console

    $ ./make_deb arm
    The package root directory is         : /home/pi/foglamp-south-sinusoid
    The FogLAMP south sinusoid version is : 1.0.0
    The Package will be built in          : /home/pi/foglamp-south-sinusoid/packages/Debian/build
    The architecture is set as            : armhf
    The package name is                   : foglamp-south-sinusoid-1.0.0-armhf

    Populating the package and updating version file...Done.
    Building the new package...
    dpkg-deb: building package 'foglamp-south-sinusoid' in 'foglamp-south-sinusoid-1.0.0-armhf.deb'.
    Building Complete.
    $


The result will be:

.. code-block:: console

  $ ls -l packages/Debian/build/
    total 12
    drwxr-xr-x 4 pi pi 4096 Jun 14 10:03 foglamp-south-sinusoid-1.0.0-armhf
    -rw-r--r-- 1 pi pi 4522 Jun 14 10:03 foglamp-south-sinusoid-1.0.0-armhf.deb
  $


If you execute the ``make_deb`` command again, you will see:

.. code-block:: console

    $ ./make_deb arm
    The package root directory is         : /home/pi/foglamp-south-sinusoid
    The FogLAMP south sinusoid version is : 1.0.0
    The Package will be built in          : /home/pi/foglamp-south-sinusoid/packages/Debian/build
    The architecture is set as            : armhf
    The package name is                   : foglamp-south-sinusoid-1.0.0-armhf

    Saving the old working environment as foglamp-south-sinusoid-1.0.0-armhf.0001
    Populating the package and updating version file...Done.
    Saving the old package as foglamp-south-sinusoid-1.0.0-armhf.deb.0001
    Building the new package...
    dpkg-deb: building package 'foglamp-south-sinusoid' in 'foglamp-south-sinusoid-1.0.0-armhf.deb'.
    Building Complete.
    $


    $ ls -l packages/Debian/build/
    total 24
    drwxr-xr-x 4 pi pi 4096 Jun 14 10:06 foglamp-south-sinusoid-1.0.0-armhf
    drwxr-xr-x 4 pi pi 4096 Jun 14 10:03 foglamp-south-sinusoid-1.0.0-armhf.0001
    -rw-r--r-- 1 pi pi 4518 Jun 14 10:06 foglamp-south-sinusoid-1.0.0-armhf.deb
    -rw-r--r-- 1 pi pi 4522 Jun 14 10:03 foglamp-south-sinusoid-1.0.0-armhf.deb.000
    $

... where the previous build is now marked with the suffix *.0001*.


Cleaning the Package Folder
===========================

Use the ``clean`` option to remove all the old packages and the files used to make the package.
Use the ``cleanall`` option to remove all the packages and the files used to make the package.
