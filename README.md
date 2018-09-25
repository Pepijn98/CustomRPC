[![Codacy Badge](https://api.codacy.com/project/badge/Grade/676abe43246644b0a4e9b02b18c5ceea)](https://www.codacy.com/app/KurozeroPB/CustomRPC?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=KurozeroPB/CustomRPC&amp;utm_campaign=Badge_Grade)

# CustomRPC
This is a simple app to set a custom rich presence in discord<br>
As far as I know it only works for Linux and Windows I do not own a mac to build and test the app<br/>


**Download from [here](https://github.com/KurozeroPB/CustomRPC/releases/download/v0.1.1/)**

**wiki is outdated**\
See the [wiki](https://github.com/KurozeroPB/CustomRPC/wiki/Creating-and-using-a-Discord-app) on how to use CustomRPC with your own app for more customization.<br/>
Check out [projects](https://github.com/KurozeroPB/CustomRPC/projects/1) to see what is planned for the future.<br/>
## Previews
Linux                                 |Windows
:------------------------------------:|:------------------------------------:
![linux](./assets/linux-preview.png)  |  ![windows](./assets/windows-preview.png)
**Result**                            |
![result](./assets/result-preview.png)|

## Building the app yourself
#### Requirements:
- [git](https://git-scm.com/downloads)
- [python 3.5+](https://www.python.org/downloads/release/python-354/) (I use 3.6)
- Qt5
  - Linux: `sudo apt-get install qtcreator build-essential qt5-default`
  - Windows/Mac: I'm sorry idk but google is your best friend
- PyQt5
  - Linux: `sudo apt-get install python3-pyqt5 pyqt5-dev-tools qttools5-dev-tools`
  - Windows/Mac: I'm sorry idk but google is your best friend
- [pyinstaller](https://www.pyinstaller.org/)

1. `git clone https://github.com/KurozeroPB/CustomRPC.git && cd CustomRPC`
2. `pyinstaller --onefile --windowed --name customrpc_0.1.1 main.py`

This will create an executable file in the `dist` folder
## Tested Operating Systems
- Linux Ubuntu 16.04 ✓
- Linux Ubuntu 17.xx ✓
- Linux Ubuntu 18.04 ✓
- Windows 7 ✓
- Windows 8/8.1 ✓
- Windows 10 ✓

*This is just what I tested if there are more that you know please make an issue*
