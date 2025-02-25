(sec-animation-character-motion_synthesis)=
# 动作合成

利用上一节的动捕技术，我们可以得到一系列动作数据，接下来我们会介绍利用这些数据能够完成哪些任务。

(sec-animation-character-motion_synthesis-bvh)=
## 动作数据

在开始之前，我们首先需要了解动作数据在计算机中是以什么样的格式存储的。动捕数据一般以 BVH 文件（Biovision Hierarchy 文件）的形式存储，这类文件一般包含两部分（如{numref}`fig-animation-character-motion_data`）：
1. 动捕角色在 T 型姿势下的大小和姿态。
2. 每一帧的角色姿态描述。这部分信息被表示成一个集合 $\{\boldsymbol p_t\}$，每一帧的信息 $\boldsymbol p_t$ 形如 $\boldsymbol p_t=(\boldsymbol t_0,\boldsymbol R_0,\boldsymbol R_1,\boldsymbol R_2,\cdots)$，其中 $\boldsymbol t_0$ 表示角色根节点 (还记得 {numref}`sec-animation-kinematic_principles-kinematics-forward` 中我们将人体骨骼结构抽象成一棵树吗？) 的三维坐标，$\boldsymbol R_0,\boldsymbol R_1,\boldsymbol R_2,\cdots$ 分别表示每个关节的旋转。

显然，我们可以根据文件中的数据还原出一个角色的动作序列。

```{figure} fig/animation-character-motion_data.png
:width: 100 %
:name: fig-animation-character-motion_data

动作数据
```

利用这些数据通常分为几个环节（如{numref}`fig-animation-character-using_motion_data`），首先需要把采集到的数据重定向（retargeting）到虚拟角色上，在此基础上我们需要对动作进行编辑（editing），然后进行动作的连接和混合（transition and blending），最后我们会把动作放到动作图（motion graph）中，实现可交互的动作组成（composition）和生成。

```{figure} fig/animation-character-using_motion_data.png
:width: 100 %
:name: fig-animation-character-using_motion_data

动作数据的使用
```

## 动作重定向

```{figure} fig/animation-character-motion_retargeting.png
:width: 40 %
:name: fig-animation-character-motion_retargeting

动作重定向
```

一般来讲，动作捕捉的采集对象是人，而虚拟角色往往多种多样，其身体结构可能也会比人复杂得多，这个时候我们就需要进行动作重定向（如{numref}`fig-animation-character-motion_retargeting`）。和人相比，虚拟角色可能具有不同数量的骨骼、不同的骨骼名称、不同的静止姿态、不同的骨骼比例、不同的骨架结构等等。正是这种复杂性，使得重定向任务会遇到各种各样的问题，例如一些不够鲁棒的重定向会导致角色的脚底离开地面（如{numref}`fig-animation-character-motion_retargeting_problem`(a)），或者出现穿模现象（如{numref}`fig-animation-character-motion_retargeting_problem`(b)）。

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-character-motion_retargeting_problem
:width: 100 %

```{image} fig/animation-character-motion_retargeting_floating.png
:alt: (a) 角色脚底离开地面
```

```{image} fig/animation-character-motion_retargeting_collision.png
:alt: (b) 穿模
```

动作重定向时会遇到的问题
````

动作重定向的流程可以分为以下几步：
1. **关节映射。** 在动捕数据中的关节和虚拟角色的关节之间建立一个映射。
2. **调整大小。** 有时动捕数据中的长度单位与虚拟角色的不一致，动捕数据中的单位大多为米或英尺，而虚拟角色用的则可能是任何单位。这个步骤要处理的一个典型场景是走路的动作，对于这个场景我们通常会把根关节的位移缩放到高度与虚拟角色腿长相近，从而保证走路过程中脚不离地。
3. **复制或重定向关节旋转以修正初始姿态。** 为虚拟角色计算出每个关节的旋转以使它的初始姿态（T 型姿势或 A 型姿势）能够匹配动捕数据的初始姿态。这个步骤在虚拟角色和动捕数据中的身体长度不一致时会比较繁琐，此时我们可以借助一些启发性的规则来确定关节旋转，例如对于动捕数据中没有出现的关节我们可以将其旋转设为零或设置为相邻关节旋转的平均值。
4. **使用逆向运动学进行后处理，以解决诸如脚底打滑、穿模等问题。** 这些问题往往需要调整关节位置来解决，仅仅修改动捕数据中的关节旋转是不够的，所以逆向运动学就不可避免。

