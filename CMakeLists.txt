cmake_minimum_required(VERSION 3.20)

project(automate_lua_build)

# Figure out latest lua source release
file(DOWNLOAD https://api.github.com/repos/lua/lua/releases/latest lua_release.json)
file(READ ${CMAKE_BINARY_DIR}/lua_release.json LUA_RELEASE_STRING)
string(JSON LUA_SOURCE_URL GET ${LUA_RELEASE_STRING} tarball_url)
message("Downloading latest lua release from " ${LUA_SOURCE_URL})

# Download and extract lua source
file(DOWNLOAD ${LUA_SOURCE_URL} lua_release.tar.gz)
file(ARCHIVE_EXTRACT INPUT lua_release.tar.gz DESTINATION lua_src)
file(GLOB LUA_SUB_DIR ${CMAKE_BINARY_DIR}/lua_src/*)
set(LUA_DIR ${LUA_SUB_DIR})

# Build lua C API library
add_library(lua STATIC
    ${LUA_DIR}/lapi.c ${LUA_DIR}/lcode.c ${LUA_DIR}/lctype.c ${LUA_DIR}/ldebug.c ${LUA_DIR}/ldo.c
    ${LUA_DIR}/ldump.c ${LUA_DIR}/lfunc.c ${LUA_DIR}/lgc.c ${LUA_DIR}/llex.c ${LUA_DIR}/lmem.c
    ${LUA_DIR}/lobject.c ${LUA_DIR}/lopcodes.c ${LUA_DIR}/lparser.c ${LUA_DIR}/lstate.c
    ${LUA_DIR}/lstring.c ${LUA_DIR}/ltable.c ${LUA_DIR}/ltm.c ${LUA_DIR}/lundump.c
    ${LUA_DIR}/lvm.c ${LUA_DIR}/lzio.c ${LUA_DIR}/lauxlib.c ${LUA_DIR}/lbaselib.c
    ${LUA_DIR}/lcorolib.c ${LUA_DIR}/ldblib.c ${LUA_DIR}/liolib.c ${LUA_DIR}/lmathlib.c
    ${LUA_DIR}/loadlib.c ${LUA_DIR}/loslib.c ${LUA_DIR}/lstrlib.c ${LUA_DIR}/ltablib.c
    ${LUA_DIR}/lutf8lib.c ${LUA_DIR}/linit.c)

target_include_directories(lua PUBLIC ${LUA_DIR})

# Build lua interpreter
add_executable(lua-bin ${LUA_DIR}/lua.c)
target_link_libraries(lua-bin lua)
set_target_properties(lua-bin PROPERTIES OUTPUT_NAME lua)

install(TARGETS lua DESTINATION lib)
install(TARGETS lua-bin DESTINATION bin)
install(
    FILES ${LUA_DIR}/lua.h ${LUA_DIR}/luaconf.h ${LUA_DIR}/lualib.h ${LUA_DIR}/lauxlib.h
    DESTINATION include)