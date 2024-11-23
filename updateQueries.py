import sqlite3

def updateJob(cursor: sqlite3.Cursor, job_id: str, updates: dict) -> bool:

    try:
        fields_to_update = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [job_id]

        cursor.execute(f"UPDATE job SET {fields_to_update} WHERE job_id = ?", values)
        return True
    except sqlite3.Error as e:
        print(f"An error occurred while updating the job: {e}")
        return False


def updateDriverNin(cursor: sqlite3.Cursor, driver_id: str, new_nin: str) -> bool:

    try:
        cursor.execute("UPDATE driver SET NIN = ? WHERE driver_id = ?", (new_nin, driver_id))
        return True
    except sqlite3.Error as e:
        print(f"An error occurred while updating the NIN: {e}")
        return False

def updateUser(cursor: sqlite3.Cursor, user_id: str, updates: dict) -> bool:
    try:
        fields_to_update = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [user_id]

        cursor.execute(f"UPDATE user SET {fields_to_update} WHERE user_id = ?", values)
        return True
    except sqlite3.Error as e:
        print(f"An error occurred while updating user fields: {e}")
        return False

def updateAddress(cursor: sqlite3.Cursor, address_id: str, updates: dict) -> bool:
    try:
        fields_to_update = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [address_id]

        cursor.execute(f"UPDATE address SET {fields_to_update} WHERE address_id = ?", values)
        return True
    except sqlite3.Error as e:
        print(f"An error occurred while updating address fields: {e}")
        return False

def updateStaff(cursor: sqlite3.Cursor, staff_id: str, new_role: str) -> bool:
    try:
        cursor.execute("UPDATE staff SET role = ? WHERE staff_id = ?", (new_role, staff_id))
        return True
    except sqlite3.Error as e:
        print(f"An error occurred while updating the staff role: {e}")
        return False
