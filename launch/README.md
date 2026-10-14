# Thu muc launch

Bai nay co the su dung launch file trong package `tb4_maps`:

```bash
ros2 launch tb4_maps tb4_simulation.launch.py
ros2 launch tb4_maps tb4_slam.launch.py
ros2 launch tb4_maps tb4_nav2.launch.py map:=/home/aionia/tb4_maps/maps/map.yaml
```

Ba file launch nay chi include lai launch file chinh thuc cua TurtleBot 4, khong tu viet lai simulator hay controller.
