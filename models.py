from database import get_connection


def insert_url(short_code, original_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO urls(short_code,original_url,status)
        VALUES(?,?,?)
        """,
        (short_code, original_url, "pending")
    )
    conn.commit()
    url_id = cursor.lastrowid
    conn.close()
    return url_id


def get_url(short_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM urls
        WHERE short_code=?
        """,
        (short_code,)
    )
    row = cursor.fetchone()
    conn.close()
    return row


def get_url_by_id(url_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM urls
        WHERE id=?
        """,
        (url_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return row


def update_status(url_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE urls
        SET status=?
        WHERE id=?
        """,
        (status, url_id)
    )
    conn.commit()
    conn.close()