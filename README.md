<h1>CustomRPC</h1>
This is a simple app to set a custom rich presence in discord<br>
<br>
The linux executable can be found <a href="https://github.com/KurozeroPB/CustomRPC/releases/download/v0.0.1/customrpc_0.0.1">here</a><br>
The dep file can be found <a href="https://github.com/KurozeroPB/CustomRPC/releases/download/v0.0.1/customrpc_0.0.1.deb">here</a><br>
The windows build can be found <a href="https://github.com/KurozeroPB/CustomRPC/releases/download/v0.0.1/customrpc-windows-x64.tar.gz">here</a><br/>
<br/>
Honestly I don't even know if the windows build runs without python and qt4<br/>
So if it doesn't see the build instructions below and install both.<br/>
<br/>
Linux preview:
<img src="./assets/linux-preview.png"></img><br/>
Windows preview:
<img src="./assests/windows-preview.png"></img><br/>
<br/>
Currently only providing linux and windows builds.<br/>
All the components are here for you to build it for whatever system you like.<br>
All you need is <a href="https://www.python.org/downloads/release/python-354/">python 3.5</a>, <a href="https://www.qt.io/download">Qt4</a>, <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4">PyQt4</a> and <a href="https://www.pyinstaller.org/">pyinstaller</a><br>
To pack everything into 1 executable the command would look like:<br>
<code>pyinstaller --onefile --windowed --name customrpc_0.0.1 main.py</code><br>
You can change the name to whatever you like.
