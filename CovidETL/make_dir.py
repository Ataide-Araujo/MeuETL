import os


def make_dir(file_name):
    if not os.path.exists(f'{os.getcwd()}/{file_name}'):
            os.makedirs(f'{os.getcwd()}/{file_name}')
    return os.chdir(f'{os.getcwd()}/{file_name}')