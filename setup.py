from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A short description of the project.',
    author='Alex',
    license='MIT',
    entry_point = '''
        [console_scripts]
        get_dataset=src.data.get_dataset:main
    ''',
)
