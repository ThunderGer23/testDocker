def userEntity(item) -> dict:
    """
    It takes a dictionary as an argument and returns a dictionary with the same keys but with different
    values
    
    :param item: The item that is being passed in from the database
    :return: A dictionary with the keys id, name, email, and password.
    """
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> list:
    """
    It takes a list of dictionaries and returns a list of dictionaries
    
    :param entity: The entity that you want to convert to a list of users
    :return: A list of userEntity objects
    """
    return [userEntity(item) for item in entity]