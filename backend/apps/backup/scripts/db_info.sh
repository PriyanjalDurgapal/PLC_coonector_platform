#!/bin/bash


DB_NAME=$1
DB_USER=$2
DB_HOST=$3
DB_PASSWORD=$4
EMAIL_TO=$5


INFO_DIR="db_info"

DATE=$(date +"%Y-%m-%d_%H-%M-%S")


INFO_FILE="${INFO_DIR}/${DB_NAME}_info_${DATE}.txt"


EMAIL_SUBJECT="PostgreSQL Storage Info: ${DB_NAME} at ${DATE}"


EMAIL_BODY="Attached is database size and storage usage report for ${DB_NAME}"



export PGPASSWORD="$DB_PASSWORD"



mkdir -p "$INFO_DIR"



{

echo "=== Database Size Report for '$DB_NAME' ==="

echo ""


echo "-> Total Database Size:"

psql \
-U "$DB_USER" \
-h "$DB_HOST" \
-d "$DB_NAME" \
-c "SELECT pg_size_pretty(pg_database_size('$DB_NAME'));" \
-qAt



echo ""

echo "-> Size by Schema:"



psql \
-U "$DB_USER" \
-h "$DB_HOST" \
-d "$DB_NAME" \
-c "
SELECT 
nspname AS schema,
pg_size_pretty(
sum(pg_total_relation_size(pg_class.oid))
)
FROM pg_class
JOIN pg_namespace 
ON relnamespace = pg_namespace.oid
WHERE nspname NOT IN 
('pg_catalog','information_schema')
GROUP BY nspname;
"



echo ""

echo "-> Size by Table:"



psql \
-U "$DB_USER" \
-h "$DB_HOST" \
-d "$DB_NAME" \
-c "
SELECT
relname,
pg_size_pretty(
pg_total_relation_size(relid)
)
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
"



} > "$INFO_FILE"



# Send email

echo "$EMAIL_BODY" | \
mail \
-s "$EMAIL_SUBJECT" \
-a "$INFO_FILE" \
"$EMAIL_TO"



unset PGPASSWORD



echo "$INFO_FILE"