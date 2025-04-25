# 虚拟现实与增强现实

三维交互技术的不断发展提升了用户与数字环境的交互方式，当沉浸式的人机交互体验成为可能，构建一个以人为中心的虚拟世界就不再遥远。

在当今数字时代，虚拟现实、增强现实以及混合现实这些术语越来越普遍，它们共同构成了扩展现实的概念。这些技术通过不同方式改变我们感知和互动的现实世界，开启了全新的交互体验。

**虚拟现实**（Virtual Reality，VR）是一种完全沉浸式的体验，用户通过头戴显示设备进入一个完全由计算机生成的场景。在这种环境中，现实世界被完全屏蔽，用户的视觉、听觉甚至触觉都被引导至一个虚构的世界。这种技术主要用于游戏、模拟训练以及教育等领域，提供了一个无界限的平台，让用户可以探索、学习和执行任务，而不受物理空间的限制。

**增强现实**（Augmented Reality，AR）技术则是在用户的现实世界中叠加计算机生成的图像或信息。通过智能手机、平板电脑或专门的 AR 眼镜，用户可以看到真实世界与虚拟对象的结合。这种技术的一个著名例子是《Pokemon Go》，这款游戏将虚拟的宠物怪兽置入真实世界的地理位置中，玩家需要在物理世界中移动来捕捉它们。AR 技术广泛应用于导航、教育、零售和娱乐等领域，通过增强现实世界的信息，提高用户的互动和认知效率。

**混合现实**（Mixed Reality，MR）则进一步扩展了 AR 的概念，它允许用户在虚拟环境中与真实世界的物体进行互动。这种交互可以通过特定的头戴设备实现，如微软的 HoloLens，用户不仅可以看到真实和虚拟世界的融合，还可以用手直接操作虚拟元素。MR 技术为工业设计、医疗、教育等行业提供了强大的应用潜力，使得复杂的数据和模型可以在真实环境中被直观地展示和操作。

**扩展现实**（Extended Reality，XR）是一个包括 VR、AR 及 MR 所有形式的综合术语。XR 涵盖了从完全虚拟到部分增强的所有现实交互形式，它的目标是通过提供更加丰富、多元的互动方式 来增强人类的感知能力和操作效率。

````{subfigure} AB
:layout-sm: AB
:gap: 8px
:subcaptions: below
:name: fig-interaction-spatial-xr_intro
:width: 80 %

```{image} fig/interaction-spatial-vr.png
:width: 90 %
:alt: 虚拟现实
```

```{image} fig/interaction-spatial-ar.png
:alt: 增强/混合现实 © HoloLens
```
虚拟现实与增强/混合现实。
````

通过这些技术，我们可以预见一个未来，在这个未来中，人们的学习、工作和娱乐方式将被彻底改变。虚拟现实与增强现实技术的发展不仅仅推动了技术界的边界，更拓展了我们对现实世界的理解和认知。

## 虚拟现实（VR）

<!-- ### 硬件：VR 头显 -->
### 用户位姿估计（User Position and Pose Estimation）

VR 应用使用的典型硬件是 VR 头显，并可能配备有手柄或外部摄像头等辅助设备。在虚拟现实应用中，对用户位置（position）和姿态（pose）的精确估计是实现高质量沉浸式体验的核心。其中，姿态指的是用户的朝向（orientation）。
<!-- 本节详细介绍度量自由度（DoF）、追踪技术、数据融合方法及其在实际设备中的应用。 -->
> Pose 一词在机器人学或计算机视觉等语境下也被当成“位姿”使用，包含位置和朝向两部分。在 VR 头显相关语境中，则常被用于仅指代姿态朝向。因此，在不同文献中，该词的具体指代需要结合上下文语境判断。

不同的 VR 设备的位姿测量的能力不同，对应着设备所配备的不同的自由度。自由度（Degrees of Freedom， DoF）指的是能够独立自由运动的参数的数目，如{numref}`fig-interaction-spatial-dof` 所示，一般设备的自由度有两种常用配置：
- 3度自由度（3-DoF）：此配置允许用户的头部在三个轴（俯仰、偏航、翻滚）上旋转，适合于静态体验，如观看虚拟现实影片或进行简单的查看任务。
- 6度自由度（6-DoF）：除了 3-DoF 提供的头部旋转外，6-DoF 还支持用户在空间中的前后、左右、上下移动，极大增强了交互性和沉浸感，允许用户在虚拟世界中自由行走和探索。

