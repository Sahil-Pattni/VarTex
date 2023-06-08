import re
import uuid
import pathlib


class Latex:
    def __init__(self, tex_file: str, variables: dict):
        self.__filepath = tex_file
        self.__filename = pathlib.Path(tex_file).name
        self._read_file(tex_file)
        self.__variables = {}

    def _read_file(self) -> None:
        """
        Read the tex file.
        """
        with open(self.tex_file, "r") as f:
            self.__contents = f.read()

    def _replace_variables(self) -> None:
        """
        Replace the variables in the tex file.
        """
        for key, value in self.__variables.items():
            pattern = r"\\newcommand{\\" + key + r"}{(.+)}"
            self.__contents = re.sub(
                pattern,
                r"\\newcommand{" + key + r"}{" + value[-1] + r"}",
                self.__contents,
            )

    def write_file(self, directory: str) -> None:
        """
        Write the tex file.

        Args:
            directory (`str`): The directory to write the file to.
        """
        with open(f"{directory}/{self.__filename}_{uuid.uuid4().hex}", "w") as f:
            f.write(self.__contents)
