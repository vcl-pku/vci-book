(chap-getting-started-drawing-2d)=
# 绘图

```{figure} fig/mondrian.jpg
:name: fig-started-drawing-mondrian
:width: 70%

Mondrian, Piet. "Composition with Red, Blue and Yellow". 1930, Kunsthaus Zürich[^mondrian]
```
[^mondrian]: [Wikipedia: Composition with Red, Blue and Yellow](https://en.wikipedia.org/wiki/Composition_with_Red,_Blue_and_Yellow)

在前面两节里，我们了解屏幕显示的原理和颜色的基础知识，相当于我们现在已经有了纸和颜料，可以开始画点东西了。为了循序渐进，我们将从画直线开始，然后是三角形，多边形，乃至后面学习的曲线与曲面。这些算法是数字画板程序的核心，比如{numref}`fig-started-drawing-brush` 中展示的那样，构成复杂画面的一条条笔触，其实是高频采样的一个个圆的叠加。由于这些绘制简单几何体的算法会被大量调用，如何设计高效的绘制算法将是本节的核心。

```{figure} fig/brush.png
:name: fig-started-drawing-brush
:width: 100%

绘制出复杂图形的光滑的笔刷其实是由高频率采样的圆组成 ©Procreate
```

```{toctree}
:maxdepth: 2

rasterization
polygon
composition
summary
```