"""
Train the notebook on all the tasks through this script
"""

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def main(path: str, quant: bool = True):
    """
    Run all needed operations

    Args:
        path(str): The path of the notebook to be executed - this does everything we need
        quant(bool): Specify if we want to quantisize the model or not
    """

    try:
        with open(path, "r") as f:
            notebook = nbformat.read(f, as_version=4)

        ExecutePreprocessor(timeout=600, kernel_name="python.exe").preprocess(
            notebook, {"metadata": {"path": "./"}}
        )
    except Exception as err:
        raise err


if __name__ == "__main__":
    main("./Starter-Notebook.ipynb")
