if __name__ == "__main__":
    def get_text_from_text_file(dirname, file_name):
        try:
            with open(f".\{dirname}\{file_name}.txt", "r", encoding="utf-8") as file:
                text = file.read()
                file.close()
            return text
        except FileNotFoundError as e:
            print(e)

    def create_write_file(filename, dirname="texttemp", text="", extension="txt", encoding="utf-8"):
        try:

            with open(f"./{dirname}/{filename}.{extension}", "w", encoding=encoding) as file:
                file.write(text)
                file.close()

            return True

        except FileExistsError as e:
            print(e)
            return False

    def file_exist(arroffile, namefile):
        return bool([i for i in [i.split(".")[0] for i in arroffile] if i == namefile])

    def get_files_list(dirname):
        import os
        return os.listdir(dirname)
