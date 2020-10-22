# Python script to rename multiple files in a directory or folder

import os

dir_path = "path to folder"

rename_file = "some name"  # part of a file name that needs to be renamed/removed

files_to_remove = ['name of a file to be removed 1', 'name of a file to be removed 2']

def main():
    for (dirpath, dirnames, filenames) in os.walk(dir_path):

        for item in filenames:
            if item in files_to_remove:
                try:
                    item_to_delete = os.path.join(dirpath, item)
                    os.remove(item_to_delete)
                    print("removed item:", item)
                except Exception as exc:
                    print(exc)

            elif rename_file in item:
                try:
                    new_item = item.replace(
                        rename_file, ""
                    )  # replacing 'rename_file' with empty space
                    print(new_item)
                    replace_item = os.path.join(dirpath, item)
                    replace_with = os.path.join(dirpath, new_item)
                    os.rename(replace_item, replace_with)
                except Exception as exc:
                    print(exc)

        for item in dirnames:
            if rename_file in item:
                try:
                    new_item = item.replace(rename_file, "")
                    replace_item = os.path.join(dirpath, item)
                    replace_with = os.path.join(dirpath, new_item)
                    os.rename(replace_item, replace_with)
                except Exception as exc:
                    print(exc)


if __name__ == "__main__":
    main()
