(sec-animation-rigid_bodies-dynamics)=
# 刚体动力学

在力学中，刚体是一个理想化的物理模型，我们对这个模型的基本假设是它不会产生任何形变；用更严谨的说法讲，刚体是**一种任意两个质点之间的距离在运动过程中保持不变的物体**。生活中我们遇到的一些比较坚硬的物体都不是刚体，因为它们在受力时总会产生微小的形变，只不过肉眼看不到——严格来讲它们应该属于劲度（stiffness）很强的弹性体。事实上，物体只有发生形变才可能产生抵抗的作用力，在力学中刚体的受力情况其实是取物体形变程度趋于零的极限得到的。

## 刚体的运动

```{figure} fig/animation-rigid_bodies-rigid_motion.png
:width: 50 %
:name: fig-animation-rigid_bodies-rigid_motion

坐标系的选择以及刚性运动的描述
```

在 {numref}`sec-animation-elastomers-fem` 中我们已经了解了什么是刚性运动（还记得超弹性体的能量要满足刚性运动下的不变性吗？），即只包含平移和旋转的运动。事实上，这个结论可以从刚体的定义推导出来。接下来，如{numref}`fig-animation-rigid_bodies-rigid_motion` 所示，我们将参考构型下刚体的质心为原点构造直角坐标系，并且选取质心为参考点（即刚体在任一时刻的旋转都认为是关于质心的旋转），那么参考构型下的任意一点 $\boldsymbol X$ 与刚体经过一系列运动后该点位置 $\boldsymbol x$ 的关系可以表示为

$$
\boldsymbol x(t)=\boldsymbol R(t)\boldsymbol X+\boldsymbol c(t)，
$$ (animation-rigid_bodies-rigid_motion)

其中 $\boldsymbol R$ 是旋转矩阵，$\boldsymbol c$ 是运动后刚体的质心；这里我们将和运动时间 $t$ 有关的量写成了函数的形式。通过式 {eq}`animation-rigid_bodies-rigid_motion` 我们自然可以想到，如果需要刻画刚体的运动，需要分别研究好 $\boldsymbol c(t)$ 和 $\boldsymbol R(t)$，它们分别对应于刚体的平动和转动。

### 刚体的平动

刚体的平动完全由质心的运动刻画，我们可以直接将整个刚体看成位置与质心重合的质点，因此刚体平动的速度 $\boldsymbol v(t)$ 与质心位置的关系是 $\boldsymbol v(t)=\dot{\boldsymbol c}(t)$。

### 刚体的转动

由刚体的定义可以推出任意两点在任一时刻的相对速度与它们的相对位置正交，利用这个结论，我们可以证明绕定点转动的刚体一定存在唯一一个过该点的转动瞬轴（instantaneous axis），即在其上的任一质点速度为 $\mathbf 0$ 的轴。证明方法可以参考 {cite}`Cao2000InstantaneousAxisProof`，大体思路就是找到刚体上两个具有不平行速度的质点，过它们分别作两个垂直于速度方向的平面，交线就是转动瞬轴，如{numref}`fig-animation-rigid_bodies-instantaneous_axis` 所示。

```{figure} fig/animation-rigid_bodies-instantaneous_axis.png
:width: 40 %
:name: fig-animation-rigid_bodies-instantaneous_axis

通过刚体质点的速度确定转动瞬轴：取两个速度方向不平行的质点 $A$ 和 $B$，过 $A$ 作垂直于 $\boldsymbol v_A$ 的平面 $\mathcal P_A$，过 $B$ 作垂直于 $\boldsymbol v_B$ 的平面 $\mathcal P_B$，$\mathcal P_A$ 与 $\mathcal P_B$ 的交线即为转动瞬轴。
```

如果我们将刚体每一时刻的位置都统一减去质心的位置，那么剩下的部分就是刚体绕质心的转动，在每一时刻都存在一个转动瞬轴。借助“任意两点在任一时刻的相对速度与它们的相对位置正交”这个结论，读者不难推理出刚体每个质点上的速度构成的速度场就是围绕着转动瞬轴的涡，并且速度的大小与质点到转动瞬轴的位置成正比。

