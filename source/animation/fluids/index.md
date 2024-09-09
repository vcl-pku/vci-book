(chap-animation-fluids)=
# 流体模拟

流体现象在自然界中随处可见，小到秋日清晨的露珠，大到覆盖地球三分之二表面积的海洋以及包裹地球的大气，构成了世间大多数的奇观。在图形学中，流体现象也常用于影视和游戏的特效，例如溃坝现象、水花飞溅、烟雾效果等等。

````{subfigure} A|B
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-fluids-fluids_in_cg
:width: 80 %

```{image} fig/animation-fluids-frozen_dam_break.png
:alt: 《冰雪奇缘 2》中的溃坝现象
```

```{image} fig/animation-fluids-blackmyth_cloud.png
:alt: 《黑神话：悟空》中的筋斗云
```

影视与游戏中的流体模拟
````

流体也是一种连续介质，但常用的流体模拟方法与 {numref}`sec-animation-elastomers-fem` 中处理弹性体的方式不同，因为流体的运动相比固体而言要复杂得多：在固体中，我们能够找到一个连续可微的变形函数 $\boldsymbol\phi$，但在流体的运动过程中这个函数的性质将很快被破坏。在本章，我们首先会介绍在物理学中如何刻画流体的运动（{numref}`sec-animation-fluids-physics`），随后会介绍两种最为经典的流体模拟方法（分别对应于 {numref}`sec-animation-fluids-sph` 和 {numref}`sec-animation-fluids-eulerian`）。

```{toctree}
:maxdepth: 2

fluid-physics
sph-method
eulerian-fluid
summary
```