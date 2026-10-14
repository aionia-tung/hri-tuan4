# Quy trinh localization va Nav2

Sau khi da co `maps/map.yaml` va `maps/map.pgm`, chay cac buoc sau.

## Terminal 1 - Chay Nav2

```bash
cd /home/aionia/tb4_maps
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch tb4_maps tb4_nav2.launch.py map:=/home/aionia/tb4_maps/maps/map.yaml
```

Lenh tren mac dinh mo lai world `depot`. Neu ban do duoc tao trong world khac, phai chay dung world do:

```bash
ros2 launch tb4_maps tb4_nav2.launch.py \
  sim_world:=maze map:=/home/aionia/tb4_maps/maps/map.yaml
```

## RViz2 - Hien robot tren map

1. Dat **Fixed Frame** la `map`.
2. Bat display **Map**, **RobotModel**, **LaserScan**, **TF**, **Global Costmap**, **Local Costmap**.
3. Chon **2D Pose Estimate**.
4. Click va keo mui ten tai dung vi tri robot trong Gazebo.
5. Doi den khi laser scan trung voi tuong tren map.

Neu robot van khong hien trong map:

```bash
ros2 topic echo /map --once
ros2 topic echo /amcl_pose --once
ros2 run tf2_ros tf2_echo map base_link
ros2 run tf2_ros tf2_echo odom base_link
```

Loi thuong gap:

- Chua co `maps/map.yaml` hoac `maps/map.pgm`.
- `map.yaml` tro den sai ten anh, vi du `image: maze_map.pgm` nhung file thuc te la `map.pgm`.
- RViz2 Fixed Frame khong phai `map`.
- Chua bam **2D Pose Estimate**, nen AMCL chua tao transform `map -> odom`.
- Robot spawn o vi tri khac so voi luc tao map, can set pose ban dau dung hon.

## Gui Nav2 Goal

Dung cong cu **Nav2 Goal** va dat it nhat 03 goal o cac khu vuc khac nhau. Sau khi dat goal, khong dieu khien robot bang teleop.
