# -*- coding: utf8 -*-
from setuptools import setup

with open("README.md", "r") as f:
    long_description = "\n".join(f.readlines())

setup(name='qrtray',
      version='0.0.1',
      description=u"Shows the current clipboard content as a QR code",
      long_description=long_description,
      classifiers=[],
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
              'pyqrtray = pyqrtray.pyqrtray:main',
          ]
      }
      )
