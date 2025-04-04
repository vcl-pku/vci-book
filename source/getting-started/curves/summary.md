# 本章小结

在本章中，我们首先介绍了曲线相关的几个数学概念：显式和隐式表达，光滑性，基函数。然后介绍了几类常见的曲线：样条曲线，厄米样条曲线，B样条曲线，NURBS 曲线，贝塞尔样条曲线。最后我们介绍了曲线的光栅化。

## 习题

### 三阶曲线

请区分三次样条曲线、三次厄米样条曲线、三次B样条曲线、三次贝塞尔样条曲线，并从不同维度（计算复杂度、光滑性、局部性等）比较它们之间的区别。

### 三阶厄米样条曲线的基函数

Catmull-Rom 三次样条曲线可以被写为基函数的形式 {eq}`eq-started-curves-linear4`，请写出对应基函数的完整定义（应该是一个分段函数），并通过基函数说明Catmull-Rom 三次样条曲线的性质，包括插值性、光滑性和局部性。

### 三阶贝塞尔样条与三阶厄米样条

三阶贝塞尔样条与三阶厄米样条都是三阶曲线，并且都有显式多项式形式，因此应该具有相同的表达能力。请对比两者的定义，给出两者相互转换的方式。

<!-- ## 参考文献 -->

<!-- ```{bibliography} ref.bib
``` -->
