from setuptools import setup

requires = [
    'requests>=2.18.4',
    'rx>=1.6.1',
    'websocket-client>=0.47.0',
]

setup(
    name='mailcatcher',
    version='0.1.6',
    description='Simple mailcatcher client for Python.',
    url='https://github.com/kamiazya/py-mailcatcher',
    author='kamiazya',
    author_email='yuki@kamiazya.tech',
    license='MIT',
    keywords='mailcatcher development rx',
    py_modules=[
        'mailcatcher',
    ],
    package_dir={
        '': 'src',
    },
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    project_urls={
        # 'Source': 'https://github.com/kamiazya/py-mailcatcher',
    }
)
