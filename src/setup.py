from setuptools import setup, find_packages

setup(
    name="bytes_backend",
    version="0.1",
    packages=find_packages(),
    install_requires=['flask', 'mongoengine', 'flask-session'],
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
)
