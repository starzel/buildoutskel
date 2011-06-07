import urllib, tarfile, os, sys

from zc.buildout import buildout

def main():
    try:
        base_path = sys.argv[1]
    except IndexError:
        print """
Usage: gs_download <path_to_buildout>

This tool assumes in the path to the buildout lies a buildout.cfg and tries
to parse it with the buildout parser.
It assumes these minimum information in the buildout:

[buildout]
localip = # 127.0.0.1
plonefolder = # Plone # The Plone folder generated when creating a plone site
login = # admin # The admin login name
password = # admin # The admin password
[ports]
instance = # 8080 # The tcp port on which a zope instance is listening on

It will always untgz the full genericsetup export in the buildout subdirectory
gs. The gs directory is not meant for versioning customizations, please
use your products profiles for that. The gs directory is just a security
mechanism to check that any configuration change that happens to get tracked by
genericsetup, gets documented in some form.
This script assumes that the full buildout directory is under 
git version control, including the gs directory.

This script returns it results only to the console. If everything is fine, 
nothing will be returned. The script is meant to be run by cron, which 
automatically sends mails when any of its programs produce any form of output.
"""
        sys.exit(1)
    # We use buildout internal api and just experimented until we get the 
    # desired results.
    config = buildout._open("", os.path.join(base_path, "buildout.cfg"), 
                            [], {}, {})

    url = ("http://%s:%s/%s/portal_setup/manage_exportSteps/"
           "manage_exportAllSteps?__ac_name=%s&__ac_password=%s") % (
        config['buildout']['localip'][0],
        config['ports']['instance'][0],
        config['buildout']['plonefolder'][0],
        config['buildout']['login'][0],
        config['buildout']['password'][0]
        )

    tgz = tarfile.TarFile.open(fileobj=urllib.urlopen(url), mode='r|gz')
    tgz.extractall(os.path.join(base_path, "gs"))
    os.system('git diff')
    os.system('git status')
