(sec-animation-fluids-physics)=
# 流体的物理模型

在了解流体的动力学方程之前，我们首先需要知道如何刻画一个正在运动的流体系统。我们可以借助“场”的概念，用速度场 $\boldsymbol v(\boldsymbol x)$ 来表示流体的速度在空间中的分布——事实上这样就足够了。如果我们知道每个时刻的速度场 $\boldsymbol v(\boldsymbol x,t)$ 以及初始时流体的分布情况，就可以唯一地还原出流体的完整运动情况，因为对于初始时流体中的任何一点，都可以借助 $\boldsymbol v(\boldsymbol x,t)$ 唯一还原出它随流体运动的完整轨迹。但是为了方便计算流体运动状态的改变，我们还需要表示出流体的其他物理量，具体来讲，用标量场 $\rho(\boldsymbol x,t)$ 表示流体的密度分布，用标量场 $p(\boldsymbol x,t)$ 表示流体的压强分布。在后续的式子中，我们将省略场的位置和时间参数 $(\boldsymbol x,t)$。

## 纳维-斯托克斯方程

与前面学过的物理现象一样，流体所遵循的最基本的动力学方程仍然是牛顿第二定律 $\boldsymbol f=m\ddot{\boldsymbol x}$，只是流体内部的力要更为复杂一些，所以方程会变得稍微复杂一点：

$$
\rho\frac{\mathrm D\boldsymbol v}{\mathrm Dt}=-\nabla p+\rho\boldsymbol g+\mu\nabla^2\boldsymbol v。
$$ (animation-fluids-ns_equation)

这就是著名的纳维-斯托克斯方程（Navier-Stokes Equation）。

为了看懂这个方程，我们首先取某一时刻流体中的一个点，由于体积无穷小，所以质量也是无穷小的，那么现在有意义的物理量就是密度 $\rho$（即单位体积内的质量），它取代了牛顿第二定律中的 $m$；$\frac{\mathrm D\boldsymbol v}{\mathrm Dt}$ 是速度的随体导数（material derivative），它的含义是，假设我们在流体中选取的点是随着流体一起运动的，那么这个点在当前时刻的速度的导数——这完美地对应了牛顿第二定律中的加速度。总而言之，纳维-斯托克斯方程等号左边的部分 $\rho\frac{\mathrm D\boldsymbol v}{\mathrm Dt}$ 对应于牛顿第二定律中的 $m\ddot{\boldsymbol x}$，它的意义是“单位体积内流体的质量乘以加速度”。

接下来再依次分析等号右边的每一项。在中学我们就知道压强 $p$ 的定义是“单位面积内受压力大小”，那么 $-\nabla p$ 可以理解为“单位距离上的压强差”，也就是“单位体积内所受压力”，由于压力是从高压强处指向低压强处，所以要带上负号；$\boldsymbol g$ 是外力（包括重力等）提供的加速度，所以 $\rho\boldsymbol g$ 就是单位体积内流体所受的外力；$\mu\nabla^2\boldsymbol v$ 是粘性项，流体的粘性阻止流体产生形变，所以与速度的拉普拉斯成正比，在一般的流体模拟中会直接忽略这一项。将这些加到一起，我们就能够知道等号右边的含义就是“单位体积内流体所受的力”，这个力由压强、重力和粘性提供，对应于牛顿第二定律中的 $\boldsymbol f$。

## 不可压性质

要想模拟出真实的水的效果，仅靠纳维-斯托克斯方程是不够的，因为水还有一个不可压性质，即任意时刻任意处的体积不变。想要描述这个性质，我们先从物理中的质量守恒方程（mass conservation equation）开始：

$$
\frac{\partial\rho}{\partial t}=-\nabla\cdot(\rho\boldsymbol v)。
$$ (animation-fluids-mass_conservation_equation)

