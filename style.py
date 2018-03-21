#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
  Quick-Typographie-Filter: style.py

  (C)opyleft in 2018 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 21.03.2018 (nm) - Erste Version


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

  LaTeX:
  ======
  Der Befehl "xspace" benötigst das Paket "xspace".
  Also bitte "usepackage{xspace}" einbauen!
  Ab Version 0.6 wird von "\," auf "thinspace" umgestellt.

  Informationen zur Typographie:
  ==============================
  URL: https://www.korrekturen.de/fehler_und_stilblueten/die_sieben_haeufigsten_typographie-suenden.shtml
  URL: http://www.typolexikon.de/abstand/
  URL: https://de.wikipedia.org/wiki/Schmales_Leerzeichen


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


TEX_CENTER_BEFORE = """\n\\begin{center}\n"""
TEX_CENTER_AFTER = """\\end{center}\n"""


'''
 Eine Log-Datei "style.log" erzeugen um einfacher zu debuggen
'''
#logging.basicConfig(filename='style.log', level=logging.ERROR)
logging.basicConfig(filename='style.log', level=logging.DEBUG)

'''
\tiny, \scriptsize, \footnotesize, \small, \normalsize (default), \large, \Large, \LARGE, \huge and \Huge. 
'''

def action(e, doc):
    if (isinstance(e, pf.Span)) and ((doc.format == "latex") or (doc.format == "beamer")):
        beforeTeX = ""
        afterTeX = ""
 
        if 'Large' in e.classes:
            beforeTeX = beforeTeX+"{\\Large "
            afterTeX = "}"+afterTeX

        if 'LARGE' in e.classes:
            beforeTeX = beforeTeX+"{\\LARGE "
            afterTeX = "}"+afterTeX
            
        if 'huge' in e.classes:
            beforeTeX = beforeTeX+"{\\huge "
            afterTeX = "}"+afterTeX
            
        if 'normalsize' in e.classes:
            beforeTeX = beforeTeX+"{\\normalsize "
            afterTeX = "}"+afterTeX

        if 'small' in e.classes:
            beforeTeX = beforeTeX+"{\\small "
            afterTeX = "}"+afterTeX
            
        if 'footnotesize' in e.classes:
            beforeTeX = beforeTeX+"{\\footnotesize "
            afterTeX = "}"+afterTeX

        if 'scriptsize' in e.classes:
            beforeTeX = beforeTeX+"{\\scriptsize "
            afterTeX = "}"+afterTeX
            
        if 'tiny' in e.classes:
            beforeTeX = beforeTeX+"{\\tiny "
            afterTeX = "}"+afterTeX
         
        if beforeTeX != "":
            before = pf.RawInline(beforeTeX, format="latex")
            after = pf.RawInline(afterTeX, format="latex")
            e.content = [before] + list(e.content) + [after]
            return e
       
    if (isinstance(e, pf.Div)) and ((doc.format == "latex") or (doc.format == "beamer")):
        beforeTeX = ""
        afterTeX = ""
        if 'center' in e.classes:
            beforeTeX = beforeTeX+TEX_CENTER_BEFORE
            afterTeX =  TEX_CENTER_AFTER+afterTeX

        if 'Large' in e.classes:
            beforeTeX = beforeTeX+"{\\Large"
            afterTeX = "}"+afterTeX

        if 'LARGE' in e.classes:
            beforeTeX = beforeTeX+"{\\LARGE"
            afterTeX = "}"+afterTeX
            
        if 'huge' in e.classes:
            beforeTeX = beforeTeX+"{\\huge"
            afterTeX = "}"+afterTeX
            
        if 'normalsize' in e.classes:
            beforeTeX = beforeTeX+"{\\normalsize"
            afterTeX = "}"+afterTeX

        if 'small' in e.classes:
            beforeTeX = beforeTeX+"{\\small"
            afterTeX = "}"+afterTeX
            
        if 'footnotesize' in e.classes:
            beforeTeX = beforeTeX+"{\\footnotesize"
            afterTeX = "}"+afterTeX

        if 'scriptsize' in e.classes:
            beforeTeX = beforeTeX+"{\\scriptsize"
            afterTeX = "}"+afterTeX
            
        if 'tiny' in e.classes:
            beforeTeX = beforeTeX+"{\\tiny"
            afterTeX = "}"+afterTeX
         
        if beforeTeX != "":
            before = pf.RawBlock(beforeTeX, format="latex")
            after = pf.RawBlock(afterTeX, format="latex")
            e.content = [before] + list(e.content) + [after]
            return e
            
def main():
    logging.debug("Start style.py")
    pf.toJSONFilter(action=action)
    logging.debug("End style.py")


if __name__ == "__main__":
    main()
