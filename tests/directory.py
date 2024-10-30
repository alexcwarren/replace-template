import os
import random
import shutil
from pathlib import Path
from string import ascii_lowercase, punctuation


class Directory:
    CHARACTERS: str = ascii_lowercase + punctuation

    def __init__(
        self,
        parent_dir: str,
        keywords: list[str],
        max_num_folders: int = 10,
        max_num_files: int = 10,
        seed=None,
    ):
        parent_path: Path = Path(parent_dir)
        self.__keywords: list[str] = keywords
        self.__max_num_folders: int = max_num_folders
        self.__max_num_files: int = max_num_files

        test_dir: str = "test_dir"
        self.__test_path: Path = parent_path.joinpath(test_dir)

        if self.__test_path.exists():
            self.remove_all()

        self.__test_path.mkdir(parents=True)
        self.path: str = str(self.__test_path)

        if seed:
            random.seed(seed)

        self.__create_contents()

    def __create_contents(self):
        """TODO"""
        # Create 1 to max number of folders.
        num_folders: int = random.randint(1, self.__max_num_folders)
        for i in range(num_folders):
            folder_name: str = self.__inject_keyword(f"subdir{i}")
            folder_path: Path = self.__test_path.joinpath(folder_name)
            folder_path.mkdir(parents=True)

            # In each folder, create 1 to max number of files.
            num_files: int = random.randint(1, self.__max_num_files)
            for j in range(num_files):
                file_name: str = self.__inject_keyword(f"file{j}")
                with folder_path.joinpath(file_name).open("w") as file:
                    # In each file, populate with random text intersparsed with at least
                    # 1 of each keyword.
                    num_lines: int = random.randint(10, 100)
                    for _ in range(num_lines):
                        word_length: int = random.randint(1, 10)
                        num_words: int = random.randint(1, 10)
                        line: str = " ".join(
                            "".join(random.choices(self.CHARACTERS, k=word_length))
                            for _ in range(num_words)
                        )
                        file.write(
                            f"{self.__inject_keyword(line, n = 2, guarantee = True)}\n"
                        )

    def __inject_keyword(self, text: str, n: int = 1, guarantee: bool = False):
        """TODO"""
        if n <= 0:
            return text

        # 50% chance injection happens (return if it doesn't)
        no_injection: bool = (not guarantee) and random.choice([True, False])
        if no_injection:
            return text

        if n > 1:
            final_text: str = ""
            inc: int = len(text) // n or 1
            i: int = 0
            for j in range(inc, len(text) + 1, inc):
                final_text += self.__inject_keyword(text[i:j])
                i = j
            return final_text

        # Randomly choose a keyword
        keyword: str = random.choice(self.__keywords)

        # Randomly choose insertion point in text
        insert_idx: int = random.randint(0, len(text) - 1)

        # Return modified text
        return text[:insert_idx] + keyword + text[insert_idx:]

    def traverse(self) -> list[str]:
        """Return a list of all folder names, file names, and file contents."""
        contents = os.listdir(self.__test_path)
        # print(c for c in contents)
        return [""]

    def remove_all(self):
        shutil.rmtree(self.__test_path)

    def __repr__(self):
        """TODO"""
        string: str = "Directory(\n"
        class_prefix: str = "_Directory__"
        longest: int = max(len(key) - len(class_prefix) for key in self.__dict__)
        for key, val in self.__dict__.items():
            string += f"    {key.removeprefix(class_prefix):{longest}} = {val}\n"
        string += ")"
        return string

    def __str__(self):
        """TODO"""
        return f'Directory("{self.__test_path.name}")'
