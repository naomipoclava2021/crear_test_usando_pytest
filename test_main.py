import pytest
from main import escribir

def test_tmp_dir(tmpdir):
    fpath=f"{tmpdir}/test.txt"
    data_in="Hola mundo"
    escribir(fpath, data_in)

    with open(fpath) as file_out:
        data_out=file_out.read()
    assert data_in == data_out