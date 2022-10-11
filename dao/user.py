from dao.model.user import User

class UserDAO():
    def __init__(self, session):
        self.session = session


    def get_all_users(self):
        return self.session.query(User).all()


    def get_user_by_id(self, uid):
        return self.session.query(User).filter(User.id == uid).one()


    def create_user(self, **kwargs):
        try:
            self.session.add(User(**kwargs))
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False


    def edit_user_by_id(self, uid, **kwargs):
        try:
            self.session.query(User).filter(User.id == uid).update(kwargs)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False


    def delete_user_by_id(self, uid):
        try:
            self.session.query(User).filter(User.id == uid).delete()
            self.session.commit()
            return True

        except Exception as e:
            print(e)
            self.session.rollback()
            return False