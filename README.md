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
sudo apt-get install ros-melodic-cartographer-ros
sudo apt-get install ros-melodic-map-server
sudo apt-get install ros-melodic-move-base
sudo apt-get install ros-melodic-dwa-local-planner
```

## For mapping:

### Kangre_bot:
```
roslaunch kangre_firmware bringup.launch
roslaunch kangre_firmware server_bringup.launch
```

### Laptop:
```
roslaunch kangre_visualization display.launch
```

#### Running the gmapping node:
```
rosrun gmapping slam_gmapping scan:=scan
```

#### Running the cartographer node:
```
roslaunch kangre_slam kangre_slam.launch
```

#### Save the map:
```
rosrun map_server map_saver -f map_name
```

## For navigation:

### Kangre_bot:
```
roslaunch kangre_firmware bringup.launch
roslaunch kangre_firmware server_bringup.launch
roslaunch kangre_navigation kangre_navigation.launch
```

### Laptop:
```
kangre_visualization kangre_navigation.launch
```
