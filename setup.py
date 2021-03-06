from distutils.core import setup
setup(
  name = 'test1',
  packages = ['test1'],
  version = '0.0.1',
  license='MIT',
  description = 'Test easily a python import',
  author = 'René Brunner',
  author_email = 'rene.brunner@datamics.com',
  url = 'https://github.com/datamics/test1',
  download_url = 'https://github.com/datamics/test1/archive/refs/tags/0.0.1.tar.gz',
  keywords = ['testing', 'easy', 'import'],
  install_requires=[
          'validators'
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)