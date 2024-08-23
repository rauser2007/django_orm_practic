import django_setup

from users_and_roles.models import Role, User

role_admin = Role.objects.get_or_create(role_type = "admin")

role_user = Role.objects.get_or_create(role_type = "user")

admin = User.objects.get_or_create(
    name = "Johnny",
    email = "bigjohn@hhmail.com",
    role = role_admin
)

user = User.objects.get_or_create(
    name = "Billy",
    email = "billy@hhmail.com",
    role = role_user
)