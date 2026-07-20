#!/bin/bash


DB_NAME=$1
DB_USER=$2
DB_HOST=$3
DB_PASSWORD=$4


BACKUP_DIR="db_backup"


DATE=$(date +"%Y-%m-%d_%H-%M-%S")


mkdir -p $BACKUP_DIR



FILE="$BACKUP_DIR/${DB_NAME}_${DATE}.sql"



export PGPASSWORD=$DB_PASSWORD



pg_dump \
-U $DB_USER \
-h $DB_HOST \
$DB_NAME \
> $FILE



gzip $FILE



unset PGPASSWORD



echo "$FILE.gz"