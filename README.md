# Automate Lua build
Use CMake to simplify Lua (library and interpreter) build. Lua compiler not included.

## Dependencies
- ~~Python 3~~ No need for python since the release is obtained by cmake itself
- CMake

## Usage
~~First download latest lua release. There is a python script included. In the project's root directory run:~~ No need for python anymore.
## Building
```shell
mkdir build
cd build
cmake .. -G "NMake Makefiles" -DCMAKE_INSTALL_PREFIX='<your choice>' -DCMAKE_BUILD_TYPE=Release
cmake --build .
cmake --install .
```

## Notes
This project was created to simplify Lua building and installation on a Windows environment. If you're using Linux you should have no problems using the default Makefile provided.
