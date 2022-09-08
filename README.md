# metu_gui_v2

This repo is created as a metu_gui_v2 package.
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
- [ ] Launch file will be written.
- [ ] Update inplace in matplotlib graphs will be implemented.
- [ ] Callback_groups will be searched.
- [ ] Try publishing the PC camera view and subscribe it.
- [ ] Correct usage of Mixins will be searched.
- [ ] Create a virtual environment and create requirements.txt accordingly.
- [ ] Give graphs proper names.
- [ ] Grey color theme is set.
- [ ] Comment on the codes.
- [x] Spinning multiple ros nodes with executors.
- [x] Create a sample graph changing with ros.
- [x] Make this TODO operations on a .txt file.


## Which file do what
* camera_input : To be implemented.
* general_input : ros node for subscribing general input.
* initiator : Class for initiating ros nodes, default ui configurations, QThreads.
* ros_reciever_thread : QThread that initialize and spins the ros nodes.
* ros_test_message : Sends a test data from a ros node.
* rover_gui : Class that unifies all the operations (ui, ros ...).
* science_input : ros node for subscribing science input.
* ui : UI file generated from QT designer.
