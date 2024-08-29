(chap-animation-rigid_bodies)=
# 刚体模拟

在我们的身边充斥着许多“硬”的物体，它们几乎不发生形变，在物理中有一个相应的概念叫做刚体（rigid body），即不发生形变的物体。在虚拟世界中，刚体模拟也是一个不可或缺的部分，在游戏、影视、仿真平台等应用场景中都属于基本的需求；另外，在 {numref}`chap-animation-kinematic_principles` 与 {numref}`chap-animation-character` 中多次出现的角色骨架也都会被建模成铰链刚体，所以不难看出刚体模拟在机器人学以及具身智能领域的重要性。与一般连续介质不同的是，刚体具有不可形变的特性，因此在模拟时我们可以将其看成一个整体，而不需要进行 {numref}`chap-animation-elastomers` 中的空间离散化，从而大大提高模拟效率。本章会首先带领大家了解刚体遵循的物理规律以及它的时间积分算法（{numref}`sec-animation-rigid_bodies-dynamics`），随后会介绍如何处理刚体的碰撞与摩擦现象（{numref}`sec-animation-rigid_bodies-contact_and_friction`），此外我们还会介绍如何模拟铰链刚体（{numref}`sec-animation-rigid_bodies-articulated`），最后会总结一个刚体求解器的完整步骤（{numref}`sec-animation-rigid_bodies-simulator`）。

```{toctree}
:maxdepth: 2

rigid-body-dynamics
contact-and-friction
articulated-rigid-body
rigid-body-simulator
summary
```