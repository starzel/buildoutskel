This is a skeleton for a buildout used by Starzel.de

Usage
=====

Customize the files site.cfg and versions.cfg according to site


Documentation
=============

This buildout can be used for most common Plone-Sites.
./bin/buildout -c bo-deploy.cfg sets up a zeo-setup with one zeo-client. 
./bin/buildout [-c buildout.cfg] sets up a development-buildout with some usefull tools 


Creating a project
==================

create a project-dir and add it to git
$ mkdir projectname
$ cd  projectname
$ git init

Add project to gitosis (by editing and pushing gitosis.conf) 

Then add remotes to project and get the empty project
$ git remote add origin git@dev.starzel.de:<projectname>.git
$ git pull origin master

Add buildout to remotes:
$ git remote add buildoutskel git@dev.starzel.de:buildout.git

Create branch buildout and checkout remote buildout master into the active local branch (buildout)
$ git b buildout 
$ git co buildout
$ git pull buildoutskel master

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
$ git pull buildoutskel master
$ git co master
$ git merge buildout