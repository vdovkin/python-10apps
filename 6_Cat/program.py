import os
import cat_service


def main():
    start()

    folder = get_or_create_folder()
    download_cats(folder)


def start():
    print("********************")
    print("  cat factory app")
    print("********************")


def get_or_create_folder():
    basefolder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(basefolder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Create folder {}".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print("download ......")
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = "localcat {}".format(i)
        print("download {}".format(name))
        cat_service.get_cat(folder, name)

    print("Done")


if __name__ == "__main__":
    main()
