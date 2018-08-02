import unittest
import io
from unittest import mock

import eles


class ElesTests(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_eles_bos(self, fake_stdout):
        eles.eles()
        import os
        files = [f for f in os.listdir(".") if not f.startswith(".")] + [""]

        cikti = fake_stdout.getvalue()
        cikti = cikti.split("\n")
        self.assertListEqual(cikti, files)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_eles_tekil(self, fake_stdout):
        eles.eles("..")
        import os
        files = [os.path.join("..", f) for f in os.listdir("..") if not f.startswith(".")] + [""]

        cikti = fake_stdout.getvalue()
        cikti = cikti.split("\n")
        self.assertListEqual(cikti, files)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_eles_cogul(self, fake_stdout):
        eles.eles(".", "..")
        import os
        files1 = [f for f in os.listdir(".") if not f.startswith(".")] + [""]
        files2 = [""] + [os.path.join("..", f) for f in os.listdir("..") if not f.startswith(".")] + [""]

        cikti = fake_stdout.getvalue()
        self.assertIn("---", cikti)
        cikti1, cikti2 = cikti.split("---")
        cikti1 = cikti1.split("\n")
        cikti2 = cikti2.split("\n")

        self.assertListEqual(cikti1, files1)
        self.assertListEqual(cikti2, files2)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_elesl(self, fake_stdout):
        eles.eles(l=True)  # noqa: E741
        import os
        import pwd
        import grp
        files = os.listdir(".")
        fmt = "{uname}\t{grp}\t{size}\t{fname}"
        data = []
        for f in files:
            if not f:
                data.append("")
                continue
            datum = {
                "uname": pwd.getpwuid(os.stat(f).st_uid).pw_name,
                "grp": grp.getgrgid(os.stat(f).st_uid).gr_name,
                "size": os.path.getsize(f),
                "fname": f
            }
            data.append(fmt.format(**datum))
        data.append("")

        cikti = fake_stdout.getvalue()
        cikti = cikti.split("\n")
        self.assertListEqual(cikti, data)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_elesa(self, fake_stdout):

        eles.eles(a=True)  # noqa: E741
        import os
        files = [".", ".."] + os.listdir(".") + [""]

        cikti = fake_stdout.getvalue()
        cikti = cikti.split("\n")
        self.assertListEqual(cikti, files)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_elesla(self, fake_stdout):
        eles.eles(l=True, a=True)  # noqa: E741
        import os
        import pwd
        import grp
        files = [".", ".."] + os.listdir(".") + [""]
        fmt = "{uname}\t{grp}\t{size}\t{fname}"
        data = []
        for f in files:
            if not f:
                data.append("")
                continue
            datum = {
                "uname": pwd.getpwuid(os.stat(f).st_uid).pw_name,
                "grp": grp.getgrgid(os.stat(f).st_uid).gr_name,
                "size": os.path.getsize(f),
                "fname": f
            }
            data.append(fmt.format(**datum))

        cikti = fake_stdout.getvalue()
        cikti = cikti.split("\n")
        self.assertListEqual(cikti, data)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_elesla_tekil(self, fake_stdout):
        eles.eles("..", l=True, a=True)  # noqa: E741
        import os
        import pwd
        import grp
        files = [".", ".."] + os.listdir("..")
        fmt = "{uname}\t{grp}\t{size}\t{fname}"
        data = []
        for f in files:
            if f not in (".", ".."):
                f = os.path.join("..", f)
            if not f:
                data.append("")
                continue
            datum = {
                "uname": pwd.getpwuid(os.stat(f).st_uid).pw_name,
                "grp": grp.getgrgid(os.stat(f).st_uid).gr_name,
                "size": os.path.getsize(f),
                "fname": f
            }
            data.append(fmt.format(**datum))

        data.append("")
        cikti = fake_stdout.getvalue()
        cikti = cikti.split("\n")
        self.assertListEqual(cikti, data)
