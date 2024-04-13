from setuptools import setup


def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as file:
        requirements = []
        for line in file:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if '#' in line:
                continue
            if line.startswith('git+') or line.startswith('svn+') or line.startswith('hg+'):
                continue  # Skip VCS dependencies
            requirements.append(line)
    return requirements

requirements = load_requirements()

setup(
    name='cartoonsegmentation',
    version='0.1.0',
    py_modules=['examples', 'animeinsseg', 'anime_3dkenburns', 'depth_modules', 'utils', 'Web_UI'],  # List individual module files here
    scripts=['run_kenburns.py', 'run_style.py', 'naive_interface.py', 'repaint_person.py'],  # Scripts that should be accessible from the command line
    install_requires=[
        # Dependencies here, same as before
    ]
)

