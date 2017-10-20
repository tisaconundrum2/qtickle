from setuptools import setup, find_packages

from qtickle import __version__

if __name__ == '__main__':
    setup(
        zip_safe=False,
        name='Qtickle',
        version=__version__,
        author='Nicholas Finch',
        author_email='tisaconundrum@github',
        packages=find_packages(),
        url='https://github.com/tisaconundrum2/qtickle',
        description="""
        A script designed to aid in saving values inside Qt objects.
        It works by inspecting for object names and then collecting their
        values.
        """,

    )