```{figure} fig/interaction-spatial-dof.png
:scale: 70 %
:name: fig-interaction-spatial-dof
自由度（DoF）示意图。
```
```{figure} fig/interaction-spatial-env_dof.png
:scale: 70 %
:name: fig-interaction-spatial-env_dof
配备不同自由度的 VR 设备，为用户提供不同程度的交互自由和沉浸式体验。
```

对于一个 6-DoF 的 VR 系统，如何定位 VR 用户的位姿？这需要用到追踪技术，主要分为外部引导（Outside-In）和内部引导（Inside-Out）两类。
```{figure} fig/interaction-spatial-tracking.png
:name: fig-interaction-spatial-tracking
追踪技术。
```

早期的 VR 系统，如 HTC Vive 和 Valve Index，采用的是外部引导技术，通过设置在环境中的外部传感器（通常是摄像头或红外传感器），捕捉穿戴设备上的特定标记或特征点，实现对用户动作的精确追踪。具体来说，分为以下两步：
- 特征点检测（Feature Detection）：外部传感器通过检测用户身上的特征点（如头戴显示器、控制器上的标记或传感器）来跟踪用户的位置和方向。这些传感器可以通过红外光、激光或其他方式识别特征点。
- 位姿估计（Pose Estimation）和追踪（Tracking）：基于传感器收集到的数据，系统会通过算法来估计用户的位置和姿态，并实时跟踪其变化。这些算法会结合外部传感器的数据，对用户的运动轨迹进行连续估计和调整。
```{figure} fig/interaction-spatial-vrheadset_feature.png
:width: 80 %
:name: fig-interaction-spatial-vrheadset_feature
VR 头显和手环上的红外光学特征点。
```
根据外部传感器探测到的特征点信息来估计用户位姿，所要求解的是一个多点透视问题（Perspective-n-Point，PnP）。

PnP 问题的基本任务是根据一组点在世界空间中的三维坐标和它们在相机拍摄的二维图像中的对应投影坐标，计算出相机或设备在世界空间中的位姿，如{numref}`fig-interaction-spatial-pnp` 所示。这一问题起源于相机校准，而后也被广泛用于计算机视觉和虚拟现实等领域。
在用户位姿估计任务中，系统使用已校准好的相机和预设的特征点，因此特征点在用户坐标系（即固连于头显设备的局部坐标系）中的位置和在相机屏幕上的像素位置均为已知，从而可以利用 PnP 问题求解出相机坐标系相对于用户坐标系的相对位姿，因此在相机固定（相机坐标系与世界坐标系的变换关系已知）的前提下，可以通过 PnP 求解出的相对位姿逆推出用户坐标系的位姿（该逆推变换本质上就是刚体坐标系之间的转换，因此不再赘述）。

```{figure} fig/interaction-spatial-pnp.png
:name: fig-interaction-spatial-pnp
:width: 60 %
PnP 问题。已知若干点在世界空间中的三维坐标（$\boldsymbol{c}_1-\boldsymbol{c}_4$）和在相机屏幕上的二维投影点位置（$\boldsymbol{u}_1-\boldsymbol{u}_4$），求解相机在世界坐标系中的位姿（位置 $\boldsymbol{t}$ 和旋转矩阵 $\boldsymbol{R}$）。
```
为了求解 PnP 问题，人们提出了不同的求解方法，下面我们将介绍由 Grunert 在1841年提出的经典求解方法。为了叙述简便，我们仍采用 PnP 问题的经典定义（{numref}`fig-interaction-spatial-pnp`），即，任务目标为计算出相机在世界空间中的位姿。
该方法分为两步，首先计算出相机与各特征点之间的距离，而后根据这些距离解出相机的位置 $\boldsymbol{X}_0$ 与姿态 $\boldsymbol{R}$。

````{subfigure} AB
:layout-sm: AB
:gap: 16px
:subcaptions: below
:name: fig-interaction-spatial-pnp_alg
:width: 80 %

```{image} fig/interaction-spatial-pnp_alg1.png
:alt: 任意两个特征点$\boldsymbol{X}_1,\,\boldsymbol{X}_2$和相机$\boldsymbol{X}_0$之间的相对关系。图中用绿色框出已知量，红色框出未知量。
```

