import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()

    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(file) for file in files])


def check_integrity():
    files = get_files()

    results = []

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['prev_hash']

        pre_file = str(file - 1)
        actual_hash = get_hash(pre_file)

        if h == actual_hash:
            res = 'OK'
        else:
            res = 'Corrupted'

        results.append({'block': pre_file, 'result': res})

    return results


def write_block(name, amount, to_whom, pre_hash=''):
    files = get_files()

    if files:
        pre_file = files[-1]
        filename = str(pre_file + 1)
        pre_hash = get_hash(str(pre_file))
    else:
        filename = 1

    data = {
        'name': name,
        'amount': amount,
        'to_whom': to_whom,
        'prev_hash': pre_hash
    }

    with open(blockchain_dir + str(filename), 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    pass


if __name__ == '__main__':
    main()
