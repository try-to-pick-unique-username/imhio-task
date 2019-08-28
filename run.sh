#!/usr/bin/env bash

BASEDIR=$(pwd)
ALLUREDIR=$BASEDIR/allure_reports

pytest -v -m API --alluredir=$ALLUREDIR
#pytest $BASEDIR/tests/webhook_test.py -v --alluredir=$BASEDIR/allure_reports

allure serve $ALLUREDIR