```{image} fig/interaction-spatial-pnp_alg2.png
:alt: 三个特征点可以在两两组合后分别列出三个方程。
```
PnP 问题求解步骤1：计算出相机与各特征点之间的距离。
````

如{numref}`fig-interaction-spatial-pnp_alg` 所示，当 $n=3$ 时，P3P 问题是 PnP 问题的最小形式。记3个特征点为 $\boldsymbol{X}_1,\,\boldsymbol{X}_2,\,\boldsymbol{X}_3$。考察任两个特征点与相机之间的关系，如{numref}`fig-interaction-spatial-pnp_alg`左所示，首先，可以计算出两个特征点之间的距离 $c$，通过它们在相机屏幕上的对应像素位置计算出它们之间的夹角 $\gamma$，于是通过余弦定理可以得到：
$$s_1^2+s_2^2-s_1s_2\cos{\gamma}=c^2，$$
其中 $s_1,\,s_2$ 是特征点 $\boldsymbol{X}_1,\,\boldsymbol{X}_2$ 与相机 $\boldsymbol{X}_0$ 之间的距离，是待求的未知量。
如{numref}`fig-interaction-spatial-pnp_alg`右所示，P3P 问题中有三个未知量 $s_1,\,s_2,\,s_3$ 并可以列出三个方程，因此可以从中解出三个未知量。但该方程的解的个数是不唯一的，如{numref}`fig-interaction-spatial-pnp_4solu` 所示，故而通常至少需要再多使用一个特征点来消除不确定性并获得唯一解。当使用 $n>4$ 个点时，系统将可以获得更多的特征点对信息，并利用最小二乘（least sqaures）或随机抽样一致（Random sample consensus，RANSAC）等优化方法获得更精确且稳定的解，抵抗噪声和误匹配点等干扰。
```{figure} fig/interaction-spatial-pnp_4solu.png
:name: fig-interaction-spatial-pnp_4solu
:width: 60 %
P3P问题：求解特征点到相机的距离，可能存在 4 组可行解。
```
在解得特征点到相机的距离 $s_i,\,i = 1,2,\cdots,n$ 后，我们可以列出特征点从世界坐标系到相机坐标系中的转换关系：
$$s_i \boldsymbol{x}^\mathrm{cam}_i = \boldsymbol{R}(\boldsymbol{X}_i-\boldsymbol{X}_0)，$$
其中 $\boldsymbol{x}^\mathrm{cam}_i$ 是从相机位置 $\boldsymbol{X}_0$ 观察特征点 $\boldsymbol{X}_i$ 的方向向量，$\mathrm{cam}$ 表示该向量是相机坐标系中观察得到的。联立$i = 1,2,\cdots,n$对应的方程，将方程间两两相减可消去含 $\boldsymbol{X}_0$ 的项，可解出 $\boldsymbol{R}$ 后（类似于{numref}`sec-animation-elastomers-fem`中解算四面体的形变梯度），代回方程解出 $\boldsymbol{X}_0$。对 $n>4$ 个控制点，同样可以使用最小二乘法最小化投影误差从而解出 $\boldsymbol{R}$ 和 $\boldsymbol{X}_0$。
```{figure} fig/interaction-spatial-pnp_dlt.png
:name: fig-interaction-spatial-pnp_dlt
:width: 60 %
PnP 问题求解步骤2：恢复出相机的位姿。
```

基于外部传感器进行的位姿估计能提供高精度和低延迟的追踪，非常适合需要精确用户互动的高端VR应用。但其缺点是，外部传感器和设备安装复杂，整体设备成本也很高（通常超过$1500），并需要确保传感器覆盖区域与用户的活动区域相匹配，活动范围受限。

另一种估计用户位姿的方法是利用内部引导技术，使用这类技术的包括Oculus Quest设备、甚至部分非 VR 的移动设备等。这种技术不需要设置外部设备，而是通过使用设备本身集成的传感器（如摄像头、加速度计、陀螺仪等）来实时估计用户的 6-DoF 位姿。这种方法依赖于视觉惯性里程计（Visual Inertial Odometry, VIO）来快速、准确地推算用户的位置和方向：
- 视觉信息（Visual）：使用设备上的摄像头或传感器捕捉环境图像和环境特征点，并通过同步定位与地图构建（SLAM）算法来估算相机在环境中的位置和姿态。
- 惯性信息（Inertial）：通过加速度计和陀螺仪来测量设备的加速度和角加速度，推算出设备的运动方向和转向。
VIO技术融合了来自摄像头的**视觉信息**和来自加速度计与陀螺仪的**惯性信息**来更准确而稳定地估计用户的 6-DoF 位姿，视觉信息提供了设备相对于环境的空间定位，而惯性信息可以帮助修正由于快速运动或环境变化带来的误差。VIO技术可以在动态环境下快速响应用户的运动，提供连贯和平滑的用户体验。

