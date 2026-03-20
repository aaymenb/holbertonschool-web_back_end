def create_session(self, email: str) -> str:
        """
        Creates a new session for the user with the given email.

        Args:
            email (str): The user's email.

        Returns:
            str: The session ID (UUID) if the user exists, else None.
        """
        try:
            # 1. Trouver l'utilisateur
            user = self._db.find_user_by(email=email)
            
            # 2. Générer un nouvel UUID
            session_id = _generate_uuid()
            
            # 3. Mettre à jour l'utilisateur dans la DB
            self._db.update_user(user.id, session_id=session_id)
            
            return session_id
        except NoResultFound:
            return None
