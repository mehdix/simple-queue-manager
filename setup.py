from setuptools import setup, find_packages

setup(name='sqmpy',
      version='v1.0.0-alpha.1',
      long_description='Simple Queue Manager, also sqmpy, is a web interface for submitting jobs to HPC resources.',
      description='A Simple Queue Manager',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      author='Mehdi Sadeghi',
      author_email='sade@iwm.fraunhofer.de',
      url='',
      data_files=[#('config', ['config.py']),
                  'sqmpy.db'],
      install_requires=['Flask',
                        'Flask-SQLAlchemy',
                        'Flask-Login',
                        'Flask-WTF',
                        'Flask-Admin',
                        'Flask-CSRF',
                        'enum34',
                        'saga-python',
                        'py-bcrypt'])
