
from os import path as op
from pbcore.util.Process import backticks

def _check_constools():
    cmd = "pbmerge"
    o, r, m = backticks(cmd)
    if r != 1:
        return False

    cmd = "dataset"
    o, r, m = backticks(cmd)
    if r != 2:
        return False

    cmd = "pbindex"
    o, r, m = backticks(cmd)
    if r != 1:
        return False

    cmd = "samtools"
    o, r, m = backticks(cmd)
    if r != 1:
        return False
    return True

def _internal_data():
    if op.exists("/pbi/dept/secondary/siv/testdata"):
        return True
    return False