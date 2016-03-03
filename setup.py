# -*- coding: utf8 -*-
from setuptools import setup

with open("README.md", "r") as f:
    long_description = "".join(f.readlines())

setup(name='qrtray',
      version='1.0.1',
      description=u"Shows the current clipboard content as a QR code",
      long_description=long_description,
      classifiers=["Environment :: X11 Applications :: GTK",
                   "Environment :: Win32 (MS Windows)",
                   "Development Status :: 4 - Beta",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
                   "Natural Language :: English",
                   "Operating System :: Microsoft",
                   "Operating System :: POSIX :: Linux",
                   "Programming Language :: Python",
                   "Topic :: Text Processing",
                   "Topic :: Utilities"
                   ],
      keywords='',
      author=u"André-Patrick Bubel",
      author_email=u"code@andre-bubel.de",
      url='https://github.com/Moredread/qrtray',
      license='GPL-3+',
      install_requires=[
          "pygobject",
          "qrcode",
      ],
      entry_points={
          'gui_scripts': [
              'qrtray = qrtray.qrtray:main',
          ]
      },
)
