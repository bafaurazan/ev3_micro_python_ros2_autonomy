# dodaj empra_EV3_client do workspace

# dodaj empra_EV3_server do kolejnego workspace

# uruchom ROS2_API_bridge.py (na linux ubuntu 22.04 z ROS2 humble)
```bash
cd ev3_micro_python_ros2_autonomy
source install/setup.bash
ros2 run empra_ros2_ev3_bridge ROS2_API_bridge.py 

```

# uruchom API_EV3_bridge.py za pomoca visual studio code (na windows)

# wgraj empra_EV3_client/main.py za pomoca `f5` w visual studio code na ev3 w robocie (na windows)

# wgraj empra_EV3_server/main.py za pomoca `f5` w visual studio code na ev3 podłączone do laptopa kablowo (na windows)

# testuj na klawiaturze (na linux ubuntu 22.04 z ROS2 humble)
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_nav

```

# łączność
vmware linux <-wifi interface-> windows pc <-kablowo-> ev3 (server) <-bluetooth-> ev3 (client - robot)