为了更方便地进行重定向，业界提出了一些新的动捕数据的表示方式（其重定向效果如{numref}`fig-animation-character-ik_rig`），称为反向运动学绑定（IK rig）。在这种表示方式中，我们不再记录每个关节的旋转，而是记录一些关键关节的位置。于是我们只需要重定向相应关节的位置，再在虚拟角色上做逆向运动学，即可完成高质量的动作重定向。目前很热门的虚幻引擎（Unreal）也支持反向运动学绑定的格式（如{numref}`fig-animation-character-ik_rig_unreal`）。

```{figure} fig/animation-character-ik_rig.png
:width: 60 %
:name: fig-animation-character-ik_rig

反向运动学绑定原型
```

```{figure} fig/animation-character-ik_rig_unreal.png
:width: 80 %
:name: fig-animation-character-ik_rig_unreal

虚幻引擎中的反向运动学绑定
```

## 动作连接

在完成动作重定向之后，我们还需要进行动作连接，这是因为我们采集到的动捕数据往往只是一个动作片段，为生成完整、流畅的动作还需要将多段动捕数据中的动作串联起来。例如我们现在已经重定向好了一段走路的动作和一段跑步的动作，我们想让虚拟角色先走路两秒钟，再跑步两秒钟，那么就需要借助动作连接技术从走路尽可能连贯地过渡到跑步。

````{subfigure} ABC
:layout-sm: A|B|C
:gap: 8px
:subcaptions: below
:name: fig-animation-character-motion_transition_steps
:width: 100 %

```{image} fig/animation-character-motion_transition1.png
```

```{image} fig/animation-character-motion_transition2.png
```

```{image} fig/animation-character-motion_transition3.png
```

动作连接的步骤
````

### 基础的动作连接方法

我们假设需要连接的两个动作分别为动作 $A$ 和动作 $B$，一个最简单的动作连接可以分为以下三步（如{numref}`fig-animation-character-motion_transition_steps`）：
1. 在 $A$ 的动作序列和 $B$ 的动作序列中分别挑选一帧，这两帧越相近越好，如{numref}`fig-animation-character-motion_transition_steps` 中的过渡帧（transition frame）。
2. 将 $A$ 与 $B$ 的动作序列进行时间对齐，使得挑选出的过渡帧处于同一时刻。
3. 保留 $A$ 序列过渡帧前的部分和 $B$ 序列过渡帧后的部分，并直接拼接形成新的动作序列。

这个方法的缺点很明显：除非保证 $A$、$B$ 动作在过渡帧完全相同，拼接处会出现一个不连续的跳变。但是这个方法在游戏中很常见，因为游戏中经常会有一些循环动作，角色在做完一个动作后总要恢复到动作开始前的姿态，比如我们经常看到一个角色做完“挥拳”或者“开枪”的动作之后总会恢复站立的姿态。

### 平滑的动作连接

```{figure} fig/animation-character-motion_transition_interpolation.png
:width: 70 %
:name: fig-animation-character-motion_transition_interpolation

平滑的动作连接
```

在一般情况下，我们在动作过渡的时候需要做一个平滑操作。这时我们不应再只考虑一帧的切换，而是要考虑两个动作在过渡帧前后一段时间的序列。如{numref}`fig-animation-character-motion_transition_interpolation` 所示，我们设这个过渡片段的开始时间为 $0$，结束时间为 $1$，再设动作序列 $A$ 为 $\boldsymbol p_0$，$B$ 为 $\boldsymbol p_1$，那么对于时刻 $t\in[0,1]$，我们的过渡动作可以取动作序列 $A$ 和 $B$ 的线性插值：

$$
\boldsymbol p(t)=(1-t)\boldsymbol p_0(i)+t\boldsymbol p_1(i)
$$ (animation-character-motion_transition_linear)

其中 $i$ 表示时刻 $t$ 对应的帧数，使用这样的插值我们能做到在时间从 $0$ 到 $1$ 推进的过程中，角色动作会从 $A$ 逐渐过渡到 $B$。为了达到一些特殊的平滑效果，我们也可以不使用线性插值，将式 {eq}`animation-character-motion_transition_linear` 中的 $t$ 换成一个关于 $t$ 的单调增函数 $\phi(t)\in[0,1]$，变成如下形式：

$$
\boldsymbol p(t)=(1-\phi(t))\boldsymbol p_0(i)+\phi(t)\boldsymbol p_1(i)
$$ (animation-character-motion_transition_nonlinear)

其中的 $\phi(t)$ 可以取二次函数、指数函数等。

### 动作对齐

### 曲线跟踪

## 动作图

## 其他动作合成方法
