#!/bin/bash
# A hopefully helpful utility tool for xmrig miners.
# Developed by Jackson Zenisek

mainmenu() {
echo "-------------------"
echo "XMRIG UTILITY TOOL"
echo "-------------------"
echo " "
echo "Choose an option:"
echo "1) Install XMRig"
echo "2) Run XMRig"
read mainmenselopt




# Install XMRig option:

if ((mainmenselopt==1)); then

echo "Preparing to update system files..."
sleep 2
sudo apt update && sudo apt upgrade -y
sleep 3
echo " "
showcurrentdir=$(pwd)
echo "Choose an option:"
echo "1) Install XMRig in current direrctory: $showcurrentdir"
echo "2) Install XMRig in a different directory"
read installxmrigchoice

fi




if ((installxmrigchoice==1)); then
sleep 3
printdir=$(pwd)
echo "Are you sure you want to install XMRig in printdir ? y = 1/n = 2"
read doublechecker

fi

if ((doublechecker==1)); then
echo "Preparing to install dependencies..."
sleep 3
sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
echo "Cloning the software package..."
sleep 2
git clone https://github.com/xmrig/xmrig.git
echo "Entering subdirectories..."
sleep 2
cd xmrig
mkdir build
cd build
cmake ..
echo "Preparing to install XMRig..."
sleep 5
make
echo " "
echo "Installation complete!"

fi


if ((installxmrigchoice==2)); then
echo " "
echo "Enter the directory that you want to install XMRig in:"
read entereddir
echo "Are you sure you want to install XMRig in $entereddir ? y = 1/n = 2"
read doublecheckertwooption

fi


if ((doublecheckertwooption==1)); then
echo "Entering $entereddir ..."
sleep 2
cd $entereddir
echo "Preparing to install dependencies..."
sleep 3
sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
echo "Cloning the software package..."
sleep 2
git clone https://github.com/xmrig/xmrig.git
echo "Entering subdirectories..."
sleep 2
cd xmrig
mkdir build
cd build
cmake ..
echo "Preparing to install XMRig..."
sleep 5
make
echo " "
echo "Installation complete!"


fi


# Run XMRig option

if ((mainmenselopt==2)); then
getcurrentdir=$(pwd)
echo " "
echo "Where did you install XMRig?:"
echo "1) This directory: $getcurrentdir"
echo "2) A different directory"
read wherexmriginstalled

fi

if ((wherexmriginstalled==1)); then
echo " "
echo "Enter your wallet key:"
read walKy
echo "Enter what port you want to join?:"
echo "Here are some options, or you can enter your own:"
echo "-------------------------------------------------"
echo "10128"
echo "10064"
echo "10256"
echo "10512"
echo "11024"
echo "12048"
echo "14096"
echo "18192"
echo " "
read portenter
echo " "
echo "What would you like to name your miner?"
read minername
echo " "
echo "Would you like to run XMRig under admin previlages? Running it under admin may increase mining speed. y = 1/n = 2:"
read adminprev


elif ((wherexmriginstalled==2)); then
echo " "
echo "Enter the directory XMRig is installed in:"
read entereddirectoryyy
cd $entereddirectoryyy
echo "Entering $entereddirectoryyy ..."
sleep 2
echo " "
echo "Enter your wallet key:"
read walKy
echo "Enter what port you want to join?:"
echo "Here are some options, or you can enter your own"
echo "-------------------------------------------------"
echo "10128"
echo "10064"
echo "10256"
echo "10512"
echo "11024"
echo "12048"
echo "14096"
echo "18192"
echo " "
read portenter
echo " "
echo "What would you like to name your miner?"
read minername
echo" "
echo "Would you like to run XMRig under admin previlages? Running it under admin may increase mining speed. y = 1/n = 2:"
read adminprev

fi


if ((adminprev==1)); then
echo " "
echo "Starting XMRig under admin..."
sleep 5
cd xmrig
cd build
sudo ./xmrig -o gulf.moneroocean.stream:$portenter -u $walKy -p $minername

elif ((adminprev==2)); then
echo " "
echo "Starting XMRig with regular previlages..."
sleep 5
cd xmrig
cd build
./xmrig -o gulf.moneroocean.stream:$portenter -u $walKy -p $minername

fi
}

# Call Functions List
mainmenu
