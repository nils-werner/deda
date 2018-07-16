import setuptools
from setuptools.command.sdist import sdist


if __name__ == "__main__":
    setuptools.setup(
        name='deda',

        version="0.1",

        description='tracking Dots Extraction, Decoding and Anonymisation toolkit',
        long_description="DEDA - tracking Dots Extraction, Decoding and Anonymisation toolkit",

        author='Timo Richter, Stephan Escher, Dagmar Schönfeld, Thorsten Strufe',
        author_email='timo.richter@tu-dresden.de',
        url='https://github.com/dfd-tud/deda',

        license='GPL3+',

        packages=setuptools.find_packages(),

        install_requires=[
            'numpy',
            'scipy',
            'opencv-python',
            'pillow',
        ],

        classifiers=[
            'Environment :: Console',
            'Operating System :: OS Independent',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Topic :: Utilities',
            'Topic :: Printing',
            'Topic :: Security',
        ],

        entry_points={'console_scripts': [
            'deda_anonmask_apply=deda.anonmask_apply:main',
            'deda_anonmask_create=deda.anonmask_create:main',
            'deda_clean_document=deda.clean_document:main',
            'deda_compare_prints=deda.compare_prints:main',
            'deda_parse_print=deda.parse_print:main',
            'deda_extract_yd=libdeda.extract_yd:main',
        ]},
    )
