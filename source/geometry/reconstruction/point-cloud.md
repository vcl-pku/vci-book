(sec-geometry-reconstruction-pcd)=
# 点云的获取与配准

经典的点云重建方法往往依赖深度相机直接感知三维空间中的深度信息，得到深度信息后，通过相机投影的逆变换，就可以将深度值转换为三维坐标，从而得到点云。实际重建过程中，深度相机往往需要围绕场景进行连续的拍摄，在此过程中还会涉及到对不同区域之间的点云进行配准的问题。本节将首先介绍深度相机的原理，随后介绍一种点云配准的经典算法。

## 深度相机

深度相机是一类能够感知物体到相机距离的设备。传统相机捕捉到的图像中，每个像素保存的信息为 RGB 三通道组成的颜色属性；深度相机则会捕捉到一组深度图（depth map），其中每个像素保存了深度属性，描述物体表面到相机平面的距离。经过投影的逆变换过程，这些深度属性能够转化为三维空间中的位置，从而得到场景或物体的点云。

深度相机可以根据原理分为三种：

1. 基于结构光的深度相机。这一类深度相机主动发射一束具有特定图案的红外光照亮物体表面，随后从红外传感器捕捉到反射回来的红外光。由于物体表面的反射，返回的红外光中，原本的图案已经发生了畸变；通过分析接收到的图案，内置的算法能够计算得到目标对象的深度信息。基于结构光的深度相机在近距离能取得较高的精度，然而由于其需要主动发射红外光的特性，在环境光较强、拍摄范围较远的室外场景下难以使用。

2. 基于光程（Time of Flight，ToF）的深度相机。与结构光类似，这一类深度相机同样主动发射红外光照射物体表面；不同的是，结构光利用图案的畸变进行深度测算，而这一类深度相机利用光程，即光的飞行时间来确定与目标物体之间的距离。同样，在环境光较强的室外场景下，基于光程的深度相机会受到较为严重的干扰。

3. 基于立体视觉的深度相机。这一类深度相机依赖双目摄像头，通过在左右两个摄像头捕捉到的图像之间计算视差，内置的算法能够根据视差估计得到图像的深度信息。基于立体视觉的深度相机不主动对外发射光，而是被动地依赖双目视差工作，因此也被称为被动深度相机。相比于另外两种主动发射光的深度相机，基于立体视觉的深度相机对环境光不敏感，能够在室外工作；然而，由于其依赖双目图像之间的特征匹配，对于无纹理或弱纹理的纯色区域，容易得到误差较大的深度估计结果。

(chap-geometry-reconstruction-icp)=
## 点云的配准：ICP 算法

在几何重建中，我们往往会对同一个场景的不同区域分别采集点云数据，每个局部点云都需要通过点云配准过程融合进全局坐标系中，才能得到完整的最终结果。

```{figure} fig/icp.png
:name: fig-geometry-reconstruction-icp
:width: 60%

左图：同一场景中的两组待对齐的点云；右图：通过 ICP 算法成功对齐后的结果 [^icp]。
```

