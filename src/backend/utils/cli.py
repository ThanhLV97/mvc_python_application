import click
from repositories.role_repository import RoleRepository, RoleUserRepository
from repositories.user_repository import UserRepository


@click.command('init_db')
def init_db():
    """Init master db"""
    try:
        RoleRepository.init_role()
        click.echo("Database seeded!")
    except Exception as e:
        click.echo(str(e))


@click.command('assign_role')
@click.argument('username')
@click.argument('role_name')
def assign_role(username: str, role_name: str) -> None:

    user = UserRepository.get_user_by_username(username)
    role = RoleRepository.get_by_name(role_name)

    if not user or not role:
        click.echo("Role is not assigned to user")

    RoleUserRepository.add_role_to_user(user, role)

    click.echo(f"Role {role_name} is not assigned to {username}") # @TODO Adjust messsage
