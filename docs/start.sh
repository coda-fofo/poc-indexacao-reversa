#!/bin/bash

WORKSPACE=$1

if [[ -z $WORKSPACE ]]; then
    echo "Uso: ./start.sh <workspace>";
    exit 255;
fi


FILE=structurizr.war

if [ ! -f "$FILE" ]; then
    echo "=> Baixando o structurizr..."
    wget -O $FILE https://github.com/structurizr/lite/releases/download/v2025.03.28/structurizr-lite.war
fi

java -Djdk.util.jar.enableMultiRelease=false -jar $FILE $WORKSPACE