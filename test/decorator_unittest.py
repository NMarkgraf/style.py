#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  Quick-Typographie-Filter unit test: style_unittest.py

  (C)opyleft in 2018 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 28.03.2018 (nm) - Erste Version
  0.2   - 28.10.2018 (nm) - EIn weitere Test hinzugefügt.


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

    def test_addAndgetPre(self):
        pre = "xxx"
        dec = Decorator()
        dec.addPre(pre)
        self.assertEqual(dec.getPre(), pre)
        del dec
        

    def test_addAndgetPost(self):
        post = "xxx"
        dec = Decorator()
        dec.addPost(post)
        self.assertEqual(dec.getPost(), post)
        del dec
    
    def test_hasPrePostFalse(self):
        dec = Decorator()
        self.assertFalse(dec.hasPrePost())        
        del dec

    def test_hasPrePostTrue(self):
        dec = Decorator()
        dec.addPre("xxx")
        dec.addPost("yyy")
        self.assertTrue(dec.hasPrePost())        
        del dec

    def test_handleClassFontsizeLaTeX(self):
        newFontsize = "XXXXX"
        prepostAfter = "{\\" + newFontsize + "{}}"
        dec = LaTeXDecorator()
        dec.handleClassFontsize(newFontsize)
        self.assertEqual(dec.getPre()+dec.getPost(), prepostAfter)
        del dec

    def test_handleClassSolution(self):
        prepostAfter = "\\solitionSpace[2-]{}"
        dec = LaTeXDecorator()
        dec.handleClassSolution()
        self.assertEqual(dec.getPre()+dec.getPost(), prepostAfter)
        del dec

    def test_handleClassSolutionTwo(self):
        prepostAfter = "\\solitionSpace[3-]{}"
        dec = LaTeXDecorator()
        dec.handleClassSolution(type="3-")
        self.assertEqual(dec.getPre()+dec.getPost(), prepostAfter)
        del dec


    def test_handleClassFontfamilyLaTeX(self):
        fontfamilies = {
            "normalfont": "normalfont",
            "romanfont": "rmfamily",
            "sansserif": "sffamily",
            "teletype": "ttfamily",
            "slanted": "slshape",
            "italic": "itshape",
            "smallcaps": "scshape",
            "upright": "upshape"}
            
        for newFontfamily in fontfamilies:
            prepostAfter = "{\\" + fontfamilies[newFontfamily] + "{}}"
            dec = LaTeXDecorator()
            dec.handleClassFontfamily(newFontfamily)
            self.assertEqual(dec.getPre()+dec.getPost(), prepostAfter)
            del dec


if __name__ == "__main__":
    unittest.main()
