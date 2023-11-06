class SessionService():
    _instances = {}
    def __new__(cls, user_id):
        if user_id not in cls._instances:
            cls._instances[user_id] = super(SessionService, cls).__new__(cls)
            cls._instances[user_id].user_id = user_id
            cls._instances[user_id].sub = ""
            cls._instances[user_id].lab = ""
            cls._instances[user_id].variant = ""
            cls._instances[user_id].spec = ""
        return cls._instances[user_id]
    



