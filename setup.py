from setuptools import setup

with open("README.md", "r") as f:
    long_description = "\n".join(f.readlines())

setup(name='pyqrtray',
      version='0.0.1',
      description=u"",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"André-Patrick Bubel",
      author_email=u"code@andre-bubel.de",
      url='https://github.com/mapbox/pyskel',
      license='GPL-3+',
      install_requires=[
          "pygobject",
          "qrcode",
      ],
      )
