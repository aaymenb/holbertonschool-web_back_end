def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
    """Returns a User corresponding to a session_id"""
    if session_id is None:
        return None

    try:
        users = self._db.find_user_by(session_id=session_id)
        return users
    except Exception:
        return None
