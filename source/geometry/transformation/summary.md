# 本章小结

## 思考题

1. 为什么需要将透视投影表示为式 {eq}`eq-geometry-transformation-persp-proj2`？其中出现的问号项具有什么实际含义？

## 习题

1. 在 {numref}`sec-geometry-transformation-3d-euler` 中我们提及，三次绕固定轴旋转的最终姿态和以相反顺序三次绕运动轴旋转的最终姿态相同。以 ZYX 欧拉角为例，证明：绕固定轴的 XYZ 旋转与绕运动轴的 ZYX 欧拉角所表示的旋转相同。

2. 式 {eq}`eq-geometry-transformation-persp-proj4` 是透视投影矩阵被表示为了含有 $x_\mathrm{min},x_\mathrm{max},y_\mathrm{min},y_\mathrm{max}$ 的形式，请将其改写为用相机参数表示的形式。以针孔相机模型为例，已知 $x_\mathrm{min}+x_\mathrm{max}=y_\mathrm{min}+y_\mathrm{max}=0$，相机参数包括：
    + 焦距 $f$；
    + 宽高比 $\mathrm{aspect}=\frac{x_\mathrm{max}-x_\mathrm{min}}{y_\mathrm{max}-y_\mathrm{min}}$；
    + 水平视场角 $\mathrm{hfov}=2\arctan\frac{x_\mathrm{max}-x_\mathrm{min}}{2f}$；
    + 近平面 $z_\mathrm{near}$；
    + 远平面 $z_\mathrm{far}$。

## 参考文献

```{bibliography} ref.bib
```
