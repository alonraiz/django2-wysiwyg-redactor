import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django2-wysiwyg-redactor',
    version='1.0.0',
    description='django-wysiwyg-redactor is a lightweight responsive wysiwyg editor for Django',
    long_description=readme,
    author="Alon Raizman",
    url='https://github.com/alonraiz/django2-wysiwyg-redactor',
    license='MIT',
    packages=['redactor'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='django,admin,wysiwyg,editor,redactor,redactorjs',
)
