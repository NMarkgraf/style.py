#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
  Quick-Typographie-Filter: style.py

  (C)opyleft in 2018 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 21.03.2018 (nm) - Erste Version
  0.2   - 25.03.2018 (nm) - Code (angebolich) "Wartbarer"" gemacht.


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
import re as re  # re fuer die Regulaeren Ausdruecke
import logging  # logging fuer die 'typography.log'-Datei

'''
  Constans for PrePost Strings
'''
PRE = 0
POST = 1

'''
 Constants for (La)TeX
'''
TEX_CENTER_BEFORE = """\n\\begin{center}\n"""
TEX_CENTER_AFTER = """\\end{center}\n"""

'''
 Eine Log-Datei "style.log" erzeugen um einfacher zu debuggen
'''
DEBUGLEVEL = logging.ERROR  # .ERROR or .DEBUG  or .INFO
logging.basicConfig(filename='style.log', level=DEBUGLEVEL)

'''
 LaTeX Fontsize commands in beamer:
 \tiny, \scriptsize, \footnotesize, \small, \normalsize (default),
 \large, \Large, \LARGE, \huge and \Huge.

 Handle Classes ".tiny", ".scriptsize", ".footnotesize", ".small",
                ".normalsize" (default), "large", ".Large",
                ".LARGE", ".huge"" and ".Huge".
'''
FONTSIZECLASSES = (
    "tiny", "scriptsize", "footnotesize", "small",
    "normalsize", "large", "Large",
    "LARGE", "huge", "Huge")


def addToPrePost(prepost=("", ""), pre="", post=""):
    '''
     Add Strings to PrePost Tupple
    '''
    return (prepost[PRE]+pre, post+prepost[POST])


def handleFontSize(fontsize="", prepost=("", "")):
    '''
     Add new Fontsize
    '''
    logging.debug("Adding new fontsize '" + fontsize + "'.")
    return addToPrePost(prepost, "{\\"+fontsize+"{}", "}")


def handleCenterClass(prepost):
    '''
     Handle center class
    '''
    logging.debug("Adding center enviroment.")
    return addToPrePost(prepost, TEX_CENTER_BEFORE, TEX_CENTER_AFTER)


def handleDivAndSpanLaTeX(e, prepost):
    '''
     Handle DIV and SPAN Blocks in LaTeX Context
    '''
    if 'center' in e.classes:
        prepost = handleCenterClass(prepost)

    for fontsize in FONTSIZECLASSES:
        if fontsize in e.classes:
            prepost = handleFontSize(fontsize, prepost)

    if 'Quelle' in e.classes:
        prepost = addToPrePost(prepost, "{\\scriptsize ", "}")

    if 'Sinnspruch' in e.classes:
        prepost = addToPrePost(
            prepost,
            "\n\\mode<all>\\begin{quote}\\small ",
            "\\end{quote}\n\\mode<*>")
    return prepost


def handleDivAndSpan(e, doc):
    '''
     Handle DIV and SPAN Blocks in gerneral
    '''
    if (doc.format in ["latex", "beamer"]):
        prepost = handleDivAndSpanLaTeX(e, ("", ""))

        if prepost != ("", ""):
            if isinstance(e, pf.Div):
                before = pf.RawBlock(prepost[PRE], format="latex")
                after = pf.RawBlock(prepost[POST], format="latex")

            if isinstance(e, pf.Span):
                before = pf.RawInline(prepost[PRE], format="latex")
                after = pf.RawInline(prepost[POST], format="latex")

            e.content = [before] + list(e.content) + [after]
            return e


def handleHeaderLevelOne(e, doc):
    '''
     Future work!
    '''
    if isinstance(e.next, pf.Div) and ("Sinnspruch" in e.next.classes):
        logging.debug("We have work to do!")


def action(e, doc):
    '''
     Main action function for panflute
    '''
    if isinstance(e, pf.Header) and (e.level == 1):
        return handleHeaderLevelOne(e, doc)

    if isinstance(e, pf.Span) or isinstance(e, pf.Div):
        return handleDivAndSpan(e, doc)


def main():
    '''
     main function
    '''
    logging.debug("Start style.py")
    pf.toJSONFilter(action=action)
    logging.debug("End style.py")


'''
 as always
'''
if __name__ == "__main__":
    main()
