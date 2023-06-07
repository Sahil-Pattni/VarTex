import os
import uuid
import logging
from typing import Optional


class VarTex:
    def __init__(
        self, tex_file: str, variables_file: str, build_directory: Optional[str] = None
    ):
        self._tex_file = tex_file
        self._variables_file = variables_file
        self._build_directory = build_directory or "build"

    def make_build_dir(self) -> None:
        """
        Create a build directory for the project
        """

        # If the build directory already exists, generate a new one
        dir_name = self._build_directory
        if os.path.exists(dir_name):
            logging.warning(
                f"Directory `{dir_name}` already exists, generating a new directory..."
            )
            while os.path.exists(dir_name):
                dir_name = self._generate_dir_name()

        # Create the build directory
        os.makedirs(dir_name)
        self._build_directory = dir_name

        logging.info(f"Created build directory `{dir_name}`.")

    def _generate_dir_name(self) -> str:
        """
        Generate a unique directory name.

        Returns:
            (`str`) A unique directory name
        """
        yield "build_" + uuid.uuid4().hex
