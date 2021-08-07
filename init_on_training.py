# used for copying files
import shutil
import os


# get filenames from `recently_labeled` directory
def get_filenames():
    try:
        result = []
        filenames = os.listdir('./recently_labeled')
        for filename in filenames:
            result.append(filename[:-4])
        return result
    except PermissionError:
        pass


def copy_files(filenames):
    if filenames is not None:
        # destination directory
        base_des = r'./on_training/'
        # copy images
        base_image_src = r'./images/'
        # copy labels
        base_label_src = r'./recently_labeled/'

        for filename in filenames:
            if filename.isnumeric():
                image_src = f'{filename}.jpg'
                file_src = f'{filename}.txt'
                if os.path.isfile(base_image_src + image_src):
                    # copy images
                    shutil.copy(base_image_src + image_src, base_des)
                if os.path.isfile(base_label_src + file_src):
                    # copy files
                    shutil.copy(base_label_src + file_src, base_des)

        print('[SUCCESS] the files have been moved to `on_training` directory')

    else:
        print('[FAILED] the input value went wrong, please check the input data')
        return ValueError


if __name__ == "__main__":
    filenames = get_filenames()
    copy_files(filenames=filenames)
