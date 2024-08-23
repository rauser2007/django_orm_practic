import django_setup

from users_and_roles.models import Role, User

role_admin = Role.objects.filter(role_type = "admin").first()

role_user = Role.objects.get(role_type = "user")

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