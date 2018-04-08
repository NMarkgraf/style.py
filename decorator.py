#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
  Quick-Typographie-Filter-Decorator-Class: decorator.py

  (C)opyleft in 2018 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 05.04.2018 (nm) - Erste Version
  0.2   - 27.03.2018 (nm) - Code (angebolich) "Wartbarer"" gemacht.


  WICHTIG:
  ========
    Benoetigt python3 !
    -> https://www.howtogeek.com/197947/how-to-install-python-on-windows/
    oder
    -> https://www.youtube.com/watch?v=dX2-V2BocqQ
    Bei *nix und macOS Systemen muss diese Datei als "executable" markiert
    sein!
    Also bitte ein
      > chmod a+x style.py
   ausfuehren!


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

'''

import panflute as pf  # panflute fuer den pandoc AST


class Decorator:
    FONTSIZECLASSES = (
    "tiny", "scriptsize", "footnotesize", "small",
    "normalsize", "large", "Large",
    "LARGE", "huge", "Huge")
    
    def __init__(self):
        self.pre = ""
        self.post = ""

    def addPrePost(self, prepost=("", "")):
        self.addPre(prepost[0])
        self.addPost(prepost[1])

    def addPost(self, post):
        self.post = post + self.post

    def addPre(self, pre):
        self.pre = self.pre + pre

    def getPre(self):
        return self.pre

    def getPost(self):
        return self.post

    def hasPrePost(self):
        return (self.pre != "") and (self.post != "")

    def handleClassCenter(self):
        pass

    def handleClassFontsize(self, fontsize):
        pass
    
    def handleDivAndSpan(self, elem):
        pass


class LaTeXDecorator(Decorator):
    '''
     Constants for (La)TeX
    '''
    TEX_CENTER_BEFORE = """\n\\begin{center}\n"""
    TEX_CENTER_AFTER = """\n\\end{center}\n"""

    def handleClassCenter(self):
        '''
        Add center environment
        '''
        self.addPre(self.TEX_CENTER_BEFORE)
        self.addPost(self.TEX_CENTER_AFTER)

    def handleClassFontsize(self, fontsize):
        '''
         Add new Fontsize
        '''
        # logging.debug("Adding new fontsize '" + fontsize + "'.")
        self.addPre("{\\" + fontsize + "{}")
        self.addPost("}")

    def getBeforeBlock(self):
        if self.hasPrePost():
            return pf.RawBlock(self.getPre(), format="latex")

    def getBeforeInline(self):
        if self.hasPrePost():
            return pf.RawInline(self.getPre(), format="latex")

    def getAfterBlock(self):
        if self.hasPrePost():
            return pf.RawBlock(self.getPost(), format="latex")

    def getAfterInline(self):
        if self.hasPrePost():
            return pf.RawInline(self.getPost(), format="latex")

    def handleDivAndSpan(self, elem):
        '''
         Handle DIV and SPAN Blocks in LaTeX Context
        '''
        if 'center' in elem.classes:
            self.handleClassCenter()
    
        for fontsize in self.FONTSIZECLASSES:
            if fontsize in elem.classes:
                self.handleClassFontsize(fontsize)

        if 'Quelle' in elem.classes:
             self.handleClassFontsize("scriptsize")
    
        if 'Sinnspruch' in elem.classes:
            self.addPre("\n\\mode<all>\\begin{quote}\\small ")
            self.addPost("\\end{quote}\n\\mode<*>")


class HTMLDecorator(Decorator):
    pass
