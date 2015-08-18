rremoval: Repository Removal Tool
=================================

## Description

rremoval aims at removing the selected repositories from any of the
Metrics Grimoire toolset databases.

## License

Licensed under GNU General Public License (GPL), version 3 or later

## Download

* Home page: https://github.com/MetricsGrimoire/rremoval
* Releases: https://github.com/MetricsGrimoire/rremoval/releases
* Latest version: https://github.com/MetricsGrimoire/rremoval.git


## Requirements

* Python >= 2.7.1
* MySQL >= 5.5
* Metrics Grimoire database

## Installation

Locally:

    python setup install
    
In the system:

    sudo python setup install

## Running rremoval

You can easily run rremoval from the cloned repository as follows:

    ~/MetricsGrimoire/rremoval/$ rremoval -u <dbuser> -p <dbpassword> -d <dbname> -b <backend> -l

    This lists the repositories available in the selected backend

    ~/MetricsGrimoire/rremoval/$ rremoval -u <dbuser> -p <dbpassword> -d <dbname> -b <backend> -r <repositoryname>

    This remove the selected repository in the selected backend


## Improving rremoval

Source code and ITS available on Github: https://github.com/MetricsGrimoire/rremoval
If you want to receive updates about new versions, and keep in touch with the development team, consider subscribing to the mailing list.
It is a very low traffic list (< 1 msg a day): https://lists.libresoft.es/listinfo/metrics-grimoire


## Contact

* Mailing list at https://lists.libresoft.es/listinfo/metrics-grimoire
* IRC channel in freenode #metrics-grimoire

