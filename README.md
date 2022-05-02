# kangre_bot
Kangre Bot is a low cost robot based in navigation.

1.- Clone your repo into your catkin workspace
```
cd ~/catkin_ws/src
git clone https://github.com/ShikurM56/lx-16a_ros.git
cd ~/catkin_ws/
catkin_make
```

## For navigation:
```
roslaunch kangre_autonomo_description gazebo.launch
roslaunch kangre_cartographer server_bringup.launch
roslaunch kangre_navigation kangre_sim_navigation.launch
```
