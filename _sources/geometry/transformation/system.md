(sec-geometry-transformation-system)=
# 坐标系变换

计算机图形应用经常需要在场景处理时将对象的描述从一个坐标系变换到另一个坐标系，比如在建模时，单个物体对象常在各自的局部笛卡尔坐标系下设计，但当将它们放置在大场景中时，就需要变换到以场景作为参考系或是世界坐标系下。同时，也有不少对象表示在非笛卡尔坐标系（如极坐标，球面坐标系下），需要将其转化到统一的笛卡尔坐标系里。

```{figure} fig/coordinate.png
:name: fig-geometry-transformation-coordinate
:width: 80%

坐标变换示意图。
```

## 二维坐标系变换

如 {numref}`fig-geometry-transformation-coordinate` 左边所示，点 $p$ 在坐标 $uv$ 和坐标 $xy$ 下的坐标分别为

$$
\begin{aligned}
    (p_u,p_v)&=\vec{e}+p_u\vec{u}+p_v\vec{v}\,, \\
    (p_x, p_y)&=\vec{o}+p_x\vec{x}+p_y\vec{y}\,.
\end{aligned}
$$ (eq-geometry-transformation-system1)

这两个坐标表示的是同一个点，从而可以得到从 $uv$ 坐标到 $xy$ 坐标的转换关系，从矩阵形式也可以看出来，二维坐标变换的过程，也可以看作是坐标系的变换，先将当前坐标系进行旋转，再对坐标系进行平移：

$$
     \begin{aligned}
        \begin{bmatrix}
            p_x \\
            p_y \\
            1
        \end{bmatrix} = 
        \begin{bmatrix}
            1 & 0 & e_x \\
            0 & 1 & e_y \\
            0 & 0 & 1
        \end{bmatrix}
        \begin{bmatrix}
            u_x & v_x & 0 \\
            u_y & v_y & 0 \\
            0 & 0 & 1
        \end{bmatrix}
        \begin{bmatrix}
            p_u \\
            p_v \\
            1
        \end{bmatrix}.
    \end{aligned}
$$ (eq-geometry-transformation-system2)

## 三维坐标变换

类比二维坐标变换，对于 {numref}`fig-geometry-transformation-coordinate` 中间的三维空间中点的表示 $(p_x,p_y,p_z)$ 和 $(u_x,u_y,u_z)$，有如下转换矩阵：

$$
     \begin{aligned}
        \begin{bmatrix}
            p_x \\
            p_y \\
            p_z \\
            1
        \end{bmatrix} = 
        \begin{bmatrix}
            1 & 0 & 0 & e_x \\
            0 & 1 & 0 & e_y \\
            0 & 0 & 1 & e_z \\
            0 & 0 & 0 & 1
        \end{bmatrix}
        \begin{bmatrix}
            u_x & v_x & w_x & 0 \\
            u_y & v_y & w_y & 0 \\
            u_z & v_z & w_z & 0 \\
            0 & 0 & 0 & 1
        \end{bmatrix}
        \begin{bmatrix}
            p_u \\
            p_v \\
            p_w \\
            1
        \end{bmatrix}.
    \end{aligned}
$$ (eq-geometry-transformation-system3)

在计算机图形里，有一个很重要的三维变换，视角变换。比如通过相机观察了一个场景中的物体，需要推测物体在三维场景中的位置，就需要从相机观察的视角下变换到世界坐标下。

通常，观察视角由三个信息组成：位置向量 $\mathbf{P}$、观察方向 $\mathbf{N}$（即观察平面的法向量）、向上向量 $\mathbf{V}$。这三个向量唯一地确定了观测坐标系。从观测坐标系到全局坐标系可以类似三维坐标变换那样将观测坐标系当作三维坐标系处理，也可以将观察点平移到原点，再将观察方向旋转到 $z$ 方向，最后将正上方旋转到 $y$ 方向。
