from fortlab import Fortlab

prj = Fortlab()

def test_basic():

    cmd = "input @1 --forward '@x=2'"
    ret = prj.main(cmd)

    assert ret == 0

def test_print(capsys):

    cmd = "-- input @1 --forward '@x=2' -- print @x @data[0]"
    ret = prj.main(cmd)

    assert ret == 0

    captured = capsys.readouterr()
    assert captured.out == "21\n"
    assert captured.err == ""
