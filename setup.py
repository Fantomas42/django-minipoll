from distutils.core import setup
import os

version = '0.1'

setup(name='django-minipoll',
      version=version,
      
      description='Django-MiniPoll is a django application who allow you to put a survey on your Django website.',
      long_description=open(os.path.join('README.rst')).read(),
      keywords='django, poll, survey',

      author='Fantomas42',
      author_email='fantomas42@gmail.com',
      url='http://github.com/Fantomas42/django-minipoll',
      license='BSD License',

      packages=['minipoll', 'minipoll.templatetags'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Framework :: Django',
          'Topic :: Software Development :: Libraries :: Python Modules',],
      )

