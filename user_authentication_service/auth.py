def valid_login(self, email: str, password: str) -> bool:
        """
        Check if the provided credentials are valid.
        
        Args:
            email (str): The user email.
            password (str): The plain-text password.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        # Vérification stricte en bytes
        if bcrypt.checkpw(password.encode('utf-8'),
                         user.hashed_password.encode('utf-8')):
            return True
        
        return False
