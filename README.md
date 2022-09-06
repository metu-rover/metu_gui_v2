# metu_gui_v2

This repo is created as a metu_gui_v2 package.
Download this repo in to your workspace/src <br />

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
- [ ] Correct usage of Mixins will be searched.
- [ ] Create a virtual environment and create requirements.txt accordingly.
- [ ] Create a sample graph changing with ros.
- [ ] Give graphs proper names.
- [ ] Grey color theme is set.
- [ ] Comment on the codes.
- [x] Bare minimum ros2 integration is set and tested.
- [ ] Make this TODO operations on a .txt file.
- [x] Push github only the package, not the whole workspace.
- [x] Skeletons of Main, Camera, Science Mixins are created.
- [x] RoverGui super class is created.
- [x] GUI is designed from Berk Abim's pdf file.