内部引导追踪技术的所需硬件可以被集成在 VR 设备之中，不依赖外部传感器，无需复杂的安装过程，因此设备成本相对较低，且更便携、易于普及，这使得相关技术也可以被应用于平板、手机等移动设备中，并因此催生了一系列基于手机就可以完成的 VR、AR 应用。不过，由于视觉信息需要依赖环境中的特征点，若环境中缺乏足够的纹理或存在光照变化，内部引导技术可能出现精度下降或追踪失败等问题，精度和稳定性略逊于外部引导。

### 无限空间体验

虽然我们可以对用户的位置和姿态进行精确而快速的估计了，但由于用户所处的物理空间是有限的，如果要为用户创造广阔的虚拟世界，那么就还需创新技术，在有限物理空间的基础上，扩展用户感知的活动空间。本节将介绍如何通过技术设计实现虚拟空间的无限体验和对用户空间感知的巧妙操控。

```{figure} fig/interaction-spatial-virtuix_omni.png
:name: fig-interaction-spatial-virtuix_omni
全向跑步机 Virtuix Omni。
```

**全向跑步机**（Omnidirectional Treadmill），如Virtuix Omni（如{numref}`fig-interaction-spatial-virtuix_omni` 所示），提供了真实行走的体验而不离开原地，使得用户可以在物理空间受限的情况下，在虚拟环境中自由移动。这种设备是通过一个能够检测步伐方向和速度的低摩擦平台来实现的，用户佩戴专用鞋或滑动设备，可以在虚拟世界中360度的自由行走、跑步甚至旋转。但该技术系外部设备需求较高、价格昂贵，因此主要被应用于专业场地，且设备需要与用户接触，不能做到完全无感。

重定向行走（Redirected Walking）与空间重映射（Spatial Remapping）技术是一种创新的解决方案，利用用户在空间感知上的不精确性，通过微妙的视觉或运动提示让用户在虚拟世界中行走更远的距离，而实际上只在较小的物理空间中移动，如{numref}`fig-interaction-spatial-rdw` 所示。这种技术可以有效地扩展虚拟环境的探索范围，提高空间利用效率。

**重定向行走**技术的设计来源于人对自身位姿感知的不确定性和对视觉信息的依赖性，人通过需要视觉信息进行辅助获知自己的位姿改变情况，例如，让蒙上眼的人走直线或转特定角度总是困难的。而当分别来自视觉和运动速度等感官的信息发生冲突时，视觉通常会占据主导地位——视觉能欺骗大脑对自身运动的感知。
因此，基于一下两部分技术原理，VR 系统可以实现用户的重定向行走：
- 被动重定向（睁眼时）：当用户行走时，如果视觉和运动反馈之间的冲突非常小，用户几乎不会察觉到自己的空间感知被“欺骗”。例如，在用户转向时，系统可以巧妙地让他们多转一点，这种微调对于大多数人来说是无法察觉的。
- 主动重定向（眨眼或扫视时）：当用户的视觉暂时失效（如眨眼或扫视等动作）时，由于视觉注意力的转移，系统通过将虚拟世界中的画面稍作调整，使得用户产生一种“转多了”的错觉，从而下意识地做出相应的转向或行动，从而实现更大范围的空间调整。

```{figure} fig/interaction-spatial-rdw.png
:name: fig-interaction-spatial-rdw
:width: 80%
通过重定向行走 3.5 米 $\times$ 3.5 米的真实房间中记录的物理路径（蓝色曲线）和 6.4 米 $\times$ 6.4 米的合成空间中的虚拟路径（橙色曲线）的俯视图。{cite}`Sun2018TowardsVR`
```

用户进行低速运动时给系统提供了足够的重定向的余地，但当用户需要进行跑跳等快速运动时，在有限的物理空间中很容易撞上障碍物或墙壁。对此，一个可以累加在重定向行走技术之上的解决方案是空间重映射，如{numref}`fig-interaction-spatial-remapping` 所示，

