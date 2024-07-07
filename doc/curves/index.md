# 曲线
:label:`chap_curves`

我们在 :numref:`chap_drawing-2d` 中学习了直线或圆等简单图形的绘制方法，但是这对于更一般的复杂图形的表示来说仍然不够。一个常见的情形是文字的显示，如 :numref:`fig_curve-fontforge` 中的字体'a'，该图形轮廓中除了直线，还包含了多段曲线。理论上说，我们可以用多段直线来近似曲线，但这种近似将会消耗较多的计算和存储资源才能达到相对光滑的视觉效果，并且在进行局部放大时仍然显示出走样。因此，为了能够更加准确、高效地绘制这些图形，我们需要一些方式来直接表示和渲染光滑曲线。

![利用[DesignWithFontforge](https://github.com/fontforge/designwithfontforge.com/)生成的字母'a'，其轮廓由直线段和三阶贝塞尔曲线段共同构成。](../../img/curve/bezier_sample_2.png)
:width:`500px`
:label:`fig_curve-fontforge`

````toc
:maxdepth: 2

curve-basic
curve-bezier
curve-spline
curve-rasterization
summary
````