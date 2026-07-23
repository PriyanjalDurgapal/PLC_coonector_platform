#!/bin/bash

DB_NAME=$1
DB_USER=$2
DB_HOST=$3
DB_PASSWORD=$4

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

BACKUP_DIR="db_backup"

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

FILE="$BACKUP_DIR/${DB_NAME}_${DATE}.sql"

export PGPASSWORD="$DB_PASSWORD"

# Maximum allowed database size (50 GB)
MAX_SIZE_BYTES=$((50 * 1024 * 1024 * 1024))

echo "Checking database size..."

DB_SIZE=$(psql \
    -U "$DB_USER" \
    -h "$DB_HOST" \
    -d postgres \
    -tAc "SELECT pg_database_size('$DB_NAME');")

# Verify size was retrieved
if [ -z "$DB_SIZE" ]; then
    echo "ERROR: Unable to determine database size."
    unset PGPASSWORD
    exit 1
fi

echo "Database size: $DB_SIZE bytes"

# Stop if larger than 50 GB
if [ "$DB_SIZE" -gt "$MAX_SIZE_BYTES" ]; then
    echo "ERROR: Database size exceeds 50 GB."
    echo "Backup aborted."
    unset PGPASSWORD
    exit 1
fi

echo "Starting backup..."

pg_dump \
    -U "$DB_USER" \
    -h "$DB_HOST" \
    "$DB_NAME" \
    > "$FILE"

# Check if backup succeeded
if [ $? -ne 0 ]; then
    echo "ERROR: Backup failed."
    rm -f "$FILE"
    unset PGPASSWORD
    exit 1
fi

gzip "$FILE"

if [ $? -ne 0 ]; then
    echo "ERROR: Compression failed."
    rm -f "$FILE"
    unset PGPASSWORD
    exit 1
fi

unset PGPASSWORD

echo "Backup completed successfully."
echo "$FILE.gz"