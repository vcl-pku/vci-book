# 本章小结

## 习题

1. 设场景中障碍物的有符号距离场为 $\phi(x,y,z)=\sqrt{x^2+y^2+z^2}-1$，质点 $A$ 的位置 $\boldsymbol x_A=(0.7,-0.4,0.6)$，速度 $\boldsymbol v_A=(0,1,-1)$，质点 $B$ 的位置 $\boldsymbol x_B=(-0.99,0,0)$，速度 $\boldsymbol v_B=(1,1,0)$。回答如下问题：
   - 质点 $A$ 和 $B$ 是否与障碍物发生碰撞？
   - 质点质量均为 $m=1$，设时间步长 $h=0.01$，摩擦系数 $\mu=0.5$，按照惩罚方法进行碰撞处理，惩罚力的系数 $k=100$，求出两个质点在一个时间步后的速度。（场景中不存在其它外力）
2. 设两刚体 $A$ 和 $B$ 的角速度分别为 $\boldsymbol\omega_1$ 和 $\boldsymbol\omega_2$，求证：$A$ 相对 $B$ 的角速度为 $\boldsymbol\omega_1-\boldsymbol\omega_2$。
3. 请解释为何用约束表示关节的方法可能出现模拟过程中关节错位的现象。（提示：不妨举个例子尝试一下）
4. 考虑{numref}`fig-animation-rigid_bodies-joints` 中的合页关节，设刚体 $1$ 与刚体 $2$ 的质心位置分别为 $\boldsymbol x_1=(x_1,y_1,z_1)^\top$、$\boldsymbol x_2=(x_2,y_2,z_2)^\top$，旋转矩阵分别为 $\boldsymbol R_1$、$\boldsymbol R_2$，两刚体的质心与关节的中心共面，关节角为 $\theta$，刚体 $1$ 和 $2$ 的质心到关节中心的距离分别为 $l_1$ 和 $l_2$。我们使用欧拉角的方式表示刚体 $1$ 的旋转，旋转顺序为 $ZYX$，角度分别为 $\theta_Z$、$\theta_Y$、$\theta_X$。在 $\theta_Z=\theta_Y=\theta_X=0$ 时，合页关节的旋转轴为 $y$ 轴正方向，且与刚体 $1$ 和关节中心连线垂直；$\theta=0$ 时两刚体质心与关节中心三点共线，且两刚体质心不重合。现在选取广义坐标为 $(x_1,y_1,z_1,\theta_Z,\theta_Y,\theta_X,\theta)$，请用广义坐标表示出 $\boldsymbol x_1$、$\boldsymbol x_2$、$\boldsymbol R_1$ 和 $\boldsymbol R_2$。

## 参考文献

```{bibliography} ref.bib
```