---
title: "Ein kleiner Test"
author: "Norman Markgraf"
date: "18 Dezember 2017"
output: 
    beamer_presentation:
        keep_tex: true
        includes:
            in_header: 
                - header.tex
        pandoc_args:
            - --filter
            - ../style.py
---

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
