#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.build_py import build_py
from pyqt_distutils.build_ui import build_ui
cmdclass = {"build_ui": build_ui}

class CustomBuildPy(build_py):
    def run(self):
        self.run_command('build_ui')
        build_py.run(self)

cmdclass['build_py'] = CustomBuildPy

setup(
    name="plover_dictionary_builder",
    version="0.0.1",
    description="Build up a steno dictionary from text content",
    author="Ted Morin",
    author_email="morinted@gmail.com",
    license="GPLv2+",
    install_requires=[
        "plover>=4.0.0.dev0",
    ],
    packages=[
        'dictionary_builder',
    ],
    include_package_data=True,
    entry_points="""
    [plover.gui.qt.tool]
    dictionary_builder = dictionary_builder.dictionary_builder:DictionaryBuilder
    """,
    cmdclass=cmdclass,
    setup_requires = [
        'setuptools-scm',
    ],
    zip_safe=True,
)
