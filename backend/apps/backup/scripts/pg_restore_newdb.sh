#!/bin/bash


DB_NAME=$1
DB_USER=$2
DB_HOST=$3
DB_PASSWORD=$4
BACKUP_FILE_GZ=$5


# Validate required inputs
if [ -z "$DB_NAME" ]; then
    echo "Database name is required."
    exit 1
fi

if [ -z "$DB_USER" ]; then
    echo "Database user is required."
    exit 1
fi

if [ -z "$DB_HOST" ]; then
    echo "Database host is required."
    exit 1
fi

if [ -z "$DB_PASSWORD" ]; then
    echo "Database password is required."
    exit 1
fi

if [ -z "$BACKUP_FILE_GZ" ]; then
    echo "Backup file is required."
    exit 1
fi


export PGPASSWORD="$DB_PASSWORD"


echo "================================="
echo "DATABASE RESTORE STARTED"
echo "================================="


echo "Database Name : $DB_NAME"
echo "User          : $DB_USER"
echo "Host          : $DB_HOST"
echo "Backup File   : $BACKUP_FILE_GZ"



# ---------------------------------
# Check backup file
# ---------------------------------

if [ ! -f "$BACKUP_FILE_GZ" ]
then
    echo "ERROR: Backup file not found"
    echo "Path: $BACKUP_FILE_GZ"
    exit 1
fi



# ---------------------------------
# Unzip backup
# ---------------------------------

echo ""
echo "Step 1: Unzipping backup..."
echo "--------------------------------"


gunzip -kf "$BACKUP_FILE_GZ"


if [ $? -ne 0 ]
then
    echo "ERROR: Unable to unzip backup file"
    exit 1
fi



SQL_FILE="${BACKUP_FILE_GZ%.gz}"


echo ""
echo "SQL File:"
echo "$SQL_FILE"



if [ ! -f "$SQL_FILE" ]
then
    echo "ERROR: SQL file does not exist"
    exit 1
fi



# ---------------------------------
# Clean existing database
# ---------------------------------

echo ""
echo "Step 2: Cleaning existing database..."
echo "--------------------------------"


psql \
-U "$DB_USER" \
-h "$DB_HOST" \
-d "$DB_NAME" \
-v ON_ERROR_STOP=1 \
-c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"


CLEAN_STATUS=$?


if [ $CLEAN_STATUS -ne 0 ]
then
    echo ""
    echo "ERROR: Database cleaning failed"
    exit $CLEAN_STATUS
fi



echo "Database cleaned successfully"



# ---------------------------------
# Restore database
# ---------------------------------

echo ""
echo "Step 3: Restoring database..."
echo "--------------------------------"



psql \
-U "$DB_USER" \
-h "$DB_HOST" \
-d "$DB_NAME" \
-v ON_ERROR_STOP=1 \
-f "$SQL_FILE"



RESTORE_STATUS=$?



echo "--------------------------------"



if [ $RESTORE_STATUS -ne 0 ]
then

    echo ""
    echo "================================="
    echo "ERROR: DATABASE RESTORE FAILED"
    echo "Exit Code: $RESTORE_STATUS"
    echo "================================="

    unset PGPASSWORD

    exit $RESTORE_STATUS

fi



# ---------------------------------
# Remove extracted SQL file
# ---------------------------------

echo ""
echo "Cleaning temporary SQL file..."

rm -f "$SQL_FILE"



echo ""
echo "================================="
echo "DATABASE RESTORED SUCCESSFULLY"
echo "================================="



unset PGPASSWORD

exit 0