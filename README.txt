This is a skeleton for a buildout used by starzel

Creating a project
==================

create a project-dir and add it to git
$ mkdir projectname
$ cd  projectname
$ git init

Add project to gitosis. Then add remote to project
$ git remote add buildout git@dev.starzel.de:<projectname>.git

Add buildout to remotes:
$ git remote add buildout git@dev.starzel.de:buildout.git

Create branch buildout and checkout remote buildout master into the active local branch (buildout)
$ git b buildout 
$ git co buildout
$ git pull buildout master

switch back to master and merge branch buildout into master
$ git co master
$ git merge buildout

Push changes into project-repo
$ git push origin

Go an with your work and push your work to origin. Don't ever push to remote buildout



Updating a project
==================
