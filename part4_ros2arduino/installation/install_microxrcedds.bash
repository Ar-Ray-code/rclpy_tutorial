#!/bin/bash
cd ~/
git clone https://github.com/eProsima/Micro-XRCE-DDS.git
mv Micro-XRCE-DDS/ .Micro-XRCE-DDS/
cd .Micro-XRCE-DDS/
git checkout v1.1.0
mkdir build && cd build && cmake ..
# make
echo "alias MicroXRCEAgent='~/.Micro-XRCE-DDS/build/MicroXRCEAgent'" >> ~/.bashrc