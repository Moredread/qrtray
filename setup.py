# -*- coding: utf8 -*-
#from setuptools import setup

#Adapted from https://wiki.gnome.org/Projects/PyGObject?action=AttachFile&do=view&target=setup.py
import os, site, sys
try:
    from cx_Freeze import setup, Executable
    cx = True
except ImportError:
    from setuptools import setup
    cx = False

## Get the site-package folder, not everybody will install
## Python into C:\PythonXX
site_dir = site.getsitepackages()[1]
include_dll_path = os.path.join(site_dir, "gnome")

## Collect the list of missing dll when cx_freeze builds the app
## Actually used DLLs found out with https://technet.microsoft.com/en-us/sysinternals/bb896656.aspx
missing_dll = [
    'libgirepository-1.0-1.dll',
    'libffi-6.dll',
    'libglib-2.0-0.dll',
    'libgobject-2.0-0.dll',
    'libgio-2.0-0.dll',
    'libgmodule-2.0-0.dll',
    'libwinpthread-1.dll',
    'libintl-8.dll',
    'libzzz.dll',
    'libgtk-3-0.dll',
    'libgdk-3-0.dll',
    'libatk-1.0-0.dll',
    'libcairo-gobject-2.dll',
    'libepoxy-0.dll',
    'libgdk_pixbuf-2.0-0.dll',
    'libpango-1.0-0.dll',
    'libpangocairo-1.0-0.dll',
    'libpangowin32-1.0-0.dll',
    'libfontconfig-1.dll',
    'libfreetype-6.dll',
    'libpng16-16.dll',
    'libpangoft2-1.0-0.dll',
    'libharfbuzz-0.dll',
    'libjasper-1.dll',
    'libjpeg-8.dll',
    'librsvg-2-2.dll',
    'libtiff-5.dll',
    'libwebp-5.dll',
    'libxmlxpat.dll',
]

## We also need to add the glade folder, cx_freeze will walk
## into it and copy all the necessary files
#glade_folder = 'glade'

# Not sure if this is all
gtk_libs = ['lib/gdk-pixbuf-2.0',
            'lib/girepository-1.0',
            'lib/gtk-3.0',
            'share/glib-2.0',
            'share/icons',
            'share/fonts',
            'share/themes',
            'etc',
]

## Create the list of includes as cx_freeze likes
include_files = []
for dll in missing_dll:
    include_files.append((os.path.join(include_dll_path, dll), dll))

## Let's add glade folder and files
#include_files.append((glade_folder, glade_folder))

## Let's add gtk libraries folders and files
for lib in gtk_libs:
    include_files.append((os.path.join(include_dll_path, lib), lib))

base = None

## Lets not open the console while running the app
if sys.platform == "win32":
    base = "Win32GUI"

if cx == True:
    executables = [
        Executable(
            "qrtray/qrtray.py",
            base=base
        )
    ]
else:
    executables = []

buildOptions = dict(
    compressed = True,
    includes = ["gi"],
    packages = ["gi"],
    include_files = include_files
    )

with open("README.md", "r") as f:
    long_description = "".join(f.readlines())

setup(name='qrtray',
      version='1.0.0',
      description=u"Shows the current clipboard content as a QR code",
      long_description=long_description,
      classifiers=["Environment :: X11 Applications :: GTK",
                   "Environment :: Win32 (MS Windows)",
                   "Development Status :: 2 - Pre-Alpha",
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
      author=u"André-Patrick Bubel" if "bdist_msi" not in sys.argv else "Andre-Patrick Bubel",
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
      options = dict(build_exe = buildOptions),
      executables = executables
)
