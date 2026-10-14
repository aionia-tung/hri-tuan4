# Thu muc maps

Dat ban do da luu bang SLAM Toolbox vao thu muc nay:

```text
map.yaml
map.pgm
```

Sau khi mapping xong, co the copy tu workspace bang:

```bash
cp ~/tb4_ws/maps/map.yaml ./maps/map.yaml
cp ~/tb4_ws/maps/map.pgm ./maps/map.pgm
```

Hoac luu truc tiep vao repository:

```bash
cd /home/aionia/tb4_maps/maps
ros2 run nav2_map_server map_saver_cli -f map
```

Neu robot khong hien tren map khi chay Nav2, kiem tra:

- `map.yaml` co ton tai.
- `map.pgm` co ton tai.
- Dong `image:` trong `map.yaml` la `image: map.pgm`.
- RViz2 Fixed Frame la `map`.
- Da bam **2D Pose Estimate** dung vi tri robot trong Gazebo.
