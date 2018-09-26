from setuptools import setup

setup(
    name='test_click',
    version='0.1',
    py_modules=['test_click'],
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        test_click=test_click:cli
    ''',
)
