import os


# get filenames from `recently_labeled` directory
def get_filenames():
    try:
        result = []
        filenames = os.listdir('./recently_labeled')
        for filename in filenames:
            result.append(filename)
        return result
    except PermissionError:
        pass


# make text file of train.txt using `get_filenames`
def make_text_file(filenames):
    if filenames is not None:
        # make the result text
        result = []
        cnt_items = 0
        for filename in filenames:
            if '.png' in filename:
                item_to_path = f'data/obj/{filename}\n'
                cnt_items += 1
                result.append(item_to_path)
        # write into text file
        # divide into 8 : 2
        cnt_train = int(cnt_items * 0.8)
        cnt_validate = cnt_items - cnt_train
        # make `train.txt`
        with open('./train.txt', 'w') as train_file:
            write_text = ''.join(result[:cnt_train])
            train_file.write(write_text)
        # make `test.txt`
        with open('./test.txt', 'w') as test_file:
            write_text = ''.join(result[cnt_train:])
            test_file.write(write_text)
        # print msg
        print('[SUCCESS] train.txt and test.txt made successfully in current directory')
    else:
        print('[FAILED] the input value went wrong, please check the input data')
        return ValueError


if __name__ == "__main__":
    filenames = get_filenames()
    make_text_file(filenames=filenames)
