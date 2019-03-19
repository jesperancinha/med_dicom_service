# med_dicom_service
A simple service to load, store and display dicom tags for different files
## Introduction

This software is used to read and display tags from dicom file transfers
## Software

* You need to have a specific python setup:
```
$ pip3 install flask

$ pip3 install virtualenv

$ cd dicom_rest_service

$ virtualenv flask

$ flask/bin/pip install flask

$ pip3 install configparser

$ pip3 install pydicom

$ pip3 install pynetdicom

```

* You also need to install the dcmtk package


> MacOS	 brew-Link Homebrew	

```
$ brew install dcmtk
```
>  Windows	choco-Link Chocolatey
```
$ choco install dcmtk
```
> MacOS	Fink	
```
$ fink install dcmtk
```
> MacOS	MacPorts
```
$ port install dcmtk
```
> Linux	 debian-Link Debian	
```
$ sudo apt install dcmtk

```