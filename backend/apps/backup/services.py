import os
import subprocess


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


SCRIPT_DIR = os.path.join(
    BASE_DIR,
    "apps",
    "backup",
    "scripts"
)



def create_backup(
    db_name,
    db_user,
    db_host,
    db_password
):

    script = os.path.join(
        SCRIPT_DIR,
        "pg_backup.sh"
    )


    result = subprocess.run(
        [
            script,
            db_name,
            db_user,
            db_host,
            db_password
        ],
        capture_output=True,
        text=True
    )


    if result.returncode != 0:

        raise Exception(
            result.stderr
        )


    return result.stdout



def restore_backup(
    backup_file,
    db_name,
    db_user,
    db_host,
    db_password
):

    backup_dir = os.path.join(
        BASE_DIR,
        "db_backup"
    )


    backup_path = os.path.join(
        backup_dir,
        backup_file
    )


    print("==============================")
    print("RESTORE DEBUG")
    print("Backup Path:", backup_path)
    print("Exists:", os.path.exists(backup_path))
    print("==============================")


    if not os.path.exists(backup_path):

        raise Exception(
            f"Backup file not found: {backup_path}"
        )


    script = os.path.join(
        SCRIPT_DIR,
        "pg_restore_newdb.sh"
    )


    print("Script:", script)



    result = subprocess.run(
        [
            "bash",
            script,
            db_name,
            db_user,
            db_host,
            db_password,
            backup_path
        ],
        capture_output=True,
        text=True
    )


    print("==============================")
    print("SCRIPT RETURN CODE:")
    print(result.returncode)

    print("SCRIPT OUTPUT:")
    print(result.stdout)

    print("SCRIPT ERROR:")
    print(result.stderr)

    print("==============================")



    if result.returncode != 0:

        raise Exception(
            result.stderr 
            or result.stdout
            or "Restore failed"
        )


    return result.stdout



def generate_db_info(
    db_name,
    db_user,
    db_host,
    db_password,
    email
):

    script = os.path.join(
        SCRIPT_DIR,
        "db_info.sh"
    )


    result = subprocess.run(
        [
            script,
            db_name,
            db_user,
            db_host,
            db_password,
            email
        ],
        capture_output=True,
        text=True
    )


    if result.returncode != 0:
        raise Exception(result.stderr)


    return result.stdout



def delete_backup(filename):

    backup_path = os.path.join(
        BASE_DIR,
        "db_backup",
        filename
    )

    if not os.path.exists(backup_path):
        raise Exception("Backup file not found.")

    os.remove(backup_path)

    return "Backup deleted successfully."