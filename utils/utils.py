import pathlib
import uuid

def generate_filename_user_avatar(instance, filename):
    return generate_filename(instance, filename, 'users')

def generate_filename_product(instance, filename):
    return generate_filename(instance, filename, 'products')


def generate_filename_blog(instance, filename):
    return generate_filename(instance, filename, 'blog')


def generate_filename(instance, filename, subdir):
    return pathlib.Path(subdir) / f"{uuid.uuid4().hex}.{filename.split('.')[-1]}"
