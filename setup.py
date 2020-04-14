from setuptools import setup

setup(name='jupyter_c_kernel_jw',
      version='1.2.1',
      description='Minimalistic C kernel for Jupyter',
      author='Brendan Rius',
      author_email='ping@brendan-rius.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/jjwhitham/jupyter-c-kernel/',
      download_url='https://github.com/jjwhitham/jupyter-c-kernel/tarball/1.2.1',
      packages=['jupyter_c_kernel_jw'],
      scripts=['jupyter_c_kernel_jw/install_c_kernel_jw'],
      keywords=['jupyter', 'notebook', 'kernel', 'c'],
      include_package_data=True
      )
