#!/usr/bin/env bash

MY_LINENO=0
SETTINGS_PY=test_settings.py
UNIVERSITIES_TXT=universities.txt

function addLastContent() {
    echo "]" >> ${SETTINGS_PY}
}

function addUniversity() {
    local uni=$1
    echo -e "\t('${uni}', '${uni}'),"
}

function addUniversities() {
    echo "added"
    while read -r UNI; do
        #echo "${UNI}"
        addUniversity "${UNI}" >> ${SETTINGS_PY}
    done < ${UNIVERSITIES_TXT}
}

function addHeadContent() {
    echo "UNIVERSITIES = [" >> ${SETTINGS_PY}
}

function clearUp() {
    head -n "$MY_LINENO" ${SETTINGS_PY} > temp_${SETTINGS_PY}
    mv temp_${SETTINGS_PY} ${SETTINGS_PY}
}

function learnLineNo() {
    MY_LINENO=$(grep -n "UNIVERSITIES" ${SETTINGS_PY} | awk -F ':' '{ print $1}')
    ((MY_LINENO--))
}

function main() {
    learnLineNo
    clearUp
    addHeadContent
    addUniversities
    addLastContent
}
main "$@"
