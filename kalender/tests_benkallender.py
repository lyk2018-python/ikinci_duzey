import unittest
import io
import datetime
from unittest import mock

import benkallender


class KalenderTests(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input')
    def test_anamenu(self, fake_input, fake_stdout):
        dun = (datetime.date.today() - datetime.timedelta(days=1))
        bugun = datetime.date.today()
        fake_input.return_value = dun.isoformat()

        donen_tarih = benkallender.anamenu()

        cikti = fake_stdout.getvalue()

        self.assertIn(bugun.isoformat(), cikti)
        self.assertIn(dun.isoformat(), cikti)
        self.assertIn("Hafta Sayısı: {}".format(dun.isocalendar()[1]), cikti)
        self.assertIn("EU Standart: {g}/{a}/{y}".format(y=dun.year, a=dun.month, g=dun.day), cikti)
        self.assertEqual(4, len(cikti.splitlines()))
        self.assertEqual(dun, donen_tarih)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input')
    def test_anamenu2(self, fake_input, fake_stdout):
        dun = (datetime.date.today() - datetime.timedelta(days=1))
        bugun = datetime.date.today()
        fake_input.return_value = dun.isoformat()

        donen_tarih = benkallender.anamenu2()

        cikti = fake_stdout.getvalue()

        self.assertIn(bugun.isoformat(), cikti)
        self.assertIn(dun.isoformat(), cikti)
        self.assertIn("Hafta Sayısı: {}".format(dun.isocalendar()[1]), cikti)
        self.assertIn("EU Standart: {g}/{a}/{y}".format(y=dun.year, a=dun.month, g=dun.day), cikti)
        self.assertEqual(4, len(cikti.splitlines()))
        self.assertEqual(dun, donen_tarih)
