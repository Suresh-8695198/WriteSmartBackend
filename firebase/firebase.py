from firebase_admin import auth

# Create a new Firebase user
def create_firebase_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return user
    except Exception as e:
        return str(e)

# Retrieve Firebase user by UID
def get_firebase_user(uid):
    try:
        user = auth.get_user(uid)
        return user
    except Exception as e:
        return str(e)