````{hint}
由于任意两点在任一时刻的相对速度与它们的相对位置正交，且转动瞬轴上所有质点的速度均为 $\mathbf 0$，读者可以尝试证明：任意一个不在转动瞬轴上质点的速度必然垂直于转动瞬轴与质点质心连线张成的平面，由此可以立即得到速度场是绕着转动瞬轴的旋转。

```{figure} fig/animation-rigid_bodies-velocity_length.png
:width: 50 %
:name: fig-animation-rigid_bodies-velocity_length

在垂直于转动瞬轴的平面 $\mathcal P_C$ 上证明速度的大小与到轴的距离成正比
```

若希望证明速度的大小与质点到转动瞬轴的位置成正比，我们可以只在过质心与转动瞬轴垂直的平面 $\mathcal P_C$ 上证明此结论，对于空间中的其他点，其速度等于该点在 $\mathcal P_C$ 上投影点处的速度。如{numref}`fig-animation-rigid_bodies-velocity_length`，设质心为点 $C$，在 $\mathcal P_C$ 上再取两点 $A$、$B$ 使得 $A$、$B$、$C$ 不共线，记向量 $CA$ 和 $CB$ 分别为 $\boldsymbol r_A$ 和 $\boldsymbol r_B$，$A$、$B$ 的速度分别为 $\boldsymbol v_A$ 和 $\boldsymbol v_B$，那么我们有

$$
\boldsymbol r_A\cdot\boldsymbol v_A=\boldsymbol r_B\cdot\boldsymbol v_B=0，\\
(\boldsymbol r_A-\boldsymbol r_B)\cdot(\boldsymbol v_A-\boldsymbol v_B)=0，
$$

其中 $\cdot$ 表示向量的内积。通过这些等式可以立即得到

$$
\boldsymbol r_A\cdot\boldsymbol v_B=-\boldsymbol r_B\cdot\boldsymbol v_A，
$$

这等价于

$$
\Vert\boldsymbol r_A\Vert\cdot\Vert\boldsymbol v_B\Vert\cos\langle\boldsymbol r_A,\boldsymbol v_B\rangle=-\Vert\boldsymbol r_B\Vert\cdot\Vert\boldsymbol v_A\Vert\cos\langle\boldsymbol r_B,\boldsymbol v_A\rangle。
$$

由于 $\boldsymbol r_A$、$\boldsymbol r_B$ 不共线，所以等式两边的三角函数必不为零，再利用 $\boldsymbol r_A$ 与 $\boldsymbol v_A$ 垂直、$\boldsymbol r_B$ 与 $\boldsymbol v_B$ 垂直且等式两边三角函数必须反号，读者不难推出 $\cos\langle\boldsymbol r_A,\boldsymbol v_B\rangle=-\cos\langle\boldsymbol r_B,\boldsymbol v_A\rangle$，于是得出向量模长的关系 $\frac{\Vert\boldsymbol r_A\Vert}{\Vert\boldsymbol r_B\Vert}=\frac{\Vert\boldsymbol v_A\Vert}{\Vert\boldsymbol v_B\Vert}$，这也正是我们希望证明的速度大小的关系。
````

到这里读者不难发现，刚体上所有质点的速度的总自由度其实很少，我们只需要知道转动瞬轴的方向，以及一个能够表示速度大小的量，就能够还原出整个刚体的转动速度。角速度（angular velocity）便是这样一个描述刚体转动有多快的量，它是一个三维矢量，记为 $\boldsymbol\omega$；其方向与转动瞬轴平行，刚体的转动方向遵循右手定则，即当 $\boldsymbol\omega$ 指向自身时看到的刚体是逆时针转动的；其大小又记为不加粗的 $\omega$，表示刚体每秒钟旋转的圈数，单位为秒的负一次方（$\mathrm s^{-1}$），因此角速度又称为角频率向量（angular frequency vector）。

通过上述对刚体质点上速度的研究，我们不难证明：若刚体质心固定，对于任一质点，设质心到该点的向量为 $\boldsymbol r$，则该点的速度为 $\boldsymbol\omega\times\boldsymbol r$。这也对应于式 {eq}`animation-rigid_bodies-rigid_motion` 中旋转部分的速度，即

$$
\dot{\boldsymbol R}(t)\boldsymbol X=\boldsymbol\omega\times(\boldsymbol x(t)-\boldsymbol c(t))=\boldsymbol\omega\times(\boldsymbol R(t)\boldsymbol X)。
$$

## 刚体力学

