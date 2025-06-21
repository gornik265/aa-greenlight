from setuptools import setup, find_packages

setup(
    name='aa-greenlight',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='AllianceAuth plugin for Discord alert buttons',
    long_description=open('README.md').read(),
    url='https://github.com/YOUR_USERNAME/aa-greenlight',
    author='Your Name',
    author_email='your@email.com',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3'
    ],
    install_requires=['requests'],
)