在一般的流体模拟（包括水、烟雾模拟等）中，我们都会有一个不可压的假设，即密度恒定，$\rho$ 在各处、任意时刻都为常数。在这样的假设下，式 {eq}`animation-fluids-mass_conservation_equation` 就变成

$$
\nabla\cdot\boldsymbol v=0，
$$ (animation-fluids-divergence_free_velocity)

即速度场无散。结合高斯公式，我们可以发现，流体速度场无散说明，在流体内部任取一个由有限块光华双侧曲面围成的有界闭区域，则流进该区域的流量和流出的流量相等，即该区域内流体体积守恒。

那么在物理上，流体的不可压性质是如何实现的呢？还记得纳维-斯托克斯方程（式 {eq}`animation-fluids-ns_equation`）中的压强项 $-\nabla p$ 吗？没错，压强就是用来维持流体的不可压性质的。绝大多数的流体仿真算法都遵循这样的流程：先按照速度场进行对流，然后加上外力项，最后我们要计算合适的压强分布使得在压强的作用下速度能重新变成一个（近似的）无散场。这样的流程背后的原理其实是处理偏微分方程常用的分裂法（splitting method），将纳维-斯托克斯方程拆分成如下三个步骤（这里忽略了粘性项），分别对应于对流、施加外力以及求解压强：

$$
\frac{\mathrm D\boldsymbol v}{\mathrm Dt}&=0，\\
\frac{\partial\boldsymbol v}{\partial t}&=\boldsymbol g，\\
\rho\frac{\partial\boldsymbol v}{\partial t}&=-\nabla p\quad\text{s.t.}\,\nabla\cdot\boldsymbol u=0。
$$

## 描述流体的两种视角

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-fluids-viewpoints
:width: 100 %

```{image} fig/animation-fluids-eulerian_viewpoint.png
:alt: 欧拉视角
```

```{image} fig/animation-fluids-lagrangian_viewpoint.jpg
:alt: 拉格朗日视角
```

描述流体运动的两个视角
````

式 {eq}`animation-fluids-ns_equation` 是以**欧拉视角**来描述流体的运动的，欧拉视角是指将流体的所有物理量看成空间上的一个场，然后描述这个场随时间的变化。这好比在水中插有无限多的木桩，每个木桩上装有检测水的流速、密度、压强等的传感器，我们描述的是所有传感器上的数值变化。

另一种描述流体的视角叫做**拉格朗日视角**，它将流体看成由无限多个质元组成，流体的运动就是每个质元的运动，我们关注的是所有的质元在每个时刻的位置、速度等物理量。这好比在水上放有无穷多个随波逐流的小船，在船上安放检测水各种物理量的传感器，并描述它们的数值变化。

借助这个概念我们可以更加深刻地理解随体导数 $\frac{\mathrm D\boldsymbol v}{\mathrm Dt}$ 的含义，它可以看做是随波逐流的小船的加速度，这个导数又称为拉格朗日导数（Lagrangian derivative）。我们也可以将其用欧拉导数（Eulerian derivative）来表示，假设我们关注流体中某一个点的运动，这个点的运动轨迹为 $\boldsymbol x(t)$，则它的速度随时间变化可以表示为函数 $\boldsymbol v(\boldsymbol x(t),t)$，那么随体导数就是对这个函数关于时间求全微分：

$$
\frac{\mathrm D\boldsymbol v}{\mathrm Dt}=\frac{\mathrm d\boldsymbol v(\boldsymbol x(t),t)}{\mathrm dt}=\frac{\partial\boldsymbol v}{\partial t}+\frac{\mathrm d\boldsymbol x}{\mathrm dt}\cdot\nabla\boldsymbol v=\frac{\partial\boldsymbol v}{\partial t}+\boldsymbol v\cdot\nabla\boldsymbol v。
$$

由此可见，欧拉视角和拉格朗日视角下描述的流体动力学方程是等价的，即便纳维-斯托克斯方程是一个欧拉视角下的方程，我们完全可以用拉格朗日视角的方法去模拟。