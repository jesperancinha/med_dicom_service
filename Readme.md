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

[![alt text](https://raw.githubusercontent.com/jesperancinha/project-signer/master/project-signer-templates/icons-100/JEOrgLogo-27.png "João Esperancinha Homepage")](http://joaofilipesabinoesperancinha.nl)
[![](https://img.shields.io/badge/youtube-%230077B5.svg?style=for-the-badge&logo=youtube&color=FF0000)](https://www.youtube.com/@joaoesperancinha)
[![](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@jofisaes)
[![](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-%230077B5.svg?style=for-the-badge&logo=buymeacoffee&color=yellow)](https://www.buymeacoffee.com/jesperancinha)
[![](https://img.shields.io/badge/Twitter-%230077B5.svg?style=for-the-badge&logo=twitter&color=white)](https://twitter.com/joaofse)
[![](https://img.shields.io/badge/Mastodon-%230077B5.svg?style=for-the-badge&logo=mastodon&color=afd7f7)](https://masto.ai/@jesperancinha)
[![](https://img.shields.io/badge/Sessionize-%230077B5.svg?style=for-the-badge&logo=sessionize&color=cffff6)](https://sessionize.com/joao-esperancinha)
[![](https://img.shields.io/badge/Instagram-%230077B5.svg?style=for-the-badge&logo=instagram&color=purple)](https://www.instagram.com/joaofisaes)
[![](https://img.shields.io/badge/Tumblr-%230077B5.svg?style=for-the-badge&logo=tumblr&color=192841)](https://jofisaes.tumblr.com)
[![](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)](https://open.spotify.com/user/jlnozkcomrxgsaip7yvffpqqm)
[![](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/joaoesperancinha/)
[![](https://img.shields.io/badge/Xing-%230077B5.svg?style=for-the-badge&logo=xing&color=064e40)](https://www.xing.com/profile/Joao_Esperancinha/cv)
[![](https://img.shields.io/badge/YCombinator-%230077B5.svg?style=for-the-badge&logo=ycombinator&color=d0d9cd)](https://news.ycombinator.com/user?id=jesperancinha)
[![GitHub followers](https://img.shields.io/github/followers/jesperancinha.svg?label=Jesperancinha&style=social "GitHub")](https://github.com/jesperancinha)
[![](https://img.shields.io/badge/bitbucket-%230077B5.svg?style=for-the-badge&logo=bitbucket&color=blue)](https://bitbucket.org/jesperancinha)
[![](https://img.shields.io/badge/gitlab-%230077B5.svg?style=for-the-badge&logo=gitlab&color=orange)](https://gitlab.com/jesperancinha)
[![](https://img.shields.io/badge/Stack%20Overflow-%230077B5.svg?style=for-the-badge&logo=stackoverflow&color=5A5A5A)](https://stackoverflow.com/users/3702839/joao-esperancinha)
[![](https://img.shields.io/badge/Credly-%230077B5.svg?style=for-the-badge&logo=credly&color=4d2a00)](https://www.credly.com/users/joao-esperancinha)
[![](https://img.shields.io/badge/Coursera-%230077B5.svg?style=for-the-badge&logo=coursera&color=000080)](https://www.coursera.org/user/da3ff90299fa9297e283ee8e65364ffb)
[![](https://img.shields.io/badge/Docker-%230077B5.svg?style=for-the-badge&logo=docker&color=cyan)](https://hub.docker.com/u/jesperancinha)
[![](https://img.shields.io/badge/Reddit-%230077B5.svg?style=for-the-badge&logo=reddit&color=black)](https://www.reddit.com/user/jesperancinha/)
[![](https://img.shields.io/badge/Hackernoon-%230077B5.svg?style=for-the-badge&logo=hackernoon&color=0a5d00)](https://hackernoon.com/@jesperancinha)
[![](https://img.shields.io/badge/Code%20Project-%230077B5.svg?style=for-the-badge&logo=codeproject&color=063b00)](https://www.codeproject.com/Members/jesperancinha)
[![](https://img.shields.io/badge/Free%20Code%20Camp-%230077B5.svg?style=for-the-badge&logo=freecodecamp&color=0a5d00)](https://www.freecodecamp.org/jofisaes)
[![](https://img.shields.io/badge/Hackerrank-%230077B5.svg?style=for-the-badge&logo=hackerrank&color=1e2f97)](https://www.hackerrank.com/jofisaes)
[![](https://img.shields.io/badge/LeetCode-%230077B5.svg?style=for-the-badge&logo=leetcode&color=002647)](https://leetcode.com/jofisaes)
[![](https://img.shields.io/badge/Codewars-%230077B5.svg?style=for-the-badge&logo=codewars&color=722F37)](https://www.codewars.com/users/jesperancinha)
[![](https://img.shields.io/badge/CodePen-%230077B5.svg?style=for-the-badge&logo=codepen&color=black)](https://codepen.io/jesperancinha)
[![](https://img.shields.io/badge/HackerEarth-%230077B5.svg?style=for-the-badge&logo=hackerearth&color=00035b)](https://www.hackerearth.com/@jofisaes)
[![](https://img.shields.io/badge/Khan%20Academy-%230077B5.svg?style=for-the-badge&logo=khanacademy&color=00035b)](https://www.khanacademy.org/profile/jofisaes)
[![](https://img.shields.io/badge/Pinterest-%230077B5.svg?style=for-the-badge&logo=pinterest&color=FF0000)](https://nl.pinterest.com/jesperancinha)
[![](https://img.shields.io/badge/Quora-%230077B5.svg?style=for-the-badge&logo=quora&color=FF0000)](https://nl.quora.com/profile/Jo%C3%A3o-Esperancinha)
[![](https://img.shields.io/badge/Google%20Play-%230077B5.svg?style=for-the-badge&logo=googleplay&color=purple)](https://play.google.com/store/apps/developer?id=Joao+Filipe+Sabino+Esperancinha)
| [Sonatype Search Repos](https://search.maven.org/search?q=org.jesperancinha)
| [Dev.TO](https://dev.to/jofisaes)
| [Codebyte](https://coderbyte.com/profile/jesperancinha)
| [InfoQ](https://www.infoq.com/profile/Joao-Esperancinha.2/)
| [VMware Spring Professional 2021](https://www.credly.com/badges/762fa7a4-9cf4-417d-bd29-7e072d74cdb7)
| [Oracle Certified Professional, Java SE 11 Programmer](https://www.credly.com/badges/87609d8e-27c5-45c9-9e42-60a5e9283280)
| [Oracle Certified Professional, JEE7 Developer](https://www.credly.com/badges/27a14e06-f591-4105-91ca-8c3215ef39a2)
| [IBM Cybersecurity Analyst Professional](https://www.credly.com/badges/ad1f4abe-3dfa-4a8c-b3c7-bae4669ad8ce)
| [Certified Advanced JavaScript Developer](https://cancanit.com/certified/1462/)
| [Certified Neo4j Professional](https://graphacademy.neo4j.com/certificates/c279afd7c3988bd727f8b3acb44b87f7504f940aac952495ff827dbfcac024fb.pdf)
| [Deep Learning](https://www.credly.com/badges/8d27e38c-869d-4815-8df3-13762c642d64)
| [![Generic badge](https://img.shields.io/static/v1.svg?label=GitHub&message=JEsperancinhaOrg&color=yellow&style=for-the-badge "jesperancinha.org dependencies")](https://github.com/JEsperancinhaOrg)
[![Generic badge](https://img.shields.io/static/v1.svg?label=All%20Badges&message=Badges&color=red&style=for-the-badge "All badges")](https://joaofilipesabinoesperancinha.nl/badges)
[![Generic badge](https://img.shields.io/static/v1.svg?label=Status&message=Project%20Status&color=red&style=for-the-badge "Project statuses")](https://github.com/jesperancinha/project-signer/blob/master/project-signer-quality/Build.md)
