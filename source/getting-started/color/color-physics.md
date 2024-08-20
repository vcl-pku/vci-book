# 颜色的物理与感知

## 颜色的物理

**颜色（color）** 是一种光的视觉效应。颜色视觉（简称“色觉”）是视觉感知的一部分，是一种用来区分由不同波长的光波组成的光的能力，在感知器官中发挥着重要作用。光是一种电磁波，我们可以按照光的波长（或者频率）对光进行展开分类，如{numref}`fig-started-color-visible_light` 所示。其中，波长大致在380-750纳米范围的电磁波称为**可见光（visible light）**，可以被人眼所观察到，在整个电磁波谱上只占非常窄的一部分。

```{figure} fig/visible_light.png
:name: fig-started-color-visible_light

可见光在整个电磁波频谱上的位置
```

单一波长的光在自然界中比较少见，可以由激光（laser）发射器产生。自然界中出现的光一般是不同频率的光的叠加，其中各个频率成分的强度比例不同就会混合出不同的颜色。在数学上可以用 $I(\lambda)$ 表示对应波长的强度。

## 颜色的感知

光在进入人眼之后，会被视网膜上的两种细胞捕获：视锥细胞（cone cells）和视杆细胞（rod cells），如{numref}`fig-started-color-photoreceptors` 所示。视锥细胞分布在视网膜的中央，每个视网膜大概有 700 万个，它对光的波长敏感。视杆细胞分散分布在视网膜上，每个视网膜上约有 1 亿个，不区分光线波长，对光线的强度更为敏感。也就是说，视锥细胞负责感知颜色，视杆细胞负责感知强度。

```{figure} fig/photoreceptors.webp
:name: fig-started-color-photoreceptors

视锥细胞与视杆细胞[^cell]
```
[^cell]: [American Academy of Ophthalmology](https://www.aao.org/eye-health/anatomy/cones)

视锥细胞按照其所敏感的光的波长可以分为三种：长、中、短，分别对红、绿、蓝三种光敏感，如图{numref}`fig-started-color-cone-spec` 展示了三种视锥细胞对可见光的响应程度。当一种频率的色光被视锥细胞捕获时，我们的大脑就能根据三种细胞响应强度的不同合成出颜色的感知。


```{figure} fig/cone-spec.svg
:name: fig-started-color-cone-spec

三种视锥细胞对可见光的响应分布[^cone-spec]
```
[^cone-spec]: [Wikipedia: Cone cell](https://en.wikipedia.org/wiki/Cone_cell)


## 颜色的混合

光可以混合，那人眼看到的颜色如何随混合变化？这个规律由赫尔曼·格拉斯曼（Hermann Grassmann）总结得到[^Grassmann]，简单来说，他说明了人类对色彩的感知（大约）是线性的。如果用数学公式来描述格拉斯曼定律，对于某一种强度分布$I(\lambda)$的色光，我们可以给出对应的红、绿、蓝（red, green, blue, RGB）座标：

$$
R = \int_0^\infty I(\lambda) \bar{r}(\lambda) d\lambda \\
G = \int_0^\infty I(\lambda) \bar{g}(\lambda) d\lambda \\
B = \int_0^\infty I(\lambda) \bar{b}(\lambda) d\lambda
$$ (eq-started-color-rgb)

其中 $\bar{r}(\lambda)$， $\bar{g}(\lambda)$，$\bar{b}(\lambda)$ 分别对应三种视锥细胞对不同波长的相应强度，展示在{numref}`fig-started-color-cone-spec` 中。坐标 $(R, G, B)$ 也可以称为三原色坐标，与 $I(\lambda)$ 满足线性关系。在这样的假设下，如果有两束色光，坐标为 $(R_1, G_1, B_1)$ 和 $(R_2, G_2, B_2)$，当此二光束合并时，观测者感知的三原色数值就应该为 $(R_1 + R_2, G_1 + G_2, B_1 + B_2)$。正是出于这样的原因，RGB坐标成为颜色表达的最经典的方式，这也是我们下一节讨论颜色离散表达的基础。

[^Grassmann]: [Wikipedia: Grassmann's laws (color science)](https://en.wikipedia.org/wiki/Grassmann%27s_laws_(color_science))