This is a skeleton for a buildout used by Starzel.de
It lives here: https://github.com/starzel/buildoutskel

Usage
=====

Customize the file site.cfg for site specific configuration.
Add version-pinnnings as required to floating_versions.cfg and pinned_versions.cfg
If required, override default configurations in custom.cfg


Documentation
=============

This buildout can be used for most common Plone-Sites.
Create a buildout.cfg link that links to
- bo-deploy.cfg for a zeo-setup with one zeo-client
- bo-develop.cfg for a development-buildout with some useful tools


Creating a new project
======================

create a project-dir and add it to git
$ mkdir projectname
$ cd projectname
$ git init

Add project to gitosis (by editing and pushing gitosis.conf) or any other repo

Then add remotes to project and get the empty project from the repo
$ git remote add origin git@dev.starzel.de:<projectname>.git
$ git pull origin master

Create master branch only if there is no remote repo
$ touch init.tmp; git add init.tmp; git commit -m "initialize"; git rm init.tmp; git commit -a -m "cleanup"

Add buildout to remotes:
$ git remote add buildoutskel git://github.com/starzel/buildoutskel.git

Create branch buildout
$ git branch buildout 
$ git co buildout

Setup the new branch buildout to trac the remote buildoutskel (pick a specific branch for your Plone-Version)
$ git pull buildoutskel 4.2 

switch back to master and merge branch buildout into master
$ git co master
$ git merge buildout

Push changes into project-repo
$ git push origin

Go an with your work and push your work to origin. Don't ever push to remote buildout


Updating a project
==================

Switch to branch buildout, pull changes and merge with your project-repo
$ git co buildout
$ git pull buildoutskel (master|4.1|4.2|plone3)
$ git co master
$ git merge buildout


Changing an existing project to use this buildout
=================================================

Optionally add empty project-dir and add it to git
$ mkdir projectname
$ cd projectname
$ git init

Optionally checkout project and add buildout to remotes:
$ git remote add origin git@dev.starzel.de:<projectname>.git
$ git pull origin master

Otherwise just cd to the project-dir
$ cd projectname

Add buildout to remotes 
$ git remote add buildoutskel git://github.com/starzel/buildoutskel.git

Create EMPTY branch 'buildout', clean it from all stuff of the branch master 
$ git symbolic-ref HEAD refs/heads/buildout
$ rm .git/index
$ git clean -fd

All in one for copy&paste:
$ git remote add buildoutskel git://github.com/starzel/buildoutskel.git; git symbolic-ref HEAD refs/heads/buildout; rm .git/index; git clean -fd

pull a certain branch into your buildout branch
$ git pull buildoutskel 4.2

Switch back to master and merge branch buildout into master
$ git co master
$ git merge buildout

RESOLVE CONFLICTS. Usually this includes:
- copy cfgs/versions.cfg into versions.cfg
- move customization from cfgs/base.cfg to site.cfg
- delete unneccessary files
- commit the merge

Push changes into project-repo
$ git push origin

Go an with your work and push your work to origin. Don't ever push to remote buildout

