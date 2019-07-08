---
title: "Ein kleiner Test"
subtitle: "Dokumenten-Fassung"
author: "Norman Markgraf"
date: "08 Juli 2019"
header-includes:
  - "`\\usepackage{xcolor}`{=latex}"
  - "`\\newcommand{\\cemph}{\\color{green}}`{=latex}"
  - "`\\newcommand{\\cstrong}{\\color{red}}`{=latex}"
output:
 pdf_document:
    keep_tex: yes
    md_extensions: +raw_tex+header_attributes+fenced_divs+bracketed_spans
    pandoc_args:
    - --filter
    - ../style.py
---

# Test

## Ein paar Testszenarien (DIV-Blöcke)

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

Das ist [ein sehr kleiner]{.tiny}, [kleiner]{.small} und [ein GROSSER]{.Large} Test!

Manchmal möchte man [klein und grün]{.scriptsize .cemph} und [groß und rot]{.cstrong .huge} schreiben.


## Alle auf einer Seite:

[tiny]{.tiny} [scriptsize]{.scriptsize} [footnotesize]{.footnotesize} [small]{.small}
(default) [normalsize ]{.normalsize} [large]{.Large} [Large]{.Large} [huge]{.huge} [Huge]{.Huge}

[normal]{.normalfont} [roman]{.romanfont} [sanserif]{.sansserif} [teletype]{.teletype} [smallcaps]{.smallcaps}
[slanted]{.slanted} [upright]{.upright} [italic]{.italic}

## Justified Alignments

All small:

::: {.small}
Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können.

Justified Left:

::: {.justifiedleft}
Um ein triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um Vorteile daraus zu ziehen? Aber wer hat irgend ein Recht, einen Menschen zu tadeln, der die Entscheidung trifft, eine Freude zu genießen, die keine unangenehmen Folgen hat, oder einen, der Schmerz vermeidet, welcher keine daraus resultierende Freude nach sich zieht? 
:::

Justified Right:

::: {.justifiedright}
Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur, weil er Schmerz ist, es sei denn, es kommt zu zufälligen Umständen, in denen Mühen und Schmerz ihm große Freude bereiten können. Um ein triviales Beispiel zu nehmen, wer von uns unterzieht sich je anstrengender körperlicher Betätigung, außer um Vorteile daraus zu ziehen? 
:::

Normal, but small:

Aber wer hat irgend ein Recht, einen Menschen zu tadeln, der die Entscheidung trifft, eine Freude zu genießen, die keine unangenehmen Folgen hat, oder einen, der Schmerz vermeidet, welcher keine daraus resultierende Freude nach sich zieht?Auch gibt es niemanden, der den Schmerz an sich liebt, sucht oder wünscht, nur,

:::

## Lücken für Lösungen

Berechnen Sie die folgenden Aufgaben:

- $1+2+3+4=\;$[$10$]{.solution type=2-}
- $2+3+4+5=\;$[$14$]{.solution type=3-}