**空间重映射**技术通过在虚拟空间和物理空间之间建立空间映射关系，将规整的物理空间及其边界与扭曲的虚拟空间及其边界相对应。映射过程需要尽量**保距**，即确保行走的距离不会被改变，因为人类对行走的距离有较为精确的感知；但不需要**保角**，因为人类对于转向角度的敏感度较低。因此，通过对虚拟空间的扭曲，系统在尽量不让用户察觉的情况下使虚拟环境与物理空间相匹配，同时保持较好的几何对齐。

更加智能化的空间重映射技术，将能够实时适应用户的行为和环境变化。通过集成更高级的传感技术和深度学习算法，系统可以更精确地预测用户的移动意图和可能路径，从而提前进行空间调整，确保虚拟环境的连贯性和真实感。此外，算法优化还需要考虑减少对用户认知和感知的干扰，使重定向行走更自然、不易被察觉。

```{figure} fig/interaction-spatial-remapping.png
:name: fig-interaction-spatial-remapping
虚拟空间扭曲映射。
```

在重定向行走的两项方案中，被动式重定向限制于用户自身的转向行为，因此主动式重定向是空间调整的重点。主动式重定向在用户在感知失明时进行空间调整：利用高级眼动追踪技术，系统可以在用户眨眼（瞳孔的瞬间遮挡或缩小）或扫视（瞳孔在短时间内的快速偏移）时精确地检测到这一行为，并且可以根据虚拟世界探索需要或现实空间中的障碍物情况规划重定向路径，随后实时调整虚拟环境的方向或位置。

另外，如{numref}`fig-interaction-spatial-sgd` 所示，系统还可以使用微妙视线诱导（Subtle Gaze Direction，SGD）技术，通过在用户的视野外围的某些区域进行细微调整，诱导用户产生扫视行为。这不仅可以用于大型展览中心引导参观者的视线，还可以在VR中应用，通过控制视线方向和扫视行为来调整用户在虚拟环境中的方向和位置。

```{figure} fig/interaction-spatial-sgd.png
:width: 80%
:name: fig-interaction-spatial-sgd
SGD 方法。
```
### 未来发展

**设备精确性与反应速度的提高** ：随着硬件技术的进步，未来的 VR 设备将提供更高的精确性和更快的反应速度。这包括更高分辨率的眼动追踪系统、更灵敏的运动传感器以及更快速的处理器，这些都是实现复杂空间重映射技术的关键。高精度的传感器和快速的反应能力能够确保虚拟环境中的任何微小调整都即时且精确地反映用户的实际动作，增强沉浸感和现实感。

**用户体验的舒适性和自然性** ：提高用户体验的舒适性和自然性是VR技术发展的另一个重要方向。这不仅涉及硬件设计的人体工程学优化，如更轻便的头显和更适合长时间佩戴的材料，还包括软件界面的用户友好性改进。例如，通过改进用户界面（UI）和用户体验（UX）设计，使得用户在进行复杂的虚拟操作时感觉更直观和轻松。此外，对VR环境的声音、光影和质感进行真实的模拟，也是提升自然性的关键。

**综合应用和跨领域融合** ：随着 VR 技术的成熟，其应用领域将进一步扩展，不仅限于娱乐和游戏，还将深入到教育、训练、医疗和工业设计等多个领域。跨领域的融合将推动 VR 技术与其他先进技术如人工智能、大数据和物联网的结合，共同创造出全新的应用场景和用户体验。

## 增强/混合现实
<!-- Orion has the largest field of view in the smallest AR glasses form to date. That field of view unlocks truly immersive use cases for Orion, from multitasking windows and big-screen entertainment to life-size holograms of people – all digital content that can seamlessly blend with your view of the physical world.
But what makes Orion unique is that it is unmistakably a pair of glasses in both look and feel – complete with transparent lenses. Unlike MR headsets or other AR glasses today, you can still see other people’s eyes and expressions, so you can be present and share the experience with the people around you.
According to The Verge, producing a unit costs about $10,000, with much of that cost coming from its silicon carbide lenses. For now, Meta is using them for internal development and external demos while working on more commercially viable versions for the future. -->
虚拟-现实融合是增强现实（AR）和混合现实（MR）中的关键技术，目标是将虚拟物体无缝、自然地集成到现实环境中。这一过程涉及多个层面的技术挑战，包括光影一致性、几何一致性和交互一致性，所有这些都依赖于精确的三维注册技术。

