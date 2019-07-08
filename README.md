[![CircleCI](https://circleci.com/gh/NMarkgraf/style.py.svg?style=svg)](https://circleci.com/gh/NMarkgraf/style.py)
[![StyleCI](https://styleci.io/repos/126166922/shield?branch=master)](https://styleci.io/repos/126166922)
[![BCH compliance](https://bettercodehub.com/edge/badge/NMarkgraf/style.py?branch=master)](https://bettercodehub.com/)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Minimal Python needed: 3.5+](https://img.shields.io/badge/Python-3.5%2B-brightgreen.svg)](https://www.python.org)
[![CodeFactor](https://www.codefactor.io/repository/github/nmarkgraf/style.py/badge)](https://www.codefactor.io/repository/github/nmarkgraf/style.py)
[![ORCiD](https://img.shields.io/badge/ORCiD-0000--0003--2007--9695-green.svg)](https://orcid.org/0000-0003-2007-9695)


# style.py

Dies ist ein [pandoc](https://pandoc.org) Filter, geschrieben in [Python3](https://www.python.org) und basierend auf [panflute](https://github.com/sergiocorreia/panflute).

Er wandelt Ausdrücke wie 

```
::: {.center}
Das ist mittig!
:::
```

in LaTeX Ausdrücke wie

```
\begin{center}
Das ist mittig!
\end{center}
```
um.


Neu seit 0.4.5:

style.py unterstützt "cemph" und "cstrong":

```
Das ist eine farbige Hervorhebung: [Wichtig]{.cemph}!

Das ist eine sehr wichtige farbige Hervorhebung: [Extrem Wichtig]{.cstrong}!!!
```

In LaTeX:

```
Das ist eine farbige Hervorhebung: {\cemph{} Wichtig}!

Das ist eine sehr wichtige farbige Hervorhebung: {\cstrong{} Extrem Wichtig}!!!
```

Dazu müssen die Befehle "\cemph" und "\cstrong" in LaTeX definiert werden:

Mit
```
\newcommand*{\cemph}{\relax}
\newcommand*{\cstrong}{\relax}
```

kann man diese farbigen Herforhebungen deaktivieren. Mit

```
\newcommand*{\cemph}{\color{green}}
\newcommand*{\cstrong}{\color{red}}
```

wird der Text durch "\cemph" grün und mit "\cstrong" rot eingefärbt.


## Better Code Hub

Ich versuche diese Code bei 7+/10 zu halten. Mehr geht z.Z. auch kaum.
