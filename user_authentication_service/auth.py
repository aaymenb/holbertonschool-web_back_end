def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        Returns the User object based on a session ID.

        Args:
            session_id (str): The session ID to look for.

        Returns:
            Optional[User]: The User object if found, otherwise None.
        """
        if session_id is None:
            return None

        try:
            # On utilise la méthode publique find_user_by
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
