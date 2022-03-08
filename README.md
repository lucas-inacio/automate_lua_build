# Automate Lua build
Use CMake to simplify Lua (library and interpreter) build. Lua compiler not included.

## Dependencies
Python 3
CMake

## Usage
First download latest lua release. There is a python script included. In the project's root directory run:
```shell
python get_lastest_lua_release.py
```
## Building
```shell
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX='<your choice>' -DCMAKE_BUILD_TYPE=Release
cmake --build .
cmake --install .
```

## Notes
This project was created to simplify Lua building and installation on a Windows environment. If you're using Linux you should have no problems using the default Makefile provided.