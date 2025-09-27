# dodaj empra_EV3_client do workspace

# uruchom ROS2_API_bridge.py
```bash
cd ev3_micro_python_ros2_autonomy
source install/setup.bash
ros2 run empra_ros2_ev3_bridge ROS2_API_bridge.py 

```

# uruchom API_EV3_bridge.py za pomoca visual studio code


# main.py uruchom za pomoca `f5` w visual studio code

# testuj na klawiaturze
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_nav

```
