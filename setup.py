from setuptools import setup, find_packages

setup(
    name='sql_injection_detector',
    version='0.11',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        "bson >= 0.5.10",
    ],
    author='Akshay Nair',
    author_email='aks7aynair@gmail.com',
    description='A library to detect SQL injection attempts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/akshaynair5/SQL_Injection_detector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    extras_require = {
        "dev" : ["pytest >= 7.0", "twine >= 4.0.2"],
    },
    python_requires='>=3.6',
)
