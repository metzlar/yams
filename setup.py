from setuptools import setup # pragma: no cover 

setup(
  name='YAMS (Yet Another Monitoring Service)',
  version='0.1',
  py_modules=['yams'],
  cmdclass={'upload':lambda x:None},
  install_requires=[
      'twisted',
      'python-memcached'
  ],
)# pragma: no cover 
 
