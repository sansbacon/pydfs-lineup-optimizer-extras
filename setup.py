# pydfs_lineup_optimizer_extras/setup.py
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Eric Truett
# Licensed under the MIT License


from setuptools import setup, find_packages

PACKAGE_NAME = "pydfs-lineup-optimizer-extras"


def run():
    setup(name=PACKAGE_NAME,
          version="0.1",
          description="python library for pydfs-lineup-optimizer utility functions",
          author="Eric Truett",
          author_email="eric@erictruett.com",
          license="MIT",
          packages=find_packages(),
          zip_safe=False)


if __name__ == '__main__':
    run()
