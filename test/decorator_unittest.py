#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  Quick-Typographie-Filter unit test: style_unittest.py

  (C)opyleft in 2018 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 28.03.2018 (nm) - Erste Version
  0.2   - 28.10.2018 (nm) - Ein weitere Test hinzugefügt.
  0.3   - 08.07.2019 (nm) - Code Refaktor


  WICHTIG:
  ========
    Benoetigt python3 !
    -> https://www.howtogeek.com/197947/how-to-install-python-on-windows/
    oder
    -> https://www.youtube.com/watch?v=dX2-V2BocqQ

  RUN THE TESTS:
  ==============
  Um die unit tests auszuführen kann man im Terminal den Befehl

    > python3 -m unittest test/decorator_unittest.py

  im Hauptverzeichnis des Projektes eingeben!

  Lizenz:
  =======
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  
  "Errare (Errasse) humanum est, sed in errare (errore) perseverare diabolicum."

    -- Cicero

'''

# import sys
import unittest

# sys.path.append('..')
from style import *
from decorator import *

class DecoratorTest(unittest.TestCase):

    def test_add_and_get_pre(self):
        pre = "xxx"
        dec = Decorator()
        dec.add_pre(pre)
        self.assertEqual(dec.get_pre(), pre)
        del dec
        

    def test_add_and_get_post(self):
        post = "xxx"
        dec = Decorator()
        dec.add_post(post)
        self.assertEqual(dec.get_post(), post)
        del dec
    
    def test_has_pre_post_false(self):
        dec = Decorator()
        self.assertFalse(dec.has_pre_post())
        del dec

    def test_has_pre_post_true(self):
        dec = Decorator()
        dec.add_pre("xxx")
        dec.add_post("yyy")
        self.assertTrue(dec.has_pre_post())
        del dec

    def test_handle_class_fontsize_latex(self):
        new_fontsize = "XXXXX"
        prepost_after = "{\\" + new_fontsize + "{}}"
        dec = LaTeXDecorator()
        dec.handle_class_fontsize(new_fontsize)
        self.assertEqual(dec.get_pre() + dec.get_post(), prepost_after)
        del dec


    def test_handle_class_fontfamily_latex(self):
        fontfamilies = {
            "normalfont": "normalfont",
            "romanfont": "rmfamily",
            "sansserif": "sffamily",
            "teletype": "ttfamily",
            "slanted": "slshape",
            "italic": "itshape",
            "smallcaps": "scshape",
            "upright": "upshape"}
            
        for new_fontfamily in fontfamilies:
            prepost_after = "{\\" + fontfamilies[new_fontfamily] + "{}}"
            dec = LaTeXDecorator()
            dec.handle_class_fontfamily(new_fontfamily)
            self.assertEqual(dec.get_pre() + dec.get_post(), prepost_after)
            del dec


if __name__ == "__main__":
    unittest.main()
