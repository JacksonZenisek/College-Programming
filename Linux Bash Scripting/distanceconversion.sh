#!/bin/bash
#This is a simple sheel program that converts a one unit of distance to another.

# Prompts the user with a distance conversion menu:
echo "DISTANCE CONVERSION"
echo " "
echo "Enter an option:"
echo "1) feet to inches"
echo "2) yards to feet"
echo "3) inches to centimeters"
echo "4) feet to miles"
echo "5) meters to miles"
echo "6) kilometers to miles"
# The program reads the input option:
read menuselectionmenuselection

# The program's condition if/elif switch:
# feet to inches condition:
if ((menuselectionmenuselection==1)); then
echo " "
echo "Enter feet:"
read feet
inches=$(echo "scale=2; $feet*12" | bc)
echo " "
echo "$feet feet is $inches inches"

# yards to feet condition:
elif ((menuselectionmenuselection==2)); then
echo " "
echo "Enter yards:"
read yards
feet=$(echo "scale=2; $yards*3" | bc)
echo " "
echo "$yards yards is $feet feet"

# inches to centimeters condition:
elif ((menuselectionmenuselection==3)); then
echo " "
echo "Enter inches:"
read inches
centi=$(echo "scale=2; $inches*2.54" | bc)
echo " "
echo "$inches inches is $centi centimeters"

# feet to miles condition
elif ((menuselectionmenuselection==4)); then
echo " "
echo "Enter feet:"
read feet
mi=$(echo "scale=2; $feet/5280" | bc)
echo " "
echo "$feet feet is $mi miles"

# meters to miles condition:
elif ((menuselectionmenuselection==5)); then
echo " "
echo "Enter meters:"
read meters
mi=$(echo "scale=2; $meters/1609" | bc)
echo " "
echo "$meters meters is $mi miles"

# kilometers to miles condition:
elif ((menuselectionmenuselection==6)); then
echo " "
echo "Enter kilometers:"
read kilom
mi=$(echo "scale=2; $kilom/1.609" | bc)
echo " "
echo "$kilom kilometers is $mi miles"

fi
