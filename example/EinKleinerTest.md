---
title: "Ein kleiner Test"
author: "Norman Markgraf"
date: "18 Dezember 2017"
output:
  beamer_presentation:
    includes:
      in_header: header.tex
    keep_tex: yes
    md_extensions: +raw_tex+header_attributes+fenced_divs+bracketed_spans
    pandoc_args:
    - --filter
    - ../style.py
    slide_level: 2
  slidy_presentation: 
    slide_level: 2
    css: ../css/style-py.css
  ioslides_presentation: 
    slide_level: 2
    css: ../css/style-py.css
  html_document:
    css: ../css/style-py.css
---

# Test

## Ein paar Testsenarien

::: {.center}
Das ist mittig!
:::

Das ist normaler Text!

::: {.Large}
Das ist GROSS!
:::

Das ist normaler Text!

::: {.Large .center}
Das ist GROSS!
:::

Das ist normaler Text!


::: {.center .LARGE}
Das ist GROSS!
:::

Das ist normaler Text!


## Nun Spans statt Divs

Das ist [ein kleiner]{.small} [GROSSER]{.Large} Test!


## Alle auf einer Seite:

[tiny]{.tiny} [scriptsize]{.scriptsize} [footnotesize]{.footnotesize} [small]{.small}
(default) [normalsize ]{.normalsize} [large]{.Large} [Large]{.Large} [huge]{.huge} [Huge]{.Huge}

[normal]{.normalfont} [roman]{.romanfont} [sanserif]{.sansserif} [teletype]{.teletype} [smallcaps]{.smallcaps}
[slanted]{.slanted} [upright]{.upright} [italic]{.italic}

# Nun einmal ein Sinnspruch im Section-Title!

::: {.Sinnspruch}
Das hier ist ein Sinnspruch und sollte als solcher.

Auch genau so behandelt werden.

[-- Norman Markgraf]{.Quelle}
:::


## Ein Sinnspruch im normalen Frame

::: {.Sinnspruch}
Das hier ist ein Sinnspruch und sollte als solcher.

Auch genau so behandelt werden.

[-- Norman Markgraf]{.Quelle}
:::
