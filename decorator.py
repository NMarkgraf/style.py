#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Quick-Typographie-Filter-Decorator-Class: decorator.py

  (C)opyleft in 2018 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 05.04.2018 (nm) - Erste Version
  0.2   - 27.03.2018 (nm) - Code (angeblich) "wartbarer" gemacht.
  0.2.1 - 14.06.2018 (nm) - Code noch "wartbarer" gemacht. ;-)
  0.2.2 - 27.06.2018 (nm) - Code etwas mehr kommentiert.


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


  PEP8 better pycodestyle
  =======================
    > pycodestyle decorator.py

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

"""

import panflute as pf  # panflute fuer den pandoc AST


class Decorator:
    FONTSIZECLASSES = (
        "tiny", "scriptsize", "footnotesize", "small",
        "normalsize", "large", "Large",
        "LARGE", "huge", "Huge")

    FONTFAMILYCLASSES = (
        "normalfont", "romanfont", "sansserif", "teletype",
        "italic", "smallcaps", "slanted", "upright")

    def __init__(self):
        """

        """
        self.pre = ""
        self.post = ""

    def addPrePost(self, prepost=("", "")):
        """

        :param prepost:
        :return:
        """
        self.addPre(prepost[0])
        self.addPost(prepost[1])

    def addPost(self, post):
        """

        :param post:
        :return:
        """
        self.post = post + self.post

    def addPre(self, pre):
        """

        :param pre:
        :return:
        """
        self.pre = self.pre + pre

    def getPre(self):
        """

        :return:
        """
        return self.pre

    def getPost(self):
        """

        :return:
        """
        return self.post

    def hasPre(self):
        """Do we have a 'pre' part?

        :return:
        """
        return self.pre != ""

    def hasPost(self):
        """Do we have a 'post' part?

        :return:
        """
        return self.post != ""

    def hasPrePost(self):
        """

        :return:
        """
        return self.hasPre() and self.hasPost()

    def handleClassCenter(self):
        """

        :return:
        """
        pass

    def handleClassFontsize(self, fontsize):
        """

        :param fontsize:
        :return:
        """
        pass

    def handleDivAndSpan(self, elem):
        """

        :param elem:
        :return:
        """
        pass


class LaTeXDecorator(Decorator):
    """
     Constants for (La)TeX
    """
    TEX_CENTER_BEFORE = """\n\\begin{center}\n"""
    TEX_CENTER_AFTER = """\n\\end{center}\n"""
    FORMAT = "latex"

    TEX_FONTFAMILY_TAG = {
        "normalfont": "normalfont",
        "romanfont": "rmfamily",
        "sansserif": "sffamily",
        "teletype": "ttfamily",
        "slanted": "slshape",
        "italic": "itshape",
        "smallcaps": "scshape",
        "upright": "upshape"}

    def handleClassCenter(self):
        """Add LaTeX center environment.
        """
        self.addPre(self.TEX_CENTER_BEFORE)
        self.addPost(self.TEX_CENTER_AFTER)

    def handleClassFontsize(self, fontsize):
        """Add new fontsize.

        :param fontsize:
        :return:
        """
        self.addPre("{\\" + fontsize + "{}")
        self.addPost("}")

    def handleClassFontfamily(self, fontfamily):
        """Add new fontfamily.

        :param fontfamily:
        :return:
        """
        self.addPre("{\\" + self.TEX_FONTFAMILY_TAG[fontfamily] + "{}")
        self.addPost("}")

    def getRawBlock(self, txt):
        """

        :param txt:
        :return:
        """
        return pf.RawBlock(txt, format=self.FORMAT)

    def getRawInline(self, txt):
        """

        :param txt:
        :return:
        """
        return pf.RawInline(txt, format=self.FORMAT)

    def getBeforeBlock(self):
        """

        :return:
        """
        if self.hasPrePost():
            return self.getRawBlock(self.getPre())

    def getBeforeInline(self):
        """

        :return:
        """
        if self.hasPrePost():
            return self.getRawInline(self.getPre())

    def getAfterBlock(self):
        """

        :return:
        """
        if self.hasPrePost():
            return self.getRawBlock(self.getPost())

    def getAfterInline(self):
        """

        :return:
        """
        if self.hasPrePost():
            return self.getRawInline(self.getPost())

    def handleClassJustifiedInDiv(self, alignment):
        """Handle classes with justified (left/right) in DIV blocks.

        :param alignment: "left" or "right"
        :return: None
        """
        if alignment == "left":
            self.addPre("\n\\begin{flushright}\n")
            self.addPost("\n\end{flushright}\n")

        if alignment == "right":
            self.addPre("\n\\begin{flushleft}\n")
            self.addPost("\n\end{flushleft}\n")

        if alignment == "center":
            self.handleClassCenter()
        pass

    def handleDiv(self, elem):
        """Handle DIV and SPAN Blocks in LaTeX Context.

        :param elem:
        :return:
        """
        if 'center' in elem.classes:
            self.handleClassCenter()

        if 'justifiedleft' in elem.classes:
            self.handleClassJustifiedInDiv("left")

        if 'justifiedright' in elem.classes:
            self.handleClassJustifiedInDiv("right")

    def handleIndexSpan(self, elem):
        """

        :param elm:
        :return:
        """
        self.addPre("")
        self.addPost("\\index{"+elem.attribute["index"]+"}")

    def handleSpan(self, elem):
        """Handle DIV and SPAN Blocks in LaTeX Context.

        :param elem:
        :return:
        """
        if elem.attribute["index"]:
            self.handleIndexSpan(elem)
        else:
            pass

    def handleDivAndSpan(self, elem):
        """Handle DIV and SPAN Blocks in LaTeX Context.

        :param elem:
        :return:
        """
        for fontsize in self.FONTSIZECLASSES:
            if fontsize in elem.classes:
                self.handleClassFontsize(fontsize)

        for fontfamily in self.FONTFAMILYCLASSES:
            if fontfamily in elem.classes:
                self.handleClassFontfamily(fontfamily)

        if 'Quelle' in elem.classes:
            self.handleClassFontsize("scriptsize")

        if 'Sinnspruch' in elem.classes:
            self.addPre("\n\\mode<all>\\begin{quote}\\small ")
            self.addPost("\\end{quote}\n\\mode<*>")


class HTMLDecorator(Decorator):
    """

    """
    pass


def main():
    """

    :return:
    """
    pass


"""
And, as always:
"""
if __name__ == "__main__":
    main()
