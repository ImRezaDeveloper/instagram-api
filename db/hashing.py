from passlib.context import CryptContext

pcw_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password: str):
        return pcw_context.hash(password)
    
    def verify(hashed_password, password):
        return pcw_context.verify(password, hashed_password)