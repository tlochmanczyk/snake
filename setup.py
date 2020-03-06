from setuptools import setup

setup(name='gym_snake',
      version='0.0.1',
      install_requires=['gym']
)

setup(name='my_project',
      version='0.1.0',
      entry_points='''
            [gui_scripts]
            my_project = gym_snake.envs.__main__:main
      ''',
      )
