#!/bin/bash
# A simple utility tool.
# Programmed by Jackson Zenisek

# Main menu section
mainmenu() {
echo " "
echo "--------------------"
echo "GENERAL UTILITY TOOL"
echo "Programmed by Jackson Zenisek"
echo "--------------------"
echo " "
echo "What would you like to do?"
echo "1) Get Device Information"
echo "2) Get Website Information"
echo "3) Troubleshoot A Problem"
echo "4) Flush DNS Cache"
echo "0) Quit"

read mainmenuoption

if ((mainmenuoption==1)); then
echo " "
echo "GET DEVICE INFORMATION"
echo " "
echo "What would you like to do?"
echo "1) View Drive Storage"
echo "2) Get IPv4 Address"
echo "3) View CPU Architecture"
echo "4) View Installed Linux Distrobution"
echo "5) View Device Name"
echo "6) View Device CPU Specifications"
echo "7) View Device MAC Address"

read getdevopt

elif ((mainmenuoption==2)); then
echo " "
echo "GET WEBSITE INFORMATION"
echo " "
echo "What would you like to do?"
echo "1) View status of a website"
echo "2) Test connection of a website"
echo "3) Get Source Code of a Website"

read getwebopt

elif ((mainmenuoption==3)); then
echo " "
echo "TROUBLESHOOT A PROBLEM"
echo " "
echo "What would you like to do?"
echo "1) Test connection to router"
echo "2) Install Antivirus/Run Scan"
echo "3) Test Loopback Connection"
echo "4) Flush DNS Cache"
echo "5) Change DNS Server"
echo "6) Change Device Password"

read gettroubleshootopt

elif ((mainmenuoption==4)); then
echo " "
echo "Preparing to update system files..."
sleep 3
sudo apt update && sudo apt upgrade -y

elif ((mainmenuoption==0)); then

exit


fi
}



# Get Device Information menu section

getdevmenusel() {

if ((getdevopt==1)); then

echo " "
echo "VIEW DRIVE STORAGE"
echo " "
echo "What would you like to do?"
echo "1) View storage on all drives"
echo "2) View storage on C drive only"

read storagesel

elif ((getdevopt==2)); then
echo "Getting device IPv4..."
sleep 2
getipv4=$(hostname -I)
echo "The IPv4 address of this device is: $getipv4"

elif ((getdevopt==3)); then
echo "Analyzing..."
sleep 2
getcpuarch=$(uname -m)
echo " "
echo "This devices CPU architecture is: $getcpuarch"

elif ((getdevopt==4)); then
viewdistro=$(cat /etc/os-release)
echo " "
echo "Installed linux distrobution on this device:"
echo " "
echo "$viewdistro"

elif ((getdevopt==5)); then
viewdevname=$(whoami)
echo " "
echo "The name of this device is: $viewdevname"

elif ((getdevopt==6)); then
viewcpuinfo=$(lscpu)
echo " "
echo "Analyzing Device CPU..."
sleep 3
echo " "
echo "$viewcpuinfo"

elif ((getdevopt==7)); then
showmac=$(ip link)
echo " "
echo "$showmac"


fi



# Storage Options section
if ((storagesel==1)); then
echo "Analyzing all drives..."
sleep 3
readalldrives=$(df -h)
echo " "
echo "$readalldrives"


elif ((storagesel==2)); then
echo "Analyzing C drive..."
sleep 3
readconly=$(df -h | grep "/mnt/c")
echo " "
echo "$readconly"

fi
}


# Get Website Information menu section

getwebmenusel() {

if ((getwebopt==1)); then
echo " "
echo "Enter the website you want the status of"
read website
websitestatus=$(curl -Is $website)

echo "Here is the status of the website: $website"
echo " "
echo "$websitestatus"

elif ((getwebopt==2)); then
echo " "
echo "Enter the website you would like to ping:"
read websitetoping
echo "Testing connection to $websitetoping..."
websitepingtest=$(ping -c 4 $websitetoping)
echo " "
echo " "
echo "$websitepingtest"

elif ((getwebopt==3)); then
echo " "
echo "Enter the website you would like to download the source code from:"
read websitesrccodelink
dwnldsrccode=$(wget $websitesrccodelink)
echo "$dwnldsrccode"


fi
}

gettoublessel() {

if ((gettroubleshootopt==1)); then
echo " "
echo "Searching router IP..."
echo " "
sleep 2
searchrouterip=$(ip route | grep default)
echo "$searchrouterip"
sleep 1
routerip=$(echo "$searchrouterip" | cut -d' ' -f3)
echo " "
pingrouter=$(ping -c 4 $routerip)
echo "$pingrouter"


elif ((gettroubleshootopt==2)); then
echo " "
echo "Checking system for ClamAV version..."
sleep 2
clamver=$(clamscan --version)
echo "$clamver"
echo " "
installav=$(sudo apt install clamav)
echo "$installav"
downloadlastestav=$(sudo freshclam)
echo "downloadlastestav"
echo " "
echo "Please wait, scanning system..."
scanandsaverepo=$(sudo clamscan ~/*)
echo "$scanandsaverepo"


elif ((gettroubleshootopt==3)); then
echo " "
echo "Testing loopback connection to 127.0.0.1..."
echo " "
sleep 2
pinglb=$(ping -c 4 127.0.0.1)
echo "$pinglb"

elif ((gettroubleshootopt==4)); then
echo " "
flushdns=$(sudo resolvectl flush-caches)
echo "DNS cache successfully flushed!"


elif ((gettroubleshootopt==5)); then
echo " "

echo "PLEASE READ!!!!"
echo "---------------"
echo "Use caution when editing this file."
echo "Look for something like 'nameserver x.x.x.x' and replace it with something like this 'nameserver 8.8.8.8','nameserver 192.168.1.1', or 'nameserver 9.9.9.9'."
sleep 5
echo "Please wait..."
sleep 15
sudo nano /etc/resolv.conf

elif ((gettroubleshootopt==6)); then
echo " "
chgpass=$(passwd)
echo "$chgpass"


fi
}


# Call functions
mainmenu
getdevmenusel
getwebmenusel
gettoublessel
