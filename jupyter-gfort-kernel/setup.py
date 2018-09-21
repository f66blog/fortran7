from setuptools import setup

setup(name='jupyter_gfort_kernel',
      version='0.1.0',
      description='Minimalistic gfortran kernel for Jupyter with plotting features',
      author='f66blog',
      author_email='fortran667790@gmail.com',
      url='https://github.com/f66blog/fortran7',
      download_url='https://github.com/f66blog/jupyter-gfort-kernel/tarball/0.1.0',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: IPython',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Fortran',
      ],
      packages=['jupyter_gfort_kernel'],
      keywords=['jupyter', 'kernel', 'fortran']
)
