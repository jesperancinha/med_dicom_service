# Medical Dicom Service

---

[![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=Med%20Dicom%20Service🏥&color=informational)](https://github.com/jesperancinha/med_dicom_service)
[![GitHub License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg?style=flat)](https://www.apache.org/licenses/LICENSE-2.0)

[![CircleCI](https://circleci.com/gh/jesperancinha/med_dicom_service.svg?style=svg)](https://circleci.com/gh/jesperancinha/med_dicom_service)
[![med_dicom_service](https://github.com/jesperancinha/med_dicom_service/actions/workflows/python-package.yml/badge.svg)](https://github.com/jesperancinha/med_dicom_service/actions/workflows/python-package.yml)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e0840fb465c6425785df419fb3887b2b)](https://www.codacy.com/gh/jesperancinha/med_dicom_service/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jesperancinha/med_dicom_service&amp;utm_campaign=Badge_Grade)
[![codebeat badge](https://codebeat.co/badges/f71948d7-db29-4b36-a309-e347f96699f0)](https://codebeat.co/projects/github-com-jesperancinha-med_dicom_service-master)
[![BCH compliance](https://bettercodehub.com/edge/badge/jesperancinha/med_dicom_service?branch=master)](https://bettercodehub.com/results/jesperancinha/med_dicom_service)

[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/e0840fb465c6425785df419fb3887b2b)](https://www.codacy.com/gh/jesperancinha/med_dicom_service/dashboard?utm_source=github.com&utm_medium=referral&utm_content=jesperancinha/med_dicom_service&utm_campaign=Badge_Coverage)
[![Coverage Status](https://coveralls.io/repos/github/jesperancinha/med_dicom_service/badge.svg?branch=master)](https://coveralls.io/github/jesperancinha/med_dicom_service?branch=master)
[![codecov](https://codecov.io/gh/jesperancinha/med_dicom_service/branch/master/graph/badge.svg?token=nuvzffSwkW)](https://codecov.io/gh/jesperancinha/med_dicom_service)

[![GitHub language count](https://img.shields.io/github/languages/count/jesperancinha/med_dicom_service.svg)](#)
[![GitHub top language](https://img.shields.io/github/languages/top/jesperancinha/med_dicom_service.svg)](#)
[![GitHub top language](https://img.shields.io/github/languages/code-size/jesperancinha/med_dicom_service.svg)](#)

---

## Technologies used

Please check the [TechStack.md](TechStack.md) file for details.

## Introduction

A simple service to load, store and display dicom tags for different files

This software is used to read and display tags from dicom file transfers

## Software

* You need to have a specific python setup:

```shell
pip3 install flask

pip3 install virtualenv

cd dicom_rest_service

virtualenv flask

flask/bin/pip install flask

pip3 install configparser

pip3 install pydicom

pip3 install pynetdicom

pip3 install coveralls

pip3 install pytest

pip3 install coverage
```

## Run Coverage

```shell
coverage run --source=dicom_rest_service -m pytest

coverage report -m

coverage html
coverage json
coverage xml
```

## Requirements file

```bash
pip freeze > requirements.txt
```

## Cleaning REGEX

```text
 @ file:///opt.*
 \@ file\:\/\/\/.*
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

## Starting simulation

You can start simulating your environment in this way:

```
$ storescp -v 1234 -od temp

$ storescu --propose-rle 127.0.0.1 1234 ~/Downloads/sample.dcm
```

> NOTE: for the example, please copy the resulting file to /tmp/dicom

## References

-   [Coverage PY](https://coverage.readthedocs.io/en/6.2/)

-   [mod_dcmnet](https://support.dcmtk.org/docs-dcmrt/mod_dcmnet.html)

-   [classDcmSCU](https://support.dcmtk.org/docs-dcmrt/classDcmSCU.html)

-   [storescp](https://support.dcmtk.org/docs-dcmrt/storescp.html)

## About me

[![GitHub followers](https://img.shields.io/github/followers/jesperancinha.svg?label=Jesperancinha&style=for-the-badge&logo=github&color=grey "GitHub")](https://github.com/jesperancinha)
