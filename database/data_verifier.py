class DataVerifier:
    @classmethod
    def verify_user_data(cls, user) -> (bool, str):
        if len(user.name) <= 2:
            return False, "User name must be longer than 2 characters"
        if len(user.password) <= 7:
            return False, "Password must be longer than 7 characters"
        if '@' not in user.email or '.' not in user.email:
            return False, "Email is incorrect"
        if not (0 <= user.get_years() <= 150):
            return False, "Invalid birth date"
        return True, ""