**三维注册** （如{numref}`fig-interaction-spatial-3Dregistration` 所示）是将虚拟物体准确地放置和定位于现实世界的过程，涉及环境感知与建模、虚拟对象定位与对齐等任务。它的核心目标是确保虚拟内容能够自然地与现实环境相结合，从而提供更加沉浸的体验。

```{figure} fig/interaction-spatial-3Dregistration.png
:name: fig-interaction-spatial-3Dregistration
三维注册。
```

**光影一致性** ：如{numref}`fig-interaction-spatial-lighting_consistency` 所示，光影一致性指的是确保虚拟物体在现实世界中的光照效果与其周围环境匹配，从而增强真实感。实现光影一致性通常涉及以下技术：
- 光照重建：使用传感器捕捉现场的光照条件，例如光强度和方向，然后在渲染虚拟物体时模拟这些光照条件。
- 真实感渲染：采用高级渲染技术，如光线追踪或全局光照算法，确保虚拟物体的阴影和高光与现实环境中的光线完美融合。

```{figure} fig/interaction-spatial-lighting_consistency.png
:name: fig-interaction-spatial-lighting_consistency
光影一致性。
```

**几何一致性** ：如{numref}`fig-interaction-spatial-geometry_consistency` 所示，几何一致性指的是确保虚拟物体与现实环境之间的空间关系准确无误，尤其是遮挡和相对位置的正确性。为了实现这一目标，系统需要充分理解和利用环境的三维几何信息，例如场景的深度数据和结构。
尺寸、位置和方向准确无误。这需要精确的物体位姿估计与跟踪、场景多属性建模以及场景理解。技术实现通常包括：

```{figure} fig/interaction-spatial-geometry_consistency.png
:name: fig-interaction-spatial-geometry_consistency
几何一致性。
```
**交互一致性**：如{numref}`fig-interaction-spatial-interaction_consistency` 所示，交互一致性指的是确保虚拟物体能够正确响应来自用户和环境的交互行为，保证虚拟物体在与现实世界互动时符合物理规律（如图左，弹弓和小球弹道的运动需要符合固体力学）和场景语义（如图右，虚拟人需要正确行走在地面上）。交互一致性的实现依赖于以下多项技术：
- 物体位姿估计与跟踪：使用各种传感器和算法持续跟踪虚拟物体在空间中的位置和姿态，确保其与现实世界中的对象保持准确的相对位置，避免虚拟物体与现实场景产生不自然的偏差。
- 场景理解与场景多属性建模：通过高级的视觉和数据处理算法可以分析环境数据，识别和解释物理空间的布局和物理属性（如材质、结构、光反射特性），从而正确地建立包含各种物理属性和视觉属性的虚拟世界场景模型。有了对现实环境的正确认识，系统才能令虚拟物体在交互时做出与现实环境相匹配的反馈行为。
- 物理仿真：在虚拟物体与现实世界交互时，确保其行为符合物理规律，如碰撞、重力和材料互动。这不仅增强了虚拟物体的真实感，也使用户的交互更加自然和可预测。
````{subfigure} AB
:layout-sm: AB
:gap: 8px
:subcaptions: below
:name: fig-interaction-spatial-interaction_consistency
:width: 80 %

```{image} fig/interaction-spatial-3Dregistration_spring.png
:alt: 与虚拟的弹弓进行交互。
```

```{image} fig/interaction-spatial-3Dregistration_drive.png
:alt: 在包含虚拟元素的场景中交互。
```
交互一致性。
````

深入的场景理解能够支持更复杂的交互，包括物理仿真，这是实现几何一致性和交互一致性的关键。这也对 AR/MR 技术和设备算力提出了要求。
实时交互对系统的响应速度要求极高，任何延迟都可能打破用户的沉浸感。但不论是场景多属性建模还是物理仿真，要做到实时仍然是值得深入研究的挑战。优化系统架构和算法以提升交互效率、减少交互延迟，是提升用户体验的关键。

未来，随着计算能力的提升和算法的优化，虚拟-现实融合技术将更加成熟，实现更加自然和无缝的融合，促进 AR/MR 设备的实用和普及。这将推动从娱乐和游戏到教育、工业和医疗等多个领域的革新，开辟虚拟和现实交互的新时代。
