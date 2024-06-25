Changelog
=========

Version 1.1.0 [Unreleased]
--------------------------

WIP

Version 1.0.0 [2022-05-06]
--------------------------

Features
~~~~~~~~

- Switched to new Immunity theme, registered the new menu items
- Added more REST API endpoint to manipulate details of Topology, Node and Link

Changes
~~~~~~~

Backward incompatible changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Changed URL prefix of REST API from to ``/api/v1/topology/``
  ``/api/v1/network-topology/``
  for consistency with the other Immunity Modules
- Removed deprecated old receive topology API url;
  use the new URL: ``/api/v1/network-topology/topology/{id}/receive/``

Dependencies
^^^^^^^^^^^^

- Dropped support for Python 3.6
- Added support for Python 3.8 and Python 3.9
- Dropped support for Django 2.2
- Added support for Django 3.2 and 4.0
- Increased Immunity Users version to 1.0.0
- Removed redundant django-model-utils (it's defined in immunity-utils)

Other changes
^^^^^^^^^^^^^

- Moved uuid field of topology admin after main fields
- Changed "View topology graph" button color
- Added the `immunity-utils DjangoModelPermissions
  <https://github.com/edge-servers/immunity-users#djangomodelpermissions>`_
  class to API views
- Allow nodes, link and topologies to be shared among different organizations

Bugfixes
~~~~~~~~

- Ensured ``Link`` and ``Node`` belong to the same topology
- Removed use of custom ``has_permission()`` of old immunity-utils
- Make sure migrations depend on swappable immunity modules
- Load Organization model with swappable in tests

Version 0.5.1 [2020-11-25]
--------------------------

- [fix] Removed static() call from media assets
- [change] Increased `immunity-users <https://github.com/edge-servers/immunity-users#immunity-users>`__ version from 0.2.x to 0.5.x
  (which brings many interesting improvements to multi-tenancy,
  `see the change log of immunity-users <https://github.com/edge-servers/immunity-users/blob/master/CHANGES.rst#version-050-2020-11-18>`_
  for more information)
- Increased `immunity-utils <https://github.com/edge-servers/immunity-utils#immunity-utils>`__ version to 0.7.x

Version 0.5.0 [2020-09-18]
--------------------------

Features
~~~~~~~~

- Added `integration with Immunity Controller and Immunity Monitoring <https://github.com/edge-servers/immunity-network-topology#integration-with-immunity-controller-and-immunity-monitoring>`_
- API: added `swagger API docs <https://github.com/edge-servers/immunity-network-topology/#rest-api>`_
- Admin: added UUID readonly field
- Added user defined properties in Node and Link

Changes
~~~~~~~

- **Backward incompatible**: API and visualizer views now require authentication by default.
  This can be changed through the new
  `IMMUNITY
_NETWORK_TOPOLOGY_API_AUTH_REQUIRED <https://github.com/edge-servers/immunity-network-topology#immunity-network-topology-api-auth-required>`_
  setting
- Upgraded openvpn nodes to netdiff 0.9
- Automatically manage organization of Node and Link
- Changed API URL: /api/v1/receive/{id}/ -> /api/v1//topology/{id}/receive/ (old URL kept for backward compatibility)

Bugfixes
~~~~~~~~

- Fixed link status bug introduced in 0.4
- Fixed exceptions during update of data
- Do not save ``status_changed``, ``modified``, ``created`` in link properties
- Fixed Topology admin for users who do not have delete permission

Version 0.4.0 [2020-06-28]
--------------------------

- [refactoring] Merged code of django-netjsongraph in immunity-network-topology
- [**breaking change**]: URLS at ``/api/`` moved to ``/api/v1/``
- [docs] Reordered & Improved docs
- [add] Requirement swapper~=1.1
- [docs] Added tutorial for extending immunity-network-topology
- [feature] Upgrader script to upgrade from django-netjsongraph to immunity-network-topology
- [change] Requirement netdiff~=0.8.0

Version 0.3.2 [2020-06-02]
--------------------------

- [add] Support for immunity-utils~=0.5.0
- [fix] swagger API fix for serializer

Version 0.3.1 [2020-02-26]
--------------------------

- bumped min immunity-utils 0.4.3
- bumped django-netjsongraph 0.6.1

Version 0.3.0 [2020-02-06]
--------------------------

- Dropped support python 3.5 and below
- Dropped support django 2.1 and below
- Dropped support immunity-users below 0.2.0
- Dropped support immunity-utils 0.4.1 and below
- Dropped support django-netjsongraph below 0.6.0
- Added support for django 3.0

Version 0.2.2 [2020-01-13]
--------------------------

- Updated dependencies
- Upgraded implementation of node addresses (via django-netjsongraph 0.5.0)

Version 0.2.1 [2018-02-24]
--------------------------

- `fe9077c <https://github.com/edge-servers/immunity-network-topology/commit/fe9077c>`_:
   [models] Fixed related name of Link.target

Version 0.2.0 [2018-02-20]
--------------------------

- `cb7366 <https://github.com/edge-servers/immunity-network-topology/commit/cb7366>`_:
   [migrations] Added a migration file for link_status_changed and openvpn_parser
- `#22 <https://github.com/edge-servers/immunity-network-topology/pull/22>`_:
  Added support to django 2.0
- `d40032 <https://github.com/edge-servers/immunity-network-topology/commit/d40032>`_:
  [qa] Fixed variable name error
- `de45b6 <https://github.com/edge-servers/immunity-network-topology/commit/de45b6>`_:
  Upgraded code according to latest django-netjsongraph 0.4.0 changes
- `#17 <https://github.com/edge-servers/immunity-network-topology/pull/17>`_:
  Integrated topology history feature from django-netjsongraph

Version 0.1.2 [2017-07-22]
--------------------------

- `#13 <https://github.com/edge-servers/immunity-network-topology/issues/13>`_:
  Fixed the fetch and receive API bugs
- `#15 <https://github.com/edge-servers/immunity-network-topology/pull/15>`_:
  Imported admin tests from django-netjsongraph
- `#16 <https://github.com/edge-servers/immunity-network-topology/pull/16>`_:
  Added more tests by importing all from django-netjsongraph

Version 0.1.1 [2017-07-10]
--------------------------

- `95f8ade <https://github.com/edge-servers/immunity-network-topology/commit/95f8ade>`_: [admin] Moved submit_line.html to `immunity-utils <https://github.com/edge-servers/immunity-utils>`_

Version 0.1 [2017-06-29]
------------------------

- Added multi-tenancy and integrated `django-netjsongraph <https://github.com/netjson/django-netjsongraph>`_
