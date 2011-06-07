from setuptools import setup

setup(
    name="gs_download",
    version="0.1",
    install_requires="zc.buildout",
    entry_points = """
    [console_scripts]
    gs_download = gs_download:main
    """
    )
