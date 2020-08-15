# GarudaHacks

![logo](https://drive.google.com/uc?export=view&id=1EA6FxWtRfL7fcRuau4w8we7ZvGr4wnhc)



**Table of Contents**

- [IQSquare](#ikhwat)
  - [Inspiration](#inspiration)
  - [What it Does](#what-it-does)
  - [Executing app](#executing-app)
  - [Current Features](#current-features)
  - [Architecture](#architecture)
  - [What is next for Ikhwat](#what-is-next-for-ikhwat)





## Inspiration
With a myriad of health devices, every remote smart health device needs a back end that supports data streaming, storage, visualization and analysis. IQSquare data platform is one-stop shop for different health device manufacturers who can come and configure their devices to stream data into our platform and obtain inferences from the data 

## What it Does

The platform allows device manufacturers to set up recipes or rules that are specific to the devices that they have built. They can also upload their own machine learning models that will feed on the streaming data from devices and predict the susceptibility of the wearer of the device to various health risks.

## Executing app

In order to set the rule, please visit
http://3.131.35.56:5001/

In order to configure your device to send data to out streaming platform, please refer to the file 
https://github.com/ashhadulislam/GarudaHacks/blob/master/test_codes/kinesis_py_code/write_kine_random.py


## Current Features

Devices Supported so far
- Headband
- FitBit
- Smart ECG Machines

Features supported so far
- Registration of Rules/Recipes for suported devices
- Continuos streaming of data 
- Visual represntation of data through dynamic graphs



## Architecture
![](https://drive.google.com/uc?export=view&id=17jAviijJvLBCL-tyEmsEV-GLEmA6cSMz)


## What is next for IQSquare

Some of the features that we are hoping to incorporate include
- Allow ML and DL models to be run
- Dynamic device registration
- Dedicated Front End platform for visualizations


Video Link: 
https://www.youtube.com/watch?v=pe0GE5RNiGM&feature=youtu.be