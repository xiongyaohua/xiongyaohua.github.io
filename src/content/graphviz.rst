================
Graphviz使用技巧
================

:date: 2014-02-18 02:21
:slug: graphviz-notes

本文记录使用Graphviz过程中发现的技巧和注意事项。

简介
====
Graphviz是一款绘制Graph的软件包。它的主要功能是通过某种算法自动排布
点线，以便清晰的展示graph的结构。

技巧
====
* 如何固定点的位置？

通过pos属性人工指定点的位置。同时使用neato排布引擎；其他引擎会
忽略人工指定的位置。::

    dot -Tpdf -Kneato expanded.viz

注意Graphviz中的长度单位默认为inch，一般来说位置坐标不应超过
5inch，否则生成图片尺寸太大。
