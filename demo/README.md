
# About demos

Folder `demo` contains different examples using Python features. This folder will populate examples with every task.

# Jupyter

Some examples are written using [Jupyter notebook](https://jupyter.readthedocs.io/en/latest/index.html).

PyCharm Community Edition doesn't support it. Here you can find information how to run them.

## Install

There are different [methods to install](https://jupyter.org/install.html) Jupyter.

If you use pip, you can install it with:

```console
$ pip install notebook
```

## Run

Use command:

```console
$ jupyter notebook
```

See [Running the Notebook](https://jupyter.readthedocs.io/en/latest/running.html#running) for more details.

## Change language

There are two solutions:

1. Change your browser language
2. Remove localization for your language from Jupyter:

   For this, you need to find where Jupyter is installed. For example:
   - `venv` (virtual environment) folder
   - Anaconda installation `c:\Anaconda3`

   Inside this folder, find the folder with your language (`fr_FR`, `ja_JP`, `nl`, `ru_RU`, `zh_CN`), e.g.:
   - `venv\Lib\site-packages\notebook\i18n\ru_RU`
   - `c:\Anaconda3\Lib\site-packages\notebook\i18n\ru_RU`

   Rename the folder by adding some suffix, e.g. `ru_RU` to `ru_RU_old` (or remove it).

   Restart your notebook.
