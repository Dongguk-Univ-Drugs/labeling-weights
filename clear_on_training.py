import os


def clear_on_training():
    dir = './on_training/'
    cnt = 0
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        cnt += 1
    print(f'{cnt} files have been removed')


if __name__ == "__main__":
    clear_on_training()
