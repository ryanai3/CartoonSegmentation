from setuptools import setup, find_packages

def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as file:
        requirements = []
        for line in file:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if '#' in line:
                line = line[:line.index('#')].strip()
            if line.startswith('git+') or line.startswith('svn+') or line.startswith('hg+'):
                continue
            requirements.append(line)
    return requirements

requirements = load_requirements()

setup(
    name='cartoon_segmentation',
    version='0.1.0',
    packages=find_packages(),  # This will now find your newly organized package
    install_requires=requirements
)

