!!! NO STATIC !!!

# Endpoints

## AppManager

* singleton
* works like Service Locator

## AddingController

* add_new_user
    * require json, keeps data about User
    * service.add_user(user)
* add_message
    * require Message (user1_id, user2_id, msg_text, auth_key)
    * UserService().add_message(msg)
* add_image
    * require image
    * returns UserService().add_image(img)

## AuthController

* get_auth_key

# Internal

## AuthService

* get_auth_key
    * return key that may be used to
    * if not exists creates new auth key
* is_valid_key - checks

## User

### Конструктор (json_data : Any)

* требует:
    * user_id (optional)
    * name
    * password (optional)
    * birth_date (optional)
    * email (optional)