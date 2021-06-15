from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='my_package',
      version='0.0.1',
      description='Image Processing',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent'
      ],
      url='https://github.com/Rohan-Raj-1729/MyPackage',
      author='Rohan-Raj-1729',
      author_email='mahajanrohanraj@gmail.com',
      keyword='configuration core yaml ini json environment',
      license='MIT',
      packages=['my_package'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False
      )
