from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
requirements = [x for x in requirements
                if ((len(x) > 0)
                     and (x[0] != '-')
                     and ("+" not in x)
                     and (x[0] != "# ")) ]
requirements = [x.replace("python-", "python_") for x in requirements]
dependencies = ["https://github.com/semantic-web-company/nif/tarball/master#egg=nif-0.0.0"]

setup(
    name='pp_api',
    version='profit-v16',
    description='Library for accessing PoolParty APIs',
    packages=['pp_api'],
    license='MIT',
    dependency_links=dependencies,
    install_requires=requirements,
)
