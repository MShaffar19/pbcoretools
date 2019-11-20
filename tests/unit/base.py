
import subprocess
import unittest
import tempfile
import logging
import os.path as op
import os

TESTDATA = "/pbi/dept/secondary/siv/testdata/pbcoretools-unittest/data"

skip_if_no_testdata = unittest.skipUnless(
    op.isdir(TESTDATA), "Testdata not found")

log = logging.getLogger(__name__)


def _get_temp_file(suffix, dir_):
    t = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, dir=dir_)
    t.close()
    return t.name


def get_temp_file(suffix="", dir_=None):
    return _get_temp_file(suffix, dir_=dir_)


def get_temp_dir(suffix=""):
    """This will make subdir in the root tmp dir"""
    return tempfile.mkdtemp(dir=None, suffix=suffix)
