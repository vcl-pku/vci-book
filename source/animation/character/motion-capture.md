(sec-animation-character-motion_capture)=
# 动作捕捉

当我们有一个虚拟角色和它的骨骼框架以后，一个很直接的让其动起来的方法，就是手动指定每个关节的弯曲程度。整个过程就像操控一个玩具小人一样，我们将其摆成我们想要的姿势。然而这样只能得到一个静态的姿势，如何产生整个的运动呢？如果能结合之前讲过的插值内容，可以发现做法也是很简单的：我们把几个关键的姿势摆出来，通过插值产生姿势之间的切换，如{numref}`fig-animation-character-motion_inbetween`。

```{figure} fig/animation-character-motion_inbetween.png
:width: 80 %
:name: fig-animation-character-motion_inbetween

通过蓝色关键帧和插值算法得到的角色动画[^fig-animation-character-motion_inbetween-ref]
```

[^fig-animation-character-motion_inbetween-ref]: 图片来源：[Robust Motion In-betweening](https://arxiv.org/pdf/2102.04942.pdf)

然而这样的方法只适用于大范围的，非精细的运动。由插值产生的动作往往较为平滑，缺少细节和风格。在一些快速的多变的运动中，我们需要非常多的关键帧才能确保动画的质量，而这会导致我们的工作量大幅度上升。

这时我们就要依赖另一个产生动作数据的重要方法：动作捕捉（motion capture），一般读为“Mocap”。动作捕捉是通过设备记录人和物体运动的方法。就角色来说，我们需要一些专业的动捕演员，让其穿戴特定的设备进行表演。在每一时刻，演员的肢体运动甚至面部表情会都会被设备记录下来，转化成骨骼的旋转数据，记录完毕后将其交给后续的处理流程。

```{figure} fig/animation-character-mocap.png
:width: 80 %
:name: fig-animation-character-mocap

动捕演员[^fig-animation-character-mocap-ref]
```

[^fig-animation-character-mocap-ref]: 图片来源：[Squeeze](https://www.squeezestudio.com/en/projects/motion-capture)

相比于插值动画，动捕数据由于是对演员的动作进行了密集的捕捉，可以较为简单地获得非常风格化和流程的动作。动作捕捉在如今有非常多的应用，下面列出了几个主要的方面：
- 休闲娱乐：如游戏、影视、虚拟偶像、元宇宙。
- 体育运动：如运专业体育训练、演出动作的优化。
- 医疗：用于帮助医生诊断、治疗一些与运动相关的疾病，以及受伤复建等。
- 机器人：例如对无人机、机械臂的跟踪和定位。

在进行动作捕捉时，我们需要一些设备来完成动作的提取和转化，根据不同的原理，我们可以将设备进行分类，我们将在下面的章节对这些设备进行简单的介绍。

## 外骨骼

基于外骨骼（exoskeleton）的动捕设备是一种早期较为常用的动捕设备，如{numref}`fig-animation-character-exoskeleton` 所示。外骨骼设备的原理十分简单，由于动捕演员穿戴了一套外骨骼，演员的肢体动作会带动外骨骼运动，通过测量外骨骼各关节的角度来近似人体上对应关节的角度；在拥有各关节角度之后，结合外骨骼设备的内参（如每个部件的长度等），我们就可以利用 {numref}`sec-animation-kinematic_principles-kinematics-forward` 中的方法还原人体的动作了。

```{figure} fig/animation-character-exoskeleton.png
:width: 100 %
:name: fig-animation-character-exoskeleton

基于外骨骼的动捕设备
```

基于外骨骼的动捕技术最大的问题在于穿戴的设备特别妨碍动捕演员做动作，当我们需要做一些比较难或者比较危险的动作时（比如躺在地上）穿着外骨骼就很难实现。但另一方面，外骨骼技术非常适用于手部动作的采集，因为手相对身体比较小，采用外骨骼技术能够获得更加准确的数据。

## 惯性传感器

基于惯性传感器的动捕技术（如{numref}`fig-animation-character-inertial_mocap`）主要依赖于惯性测量单元（inertial measurement unit，IMU），它一般是一个六轴传感器，包括 $3$ 自由度的加速度计（accelerometers）和 $3$ 自由度的角速度计（gyroscope）。通过这些传感器的信息，我们可以得到人体各部位的相对运动，进而使用逆向运动学（{numref}`sec-animation-kinematic_principles-kinematics-backward`）或者优化的方法来求解每个关节的旋转。

```{figure} fig/animation-character-inertial_mocap.png
:width: 100 %
:name: fig-animation-character-inertial_mocap

基于惯性传感器的动捕技术
```

基于惯性传感器的动捕技术存在的一个不可避免的问题就是传感器的漂移。由于惯性传感器测量的是加速度或者速度，为了得到位置，需要对加速度或速度进行积分，而随着时间的推移，这个积分的误差会累积，导致得到的位置关系越来越不准确。在实践中，常常会因此看到人物会飘起来或者陷进地面。我们往往会借助其他技术来减少漂移带来的影响，比如一些启发性的辅助措施，例如我们可以借助“人的脚总是接触地面”这个先验知识来对整个人体的位姿加一个修正项；另外一方面我们也可以使用更精确的或者添加更多的传感器来减小积分时产生的误差，例如可以借助重力传感器来避免在竖直方向产生过大的漂移，类似还可以借助磁场传感器、光流传感器等。

## 光学动捕

### 多视角重建

### 标记点的丢失

### 无标记点的光学动捕

#### 基于深度相机的无标记点光学动捕

## 其他运动估计方法

### 基于单视角视频的运动估计

### 使用少量传感器进行运动估计
