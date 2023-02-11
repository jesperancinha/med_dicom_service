# Medical Dicom Service

---
[![Twitter URL](https://img.shields.io/twitter/url?logoColor=blue&style=social&url=https%3A%2F%2Fimg.shields.io%2Ftwitter%2Furl%3Fstyle%3Dsocial)](https://twitter.com/intent/tweet?text=%20Checkout%20this%20%40github%20repo%20by%20%40joaofse%20%F0%9F%91%A8%F0%9F%8F%BD%E2%80%8D%F0%9F%92%BB%3A%20https%3A//github.com/jesperancinha/med_dicom_service)
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

---
[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-50/python-50.png "Python")](https://www.python.org/)
[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-50/flask-50.png "Flask Service")](https://flask.palletsprojects.com/)
[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-50/pydicom-50.png "Pydicom")](https://flask.palletsprojects.com/)
---

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

[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-20/JEOrgLogo-20.png "João Esperancinha Homepage")](http://joaofilipesabinoesperancinha.nl)
[![GitHub followers](https://img.shields.io/github/followers/jesperancinha.svg?label=Jesperancinha&style=social "GitHub")](https://github.com/jesperancinha)
[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-20/mastodon-20.png "Mastodon")](https://masto.ai/@jesperancinha)
[![Twitter Follow](https://img.shields.io/twitter/follow/joaofse?label=João%20Esperancinha&style=social "Twitter")](https://twitter.com/joaofse)
| [Sessionize](https://sessionize.com/joao-esperancinha/)
| [Spotify](https://open.spotify.com/user/jlnozkcomrxgsaip7yvffpqqm?si=b54b89eae8894960)
| [Medium](https://medium.com/@jofisaes)
| [YouTube](https://www.youtube.com/@joaoesperancinha/featured)
| [Instagram](https://www.instagram.com/joaofisaes/)
| [Buy me a coffee](https://www.buymeacoffee.com/jesperancinha)
| [Credly Badges](https://www.credly.com/users/joao-esperancinha)
| [Google Apps](https://play.google.com/store/apps/developer?id=Joao+Filipe+Sabino+Esperancinha)
| [Sonatype Search Repos](https://search.maven.org/search?q=org.jesperancinha)
| [Docker Images](https://hub.docker.com/u/jesperancinha)
| [Stack Overflow Profile](https://stackoverflow.com/users/3702839/joao-esperancinha)
| [Reddit](https://www.reddit.com/user/jesperancinha/)
| [Dev.TO](https://dev.to/jofisaes)
| [Hackernoon](https://hackernoon.com/@jesperancinha)
| [Code Project](https://www.codeproject.com/Members/jesperancinha)
| [BitBucket](https://bitbucket.org/jesperancinha)
| [GitLab](https://gitlab.com/jesperancinha)
| [Coursera](https://www.coursera.org/user/da3ff90299fa9297e283ee8e65364ffb)
| [FreeCodeCamp](https://www.freecodecamp.org/jofisaes)
| [HackerRank](https://www.hackerrank.com/jofisaes)
| [LeetCode](https://leetcode.com/jofisaes)
| [Codebyte](https://coderbyte.com/profile/jesperancinha)
| [CodeWars](https://www.codewars.com/users/jesperancinha)
| [Code Pen](https://codepen.io/jesperancinha)
| [Hacker Earth](https://www.hackerearth.com/@jofisaes)
| [Khan Academy](https://www.khanacademy.org/profile/jofisaes)
| [Hacker News](https://news.ycombinator.com/user?id=jesperancinha)
| [InfoQ](https://www.infoq.com/profile/Joao-Esperancinha.2/)
| [LinkedIn](https://www.linkedin.com/in/joaoesperancinha/)
| [Xing](https://www.xing.com/profile/Joao_Esperancinha/cv)
| [Tumblr](https://jofisaes.tumblr.com/)
| [Pinterest](https://nl.pinterest.com/jesperancinha/)
| [Quora](https://nl.quora.com/profile/Jo%C3%A3o-Esperancinha)
| [VMware Spring Professional 2021](https://www.credly.com/badges/762fa7a4-9cf4-417d-bd29-7e072d74cdb7)
| [Oracle Certified Professional, Java SE 11 Programmer](https://www.credly.com/badges/87609d8e-27c5-45c9-9e42-60a5e9283280)
| [Oracle Certified Professional, JEE7 Developer](https://www.credly.com/badges/27a14e06-f591-4105-91ca-8c3215ef39a2)
| [IBM Cybersecurity Analyst Professional](https://www.credly.com/badges/ad1f4abe-3dfa-4a8c-b3c7-bae4669ad8ce)
| [Certified Advanced JavaScript Developer](https://cancanit.com/certified/1462/)
| [Certified Neo4j Professional](https://graphacademy.neo4j.com/certificates/c279afd7c3988bd727f8b3acb44b87f7504f940aac952495ff827dbfcac024fb.pdf)
| [Deep Learning](https://www.credly.com/badges/8d27e38c-869d-4815-8df3-13762c642d64)
| [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=JEsperancinhaOrg&color=yellow "jesperancinha.org dependencies")](https://github.com/JEsperancinhaOrg)
[![Generic badge](https://img.shields.io/static/v1.svg?label=All%20Badges&message=Badges&color=red "All badges")](https://joaofilipesabinoesperancinha.nl/badges)
[![Generic badge](https://img.shields.io/static/v1.svg?label=Status&message=Project%20Status&color=red "Project statuses")](https://github.com/jesperancinha/project-signer/blob/master/project-signer-quality/Build.md)