[^icp]: [Wikipedia: Point-set registration](https://en.wikipedia.org/wiki/Point-set_registration)

下面我们给出一种最经典的点云注册算法：ICP 算法（Iterative Closest Point）。如 {numref}`fig-geometry-reconstruction-icp` 所示，ICP 算法根据两组点云之间的形状匹配关系，计算出它们之间的相对变换，从而实现点云之间的融合配准。

### ICP 流程

ICP 算法迭代地估计点云之间的相对变换。具体来说，给定待变换点云 $S$ 和目标点云 $T$，ICP 算法估算一组旋转平移变换 $R,t$，使得点云 $S$ 经过该变换后，最大程度地与点云 $T$ 对齐。具体流程如下：

1. 首先，算法通过主成分分析（PCA），初始化一组旋转平移变换 $R,t$，作为待估计的相对变换；
2. 将这组变换应用于点云 $S$，$S$ 中每个点 $p_i$ 变换后得到 $p'_i=Rp_i+t$ ，然后为变换后的每一个 $p'_i$ 找到它在目标点云 $T$ 中的最近点 $q_i$，如此将 $S$ 和 $T$ 中的点两两匹配起来；
3. 对于每一对匹配点，如果它们之间的距离太远（例如大于所有匹配点距离中位数的若干倍），则丢弃这一组匹配对；
4. 在余下的 $N$ 对匹配 $\{(p'_j, q_j)|j=1,...,N\}$ 中，构造累计误差函数：

    $$
    E=\sum_j\left|p'_j-q_j\right|^2=\sum_j\left|Rp_j+t-q_j\right|^2\,.
    $$ (eq-geometry-reconstruction-icp-error)

5. 通过奇异值分解（SVD）求解合适的 $R,t$，使得该误差函数最小；
6. 重复2-5步直到误差小于特定阈值或者迭代次数超过上限。

下面我们将具体阐述算法中两个关键的步骤：PCA 初始化和 SVD 最小化误差。

### PCA 初始化

PCA 全称主成分分析（Principal Component Analysis），可以用来求解数据的“轴”。

我们考虑一组点 $p_1,...,p_N$ 及其中心坐标 $c=\frac1N\sum_{i=1}^Np_i$。

构造矩阵 $P_{3\times n}$，使其第 $i$ 列为 $p_i-c$。

构造协方差矩阵 $M=P\times P^T$，$M$ 的特征向量即代表了数据的“主成分”。对于二维数据，$M$ 的两个特征向量表示数据的两条轴线：对应最大特征值的那个特征向量表示，数据在这个方向上的分布最分散（数值变化最大）；对应最小特征值的那个特征向量表示，数据在这个方向上的分布最集中（数值变化最小）。对于三维数据亦是同理。

由于这些轴都是正交的，因此我们可以通过分别对两组点云进行主成分分析，然后寻找一个变换来对齐它们的这些轴线，即能得到一组粗略的初始化变换。

具体地，对于两组点云 $S,T$，它们的中心分别是 $c_S,c_T$，首先我们将点云 $S$ 平移 $c_T-c_S$，然后找到一个旋转矩阵 $R'$ 使得两组点云的轴分别对齐，则最终得到的变换就是：

$$
R=R', t=c_T-R'\times c_S\,.
$$ (eq-geometry-reconstruction-icp1)

即，对于 $S$ 中的每个点 $p_i$，我们都可以通过应用这个变换得到对齐后的位置：

$$
p_i'=R\times p_i + t=c_T+R\times(p_i-c_S)\,.
$$ (eq-geometry-reconstruction-icp2)

至此，算法找到了一组初始的 $R,t$，接着便可以执行后续步骤。

### 奇异值分解

当我们已经找到了一系列的点对 $(p_j,q_j)$ 时（其中 $p_j$ 来自点云 $S$，$q_j$ 来自点云 $T$），便需要估算合适的 $R,t$ 来最小化式 {eq}`eq-geometry-reconstruction-icp-error` 中的误差函数。由于该误差函数恰好具有二次形式，可以将该误差函数的最小化问题视作一个最小二乘估计问题，从而能够使用奇异值分解（SVD）来求解。具体来说：

1. 首先，构造矩阵 $P$，使得其第 $j$ 列为 $p_j-c_S$；构造矩阵 $Q$，使得其第 $j$ 列为 $q_j-c_T$。

2. 随后，构造协方差矩阵：

    $$
    M=P\times Q^T\,.
    $$ (eq-geometry-reconstruction-icp3)

3. 计算 $M$ 奇异值分解：

    $$
    M=U\times\Sigma\times V^T\,.
    $$ (eq-geometry-reconstruction-icp4)

4. 则，旋转矩阵可以表示为：

    $$
    R=V\times U^T\,.
    $$ (eq-geometry-reconstruction-icp5)

5. 此时，使误差函数最小的 $R,t$ 可以表示为：

    $$
    R=V\times U^T,t=c_T-R\times c_S\,.
    $$ (eq-geometry-reconstruction-icp6)
