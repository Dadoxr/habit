from users import models as u_m


def get_objects():
    return u_m.User.objects.all()
