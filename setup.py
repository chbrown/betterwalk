"""Run "python setup.py install" to install BetterWalk."""

from distutils.core import setup

import betterwalk

setup(
    name='BetterWalk',
    version=betterwalk.__version__,
    author='Ben Hoyt',
    author_email='benhoyt@gmail.com',
    url='https://github.com/benhoyt/betterwalk',
    license='New BSD License',
    description='BetterWalk, a better and faster os.walk() for Python',
    long_description="""BetterWalk is a somewhat better and significantly faster version of Python's os.walk(), as well as a generator version of os.listdir(). Read more at the GitHub project page.""",
    py_modules=['betterwalk'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System',
    ]
)
