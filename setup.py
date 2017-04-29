from setuptools import setup

setup(name='recolor_dots',
      version='0.1.1',
      description='Templates for dotfile recoloring',
      url='http://github.com/raghavsub/recolor-dots',
      author='Raghav Subramaniam',
      author_email='raghavs511@gmail.com',
      license='MIT',
      packages=['recolor_dots'],
      entry_points={'console_scripts': ['recolor=recolor_dots.main:main']},
      install_requires=['docopt', 'pystache', 'pyyaml'])
