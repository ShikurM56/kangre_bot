# kangre_bot
Kangre Bot is a low cost robot based in navigation.

## Clone your repo into your catkin workspace
```
cd ~/catkin_ws/src
git clone https://github.com/ShikurM56/lx-16a_ros.git
cd ~/catkin_ws/
catkin_make
```

## Install all the dependences
```
sudo apt-get install ros-melodic-gmapping
sudo apt-get install ros-melodic-map-server
sudo apt-get install ros-melodic-cartographer-ros
sudo apt-get install ros-melodic-map-server
sudo apt-get install ros-melodic-move-base
sudo apt-get install ros-melodic-dwa-local-planner
```

## For mapping:
```
roslaunch kangre_firmware bringup.launch
roslaunch kangre_firmware server_bringup.launch
roslaunch kangre_slam kangre_slam.launch
roslaunch kangre_visualization display.launch
```

### Run the gmapping node:
```
rosrun gmapping slam_gmapping scan:=scan
```

### Save the map:
```
rosrun map_server map_saver -f ~/catkin_ws/src/kangre_navigation/maps/map_name
```

## For navigation:
```
roslaunch kangre_autonomo_description gazebo.launch
roslaunch kangre_cartographer server_bringup.launch
roslaunch kangre_navigation kangre_sim_navigation.launch
```
