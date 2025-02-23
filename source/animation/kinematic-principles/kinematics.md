(sec-animation-kinematic_principles-kinematics)=
# 运动学

在主观动态的场景中，大多数运动的对象可以被表示成一个铰链刚体，即由关节连接的一系列刚体（我们在 {numref}`sec-animation-rigid_bodies-articulated` 中还会探讨这类物体的模拟）。以人体为例，我们会将足部、大腿、小腿等在运动中几乎不产生形变的部位视为刚体，将膝、肘、脖子等关节视为铰链，如{numref}`fig-animation-kinematic_principles-human_T_pose` 所示。

```{figure} fig/animation-kinematic_principles-human_T_pose.png
:width: 25 %
:name: fig-animation-kinematic_principles-human_T_pose

人体的铰链刚体结构
```

本节会以{numref}`fig-animation-kinematic_principles-human_T_pose` 中的结构为例介绍一些处理这种铰链刚体运动状态的基本方法。运用这些方法，对于任意一个角色，只要我们能够抽象出它的骨架（即铰链刚体结构），就能够为它摆好姿态，进而使其活动起来。

(sec-animation-kinematic_principles-kinematics-forward)=
## 前向运动学

我们进一步将{numref}`fig-animation-kinematic_principles-human_T_pose` 中的人体结构抽象化，将每个关节看成一个节点、每个骨骼看成一条边，则可以转换成{numref}`fig-animation-kinematic_principles-human_structure` 所示的树结构。选定腰部关节作为整棵树的根节点，那么其余所有节点可以确定其唯一的父节点，并且每个节点的状态（即位置和全局朝向）可以从其父节点的状态推算出来；因此，只要我们知道了根节点的位置以及每个节点所对应关节的旋转，就可以从根开始向下遍历整棵树，推出所有关节的状态——这个过程又称为前向运动学（forward kinematics）。

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-kinematic_principles-human_structure
:width: 60 %

```{image} fig/animation-kinematic_principles-human_structure.png
:alt: 关节与骨骼形成的树结构
```

```{image} fig/animation-kinematic_principles-human_T_pose_with_marks.png
:alt: 树的顶点与关节之间的对应
```

将{numref}`fig-animation-kinematic_principles-human_T_pose` 中的人体结构抽象成树
````

定义一个三维空间下的正交坐标系 $xyz$，称关节相对于 $xyz$ 坐标系的旋转为全局旋转，其自身为子树内全部骨骼以及关节带来的旋转为局部旋转。在本节，我们一律使用四元数表示旋转。当所有关节的旋转为 $[1,\boldsymbol 0]$ 时，整个系统处于初始姿态。对于人体我们常常把这个初始姿态定义成{numref}`fig-animation-kinematic_principles-human_T_pose` 所示的姿态，即身体直立且手臂平举；这个姿态形似英文字母“T”，因此又被称为 T 型姿势（T-pose）。

现在我们以{numref}`fig-animation-kinematic_principles-simplified_chain_structure` 中展示的铰链刚体为例展示前向运动学的计算过程。这个铰链刚体包含三根骨骼、四个关节，将四个关节记为 $P_0\sim P_4$，它们的位置记为 $\boldsymbol p_0\sim\boldsymbol p_4$，相邻两个关节的相对位移记为 $\boldsymbol l_{0\sim 1}\sim\boldsymbol l_{2\sim 3}$，三根骨骼的长度就是这些相对位移的模长 $l_{0\sim 1}\sim l_{2\sim 3}$。

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-kinematic_principles-simplified_chain_structure
:width: 100 %

```{image} fig/animation-kinematic_principles-joint_chain_initial_pose.png
:alt: 简化铰链刚体的初始姿态
```

```{image} fig/animation-kinematic_principles-joint_chain.png
:alt: 简化铰链刚体的某一个姿态
```

简化的铰链刚体系统
````

令 $P_0$ 为根关节，那么在这个例子中，对于 $i\in\{1,2,3\}$，关节 $i$ 的父关节即为 $i-1$，有如下关系：

