from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='coord_generator',
  version='0.0.4',
  description='A very basic random coordination generator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/DevER-M/coord_generator/upload',  
  author='Dever',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='random coordination generator', 
  packages=find_packages(),
  install_requires=['rand-password-generator','random-dice-roller']
) 