from setuptools import setup

setup(
    name='social-auth-backend-epita',
    version='0.0.5',
    author='Nicolas Geniteau',
    author_email='nicolas@lse.epita.fr',
    description='Social Auth backend for epita connect',
    license='GPL',
    packages=['epita_connect'],
    install_requires=[
        'social-auth-core[openidconnect]',
        'pyjwkest',
    ],
    include_package_data=True,
)
