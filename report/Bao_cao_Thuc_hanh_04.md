# Bao cao Bai Thuc Hanh 04 - TurtleBot 4 Simulation, SLAM va Nav2

## 1. Muc tieu

Bai thuc hanh su dung TurtleBot 4 trong moi truong mo phong Gazebo de kiem tra cac topic co ban, xay dung ban do bang SLAM Toolbox, luu ban do, load lai ban do de localization bang AMCL va thuc hien autonomous navigation voi Nav2.

Moi truong duoc su dung la world `maze` cua TurtleBot 4 Simulator tren ROS 2 Humble.

## 2. Moi truong thuc hien

- He dieu hanh: Ubuntu 22.04 LTS.
- ROS: ROS 2 Humble Desktop.
- Simulator: Ignition Gazebo.
- Robot: TurtleBot 4 standard.
- World: `maze`.
- Package chinh: `turtlebot4_ignition_bringup`, `turtlebot4_navigation`, `slam_toolbox`, `nav2_map_server`, `nav2_amcl`, `nav2_bt_navigator`.

## 3. Cau truc repository

```text
tb4_maps/
├── package.xml
├── setup.py
├── launch/
│   ├── tb4_simulation.launch.py
│   ├── tb4_slam.launch.py
│   └── tb4_nav2.launch.py
├── maps/
│   ├── map.yaml
│   └── map.pgm
├── report/
│   ├── Bao_cao_Thuc_hanh_04.md
│   └── Bao_cao_Thuc_hanh_04.pdf
└── readme.md
```

Repository co package ROS 2 `tb4_maps`. Cac launch file trong package chi include lai launch file co san cua TurtleBot 4, dung theo yeu cau khong can tu xay dung simulator hoac controller.

## 4. Cac lenh chay chinh

Chay mo phong:

```bash
ros2 launch tb4_maps tb4_simulation.launch.py
```

Chay mo phong kem SLAM:

```bash
ros2 launch tb4_maps tb4_slam.launch.py
```

Luu ban do:

```bash
ros2 run nav2_map_server map_saver_cli -f map
```

Chay localization va Nav2 voi ban do da tao:

```bash
ros2 launch tb4_maps tb4_nav2.launch.py map:=/home/aionia/tb4_maps/maps/map.yaml
```

## 5. Kiem tra TurtleBot 4 Simulation

Sau khi khoi chay simulation, robot TurtleBot 4 xuat hien trong Gazebo va RViz2 hien thi robot model, TF, du lieu laser scan. Cac topic co ban duoc kiem tra nhu sau:

