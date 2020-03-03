from setuptools import setup

setup(name='gym_snake',
      version='0.0.1',
      install_requires=['gym']  # And any other dependencies foo needs
)

setup(name='my_project',
      version='0.1.0',
      # packages=['my_project'],
      # entry_points={
      #     'gui_scripts': [
      #          'my_project = gym_snake.envs.__main__:main'
      #     ]
      entry_points='''
            [gui_scripts]
            my_project = gym_snake.envs.__main__:main
      ''',
      #},
      )