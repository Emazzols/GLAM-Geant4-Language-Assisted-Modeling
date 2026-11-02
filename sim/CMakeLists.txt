cmake_minimum_required(VERSION 3.16)
project(SimpleSim)

find_package(Geant4 REQUIRED ui_all vis_all)
find_package(ROOT REQUIRED)

include(${Geant4_USE_FILE})

include_directories(
    ${PROJECT_SOURCE_DIR}/include
    ${ROOT_INCLUDE_DIRS}
)

add_executable(SimpleSim
    main.cc
    src/DetectorConstruction.cc
    src/PrimaryGeneratorAction.cc
    src/ActionInitialization.cc
    src/RunAction.cc
    src/EventAction.cc
    src/SteppingAction.cc
    vis.mac
    run.mac
)

target_link_libraries(SimpleSim
    ${Geant4_LIBRARIES}
    ROOT::Core
    ROOT::RIO
    ROOT::Tree
)

