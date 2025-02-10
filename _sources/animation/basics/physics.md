# 物理动态

````{subfigure} AB|CD|EF
:layout-sm: A|B|C|D|E|F
:gap: 8px
:subcaptions: below
:name: fig-animation-basics-physics_demo
:width: 100 %

```{image} fig/animation-basics-rigid_demo.png
:alt: 刚体模拟
```

```{image} fig/animation-basics-elastic_demo.png
:alt: 弹性体模拟
```

```{image} fig/animation-basics-thinshell_demo.png
:alt: 布料模拟
```

```{image} fig/animation-basics-fluid_demo.png
:alt: 烟雾模拟
```

```{image} fig/animation-basics-magnetic_demo.png
:alt: 磁流体模拟
```

```{image} fig/animation-basics-surfacetension_demo.png
:alt: 流体表面现象模拟
```

各种物理现象的模拟
````

我们生活在一个物理世界当中，万物的运动都遵循着相应的物理原理。物理现象在我们身边随处可见，它们多种多样，包括刚体现象、软体现象、流体现象、薄壳现象、磁现象等等。在物理学科漫长的发展史上，人类已经探索出大多数现象的物理方程，这些方程精确描述了物体的运动，为我们解释了自然界中各种现象的规律。

然而，仅仅拥有物理方程不足以让我们完全理解这个世界，因为这些方程往往过于复杂而难以求解，甚至不存在一种数学表达形式来描述它的解；1929 年，英国著名量子物理学家保罗·狄拉克（Paul Dirac）曾说过，“大部分物理学和整个化学的数学理论所需的基本物理定律是完全已知的，困难只是这些定律的确切应用导致方程太复杂而无法解决”。

> jr: 这句话可以在知乎上找到（https://zhuanlan.zhihu.com/p/407366845）。

正是因为绝大多数物理方程难以精确求解，人们开始退而求其次，选择求解一个数值近似解来大致地理解某一种现象的运动规律。并且，我们往往还要求这个数值近似解能够随着计算量的增大尽可能逼近真实解。这样，我们就可以将不可解的问题转化为计算量巨大的近似问题，并交给计算机去做了。于是，物理模拟就这样诞生了。

除了辅助研究物体的运动规律，物理模拟还有着丰富的应用场景。在工程实验上，我们可以借助计算机模拟飞行器的风洞试验、材料的抗压测试等；在机器人学与具身智能领域，人们往往会搭建一个物理模拟环境用来测试一个机器人控制算法，从而避免实机测试所造成的损坏；我们还可以根据气象数据对天气或气候进行建模并模拟，以做出较准确的天气预报……在图形学中，物理模拟能够帮助我们生成电影、游戏甚至元宇宙中更加真实的动画效果。为追求更真实的现象、更高的计算效率以及更复杂现象的模拟，已有大量的研究成果被发表。{numref}`fig-animation-basics-physics_demo` 展示了一些工作对各种现象的模拟。

我们将在接下来的章节中介绍自然界中最常见的几种物理现象的模拟方法，包括弹性体模拟（{numref}`chap-animation-elastomers`）、刚体模拟（{numref}`chap-animation-rigid_bodies`）和流体模拟（{numref}`chap-animation-fluids`）。