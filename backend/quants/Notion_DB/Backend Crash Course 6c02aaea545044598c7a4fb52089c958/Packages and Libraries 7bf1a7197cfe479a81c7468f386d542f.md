# Packages and Libraries

As you develop your Python-based apps and programs, you’ll make use of a wide variety of libraries to extend the functionalities of your code. Managing them is an important step to keeping your code shareable, so read about a few ways to do just that! 

---

# Package Managers

## Pip

`pip` is the most used Python package manager. Most Python distributions have `pip` automatically installed, and it is very easy to use, allowing you to install the most-used Python libraries. You can install / uninstall libraries like so:

```bash
pip install library_name
pip uninstall library_name
```

You can even install a collection of specified necessary modules for a project via a `requirements.txt` file like so:

```bash
pip install -r requirements.txt
```

- Extra Usage Cases
    
    List all packages in a Python environment:
    
    ```bash
    pip list 
    ```
    
    Create `requirements.txt` file. You can run this even if you have an existing `requirements` file to add any new packages!
    
    ```bash
    pip freeze > requirements.txt
    ```
    

********************Resources:********************

[🍊 Pip Documentation](https://pip.pypa.io/en/stable/installation/)

## Conda

`conda` is a package manager produced by Anaconda, one of the most widely-used distributions of base data science tools. `conda` operates very similarly to `pip`, and is a solid option if you are focused on building data science-related projects.

```bash
conda install library_name
```

`conda` also supports virtual environments for ease in dependency management: 

```bash
conda create -n env_name python=version_number
conda activate env_name
```

********************Resources:********************

[🟢 Anaconda Distribution](https://www.anaconda.com/products/distribution)

[🐉 Conda Documentation](https://docs.conda.io/en/latest/)

# Package Information

## [PyPI](https://pypi.org)

PyPI, the Python Package Index, is the ultimate resource for all Python libraries. It contains info on what each package does, release information, documentation, and all important links for any package you need. For example, here’s the PyPI entry for Django:

![Screenshot 2023-01-31 at 1.27.33 PM.png](Packages%20and%20Libraries%207bf1a7197cfe479a81c7468f386d542f/Screenshot_2023-01-31_at_1.27.33_PM.png)