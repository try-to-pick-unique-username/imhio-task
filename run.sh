#!/usr/bin/env bash

BASEDIR=$(pwd)
ALLUREDIR=$BASEDIR/allure_reports

pytest -v -m API --alluredir=$ALLUREDIR

allure serve $ALLUREDIR