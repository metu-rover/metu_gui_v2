# metu_gui_v2

This repo is created as a metu_gui_v2 package by Yusuf Onat Yılmaz.
Download this repo in to your workspace/src. Please do not commit to main branch without informing the admin. However, feel free to create new branch anytime you want. <br />

Final folder structure should be like below:
- workspace
  - ...
  - build/
  - src/
    - metu_gui_v2/
      - metu_gui_v2/
      - setup.py
      - package.xml
      - ...
    - ....

In order to start the gui run the following commands in different terminals. Make sure that workspace is builded and sourced correctly.

```bash
ros2 run metu_gui_v2 talker
```

```bash
ros2 run metu_gui_v2 listener
```

Please contact the admin:
* If you still can't open the GUI.
* If you didn't understand the code.
* Things you have tried from stackoverflow are not working.
* In case of emergency.


## TODO
- [ ] Launching executors will be searched.
- [ ] Callback_groups will be searched.
- [ ] Try publishing the PC camera view and subscribe it.
- [ ] Correct usage of Mixins will be searched.
- [ ] Create a virtual environment and create requirements.txt accordingly.
- [ ] Grey color theme is set.
- [x] Launch file will be written.
- [x] Update inplace in matplotlib graphs will be implemented.
- [x] Give graphs proper names.
- [x] Comment on the codes.
- [x] ...

## Which file do what
* camera_input : To be implemented.
* general_input : ros node for subscribing general input.
* initiator : Class for initiating ros nodes, default ui configurations, QThreads.
* ros_reciever_thread : QThread that initialize and spins the ros nodes.
* ros_test_message : Sends a test data from a ros node.
* rover_gui : Class that unifies all the operations (ui, ros ...).
* science_input : ros node for subscribing science input.
* ui : UI file generated from QT designer.

## rqtgraph
!["ros2 run rqtgraph rqtgraph"](/assets/nodes_topics.png)
