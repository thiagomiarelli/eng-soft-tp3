import pytest
from crud import insert, update, delete, get

def test_insert_new_record():
    """
    Test inserting a new record
    """
    result = insert("John Doe", 30, "john.doe@example.com")
    assert result == {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }

def test_insert_invalid_email():
    """
    Test inserting a record with an invalid email
    """
    with pytest.raises(Exception):
        insert("Jane Doe", 25, "jane.doe@example")

def test_insert_existing_email():
    """
    Test inserting a record with an existing email
    """
    with pytest.raises(Exception):
        insert("Jane Doe", 25, "john.doe@example.com")

def test_update_existing_record():
    """
    Test updating an existing record
    """
    result = update("john.doe@example.com", "John Smith", 35)
    assert result == {
        "name": "John Smith",
        "age": 35,
        "email": "john.doe@example.com"
    }

def test_update_nonexistent_record():
    """
    Test updating a non-existent record
    """
    with pytest.raises(Exception):
        update("jane.doe@example.com", "Jane Smith", 30)

def test_delete_existing_record():
    """
    Test deleting an existing record
    """
    delete("john.doe@example.com")
    with pytest.raises(Exception):
        get("john.doe@example.com")

def test_delete_nonexistent_record():
    """
    Test deleting a non-existent record
    """
    with pytest.raises(Exception):
        delete("jane.doe@example.com")

def test_get_existing_record():
    """
    Test getting an existing record
    """
    insert("John Smith", 35, "john.doe@example.com")
    result = get("john.doe@example.com")
    assert result == {
        "name": "John Smith",
        "age": 35,
        "email": "john.doe@example.com"
    }

def test_get_nonexistent_record():
    """
    Test getting a non-existent record
    """
    with pytest.raises(Exception):
        get("jane.doe@example.com")