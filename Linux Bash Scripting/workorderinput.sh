#!/bin/bash
# A basic program that reads the last name, project name, work order number, and the product ID inputs from the user and returns the values to the output.

printdate=$(date)

echo "Enter your last name:"
read lastname
echo " "

echo "Enter the project name:"
read project
echo " "

echo "Enter the work order number:"
read wo
echo " "

echo "Enter the product ID:"
read productid
echo " "

echo "Input captured as:
sleep 2
echo "Last Name: $lastname"
sleep 2
echo "Project: $project"
sleep 2
echo "Work Order Number: $wo"
sleep 2
echo "Product ID: $productid"
sleep 3
echo "Input captured!"
