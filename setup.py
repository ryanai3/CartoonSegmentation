from setuptools import setup, find_packages

def load_requirements(filename='requirements.txt'):
    standard_reqs = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if '#' in line:
                line = line[:line.index('#')].strip()
            if line.startswith('git+') or line.startswith('svn+') or line.startswith('hg+'):
                # These are VCS dependencies that cannot be processed here
                continue
            else:
                standard_reqs.append(line)
    return standard_reqs

requirements = load_requirements()

setup(
    name='cartoonsegmentation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements
)