$$
\boldsymbol p_i=\boldsymbol p_{i-1}+\boldsymbol l_{(i-1)\sim i}。
$$

在初始姿态下，铰链刚体的所有关节和骨骼共线，我们不妨以根关节为原点、铰链刚体初始姿态下的指向为 $x$ 轴构建坐标系 $xyz$，那么初始状态下每个骨骼带来的相对位移即为

$$
\boldsymbol l_{(i-1)\sim i}^\mathrm{init}=\begin{bmatrix}l_{(i-1)\sim i}\\0\\0\end{bmatrix}。
$$

为了让铰链刚体摆出一个特定的姿态，我们会为除了 $P_3$ 的每个关节指定一个局部旋转，这个局部旋转会带动其后的全部关节和骨骼整体旋转，记这些局部旋转为 $q_0^\mathrm{local}\sim q_2^\mathrm{local}$。据此我们可以计算出所有关节的全局旋转。首先跟关节的全局旋转等于局部旋转，即 $q_0=q_0^\mathrm{local}$；对于非根关节，其局部旋转即为相对于父关节上固连的坐标系的旋转，因此全局旋转即为先进行局部旋转再进行父关节的全局旋转的复合结果，因此有 $q_i=q_{i-1}q_i^\mathrm{local}$（$i\in\{1,2\}$）。根据全局旋转，我们可以进一步求出骨骼带来的相对位移 $\boldsymbol l_{(i-1)\sim i}$ 即为 $q_{i-1}\left[0,\boldsymbol l_{(i-1)\sim i}^\mathrm{init}\right]q_{i-1}^\star$ 的虚部（$i\in\{1,2,3\}$）。至此我们不难求出每个关节的全局坐标。

在角色动画领域，人们常用的动捕文件格式——BVH 文件（BioVision Hierarchy 文件）——就是基于前向运动学的原理。这种动捕文件会包含一个铰链刚体在每个关节局部旋转均为 $[1,\boldsymbol 0]$ 时的初始状态信息，以及一段动作序列的每一帧的运动信息。每一帧的运动信息又包含根关节的位移，以及所有关节的局部旋转；我们需要借助前向运动学才能从动捕数据中恢复出完整的角色姿态。

## 关键帧动画

在学习了前向运动学之后，我们知道可以使用关节旋转和根节点位移的序列，来表示一段连续的动作序列。但是如果一段动作序列每一帧的信息都需要我们挨个输入，那么无论是时间成本还是制作成本，都会变得非常高昂。

```{figure} fig/animation-kinematic_principles-inbetween.png
:width: 50 %
:name: fig-animation-kinematic_principles-inbetween

关键帧动画
```

在手工绘制动画的时代，动画画师也会遇到相同的问题，针对该问题动画界给出的答案是中间画（in between）。动画师只绘制包含关键转折在内的关键帧，而在关键帧之间的起到衔接过渡的较为次要的动画，会由另一批画师绘制。这样子便可以让多个画师同时参与动画的绘制，同时能够较好地解决画师之间不同风格带来的问题。

类似于中间画的做法，运动学上也可以只编辑关键帧，通过关键帧之间进行插值的方式来降低生成动画的复杂性，但是此时我们可以使用计算机进行自动的中间动画生成。针对根节点的位置，我们可以采用贝塞尔曲线的方式对于根节点所处的位置进行插值。针对关节的旋转，我们则可以使用球面线性插值公式 {eq}`animation-kinematic_principles-quaternion_slerp` 进行更为平滑的旋转插值，也可以进一步的将贝塞尔曲线的思想应用到旋转插值上。由于关键帧之间不存在较为显著的位置，旋转的突变，因此使用上述算法进行动作的平滑过渡即可实现很好的插值结果。

(sec-animation-kinematic_principles-kinematics-backward)=
## 逆向运动学

### 循环坐标法

### 前向和后向迭代逆运动学

### 雅可比矩阵法
