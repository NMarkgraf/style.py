[![BCH compliance](https://bettercodehub.com/edge/badge/NMarkgraf/style.py?branch=master)](https://bettercodehub.com/)

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

