# Quy trinh tao map thuc nghiem

Chay cac terminal theo thu tu sau.

## Terminal 1 - Build va source package

```bash
cd /home/aionia/tb4_maps
source /opt/ros/humble/setup.bash
colcon build --packages-select tb4_maps
source install/setup.bash
```

## Terminal 2 - Chay simulation kem SLAM

```bash
cd /home/aionia/tb4_maps
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch tb4_maps tb4_slam.launch.py
```

Mo RViz2 va quan sat map dang duoc tao.

Mac dinh package dung world `depot` vi nhe hon `maze`. Neu can dung world khac:

```bash
ros2 launch tb4_maps tb4_slam.launch.py sim_world:=warehouse
ros2 launch tb4_maps tb4_slam.launch.py sim_world:=maze
```

## Terminal 3 - Teleop

```bash
source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Di chuyen robot cham qua cac hanh lang. Neu map bi lech tuong, quay robot cham hon va tranh va cham vao tuong.

## Terminal 4 - Luu map

Khi map da on dinh:

```bash
source /opt/ros/humble/setup.bash
mkdir -p /home/aionia/tb4_maps/maps
cd /home/aionia/tb4_maps/maps
ros2 run nav2_map_server map_saver_cli -f map
```

Can co hai file:

```text
/home/aionia/tb4_maps/maps/map.yaml
/home/aionia/tb4_maps/maps/map.pgm
```

Kiem tra:

```bash
ls -lh /home/aionia/tb4_maps/maps/map.*
cat /home/aionia/tb4_maps/maps/map.yaml
```