```bash
ros2 topic echo /scan --once
ros2 topic echo /odom --once
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

Ket qua mong doi:

- `/scan` publish du lieu `sensor_msgs/msg/LaserScan`.
- `/odom` publish du lieu `nav_msgs/msg/Odometry`.
- `/cmd_vel` nhan lenh `geometry_msgs/msg/Twist` va robot di chuyen trong Gazebo.

## 6. Qua trinh xay dung ban do

SLAM Toolbox nhan du lieu LiDAR tu `/scan`, odometry tu `/odom` va TF cua robot de xay dung ban do occupancy grid. Robot duoc dieu khien bang `teleop_twist_keyboard` de di qua cac hanh lang trong world maze.

Trong qua trinh mapping, robot di chuyen voi toc do cham va re cua tu tu de giam sai so scan matching. Khi robot quay lai cac khu vuc da di qua, SLAM Toolbox thuc hien loop closure de giam sai so tich luy va lam ban do on dinh hon.

Ban do sau khi hoan thanh duoc luu bang:

```bash
ros2 run nav2_map_server map_saver_cli -f map
```

Hai file ket qua:

- `map.yaml`: chua thong tin resolution, origin, threshold va ten anh map.
- `map.pgm`: anh raster occupancy grid bieu dien tuong, vat can va vung trong.

## 7. Localization

Sau khi tao ban do, SLAM duoc dung lai. Nav2 load ban do bang `map_server`, sau do AMCL duoc su dung de uoc luong vi tri robot tren ban do.

Tren RViz2, cong cu **2D Pose Estimate** duoc dung de thiet lap pose ban dau. Khi cac tia laser `/scan` trung voi cac tuong tren ban do, robot da duoc localization thanh cong. AMCL tiep tuc cap nhat pose robot dua tren so khop giua laser scan hien tai va map tinh.

## 8. Navigation voi Nav2

Sau khi localization dung, cong cu **Nav2 Goal** trong RViz2 duoc dung de gui goal. Nav2 thuc hien pipeline:

1. `bt_navigator` nhan goal va dieu phoi qua trinh navigation.
2. `nav2_planner` tao global path tu vi tri hien tai den goal.
3. `nav2_costmap_2d` tao global costmap va local costmap de bieu dien vat can, tuong va vung an toan.
4. `nav2_dwb_controller` tinh lenh van toc cuc bo de robot bam theo path va tranh va cham.
5. Lenh dieu khien duoc publish len `/cmd_vel`.

Trong video demo can thuc hien it nhat 03 goal o cac khu vuc khac nhau. Sau khi dat goal, robot tu lap ke hoach va di chuyen, khong dieu khien bang teleop.

## 9. Cac node, package va topic chinh

| Thanh phan | Package / Node | Vai tro |
| :--- | :--- | :--- |
| Simulation | `turtlebot4_ignition_bringup` | Khoi chay TurtleBot 4 trong Gazebo |
| LiDAR | Gazebo sensor plugin | Publish `/scan` |
| Odometry | TurtleBot 4 control/simulation | Publish `/odom` |
| Teleoperation | `teleop_twist_keyboard` | Gui lenh van toc len `/cmd_vel` |
| SLAM | `slam_toolbox` | Xay dung ban do `/map` |
| Map server | `nav2_map_server` | Load va publish static map |
| Localization | `nav2_amcl` | Uoc luong pose robot tren map |
| Planner | `nav2_navfn_planner` | Tao global path |
| Controller | `nav2_dwb_controller` | Tao lenh dieu khien cuc bo |
| Costmap | `nav2_costmap_2d` | Bieu dien vat can va vung an toan |

| Topic | Kieu du lieu | Y nghia |
| :--- | :--- | :--- |
| `/scan` | `sensor_msgs/msg/LaserScan` | Du lieu LiDAR |
| `/odom` | `nav_msgs/msg/Odometry` | Odometry robot |
| `/cmd_vel` | `geometry_msgs/msg/Twist` | Lenh van toc |
| `/map` | `nav_msgs/msg/OccupancyGrid` | Ban do occupancy grid |
| `/tf`, `/tf_static` | `tf2_msgs/msg/TFMessage` | Bien doi he toa do |
| `/amcl_pose` | `geometry_msgs/msg/PoseWithCovarianceStamped` | Pose do AMCL uoc luong |
| `/plan` | `nav_msgs/msg/Path` | Duong di toan cuc |

## 10. Hinh anh minh hoa

Can chen cac hinh sau vao ban PDF cuoi cung:

- Hinh Gazebo hien thi TurtleBot 4 trong world maze.
- Hinh RViz2 hien thi robot va LiDAR scan.
- Hinh qua trinh SLAM dang xay dung map.
- Hinh ban do 2D hoan chinh.
- Hinh localization sau khi load lai map.
- Hinh Nav2 Goal voi global path, local costmap va robot dang di chuyen.

## 11. Ket luan

Bai thuc hanh da thuc hien day du pipeline co ban cua mobile robot trong ROS 2: mo phong, doc sensor, dieu khien van toc, SLAM mapping, luu ban do, localization va autonomous navigation. TurtleBot 4 co the tu lap ke hoach va di chuyen den cac goal khac nhau trong world maze bang Nav2 ma khong can dieu khien thu cong sau khi goal duoc gui.

## 12. Link nop bai

- Video demo Google Drive: TODO
- GitHub repository: TODO
