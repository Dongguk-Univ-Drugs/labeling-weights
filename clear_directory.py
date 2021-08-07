import os
import shutil
from datetime import date


# get filenames from `recently_labeled` directory
def get_filenames():
    try:
        return os.listdir('./recently_labeled')

    except PermissionError:
        pass


def create_backup(filenames):
    if filenames is not None:
        today = date.today().strftime('%m-%d-%y')
        src = './recently_labeled/'
        des = f'./backups/{today}/'
        shutil.copytree(src, des)
        print('[SUCCESS] the files have been moved to `backups` directory')
    else:
        return ValueError


def clear_recently_labeled(filenames):
    if filenames is not None:
        for filename in filenames:
            os.remove(f'./recently_labeled/{filename}')
        print(
            '[SUCCESS] the files have been removed from `recently_labeled` directory'
        )
    else:
        print(
            '[FAILED] the input value went wrong, please check the input data')
        return ValueError



if __name__ == "__main__":
    filenames = get_filenames()
    # create backup first
    create_backup(filenames=filenames)
    # then remove
    clear_recently_labeled(filenames=filenames)
