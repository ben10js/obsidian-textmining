from setuptools import setup, find_packages
setup(
    name='obsidian_txtmining',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'konlpy', 'jpype1', 'scikit-learn', 'pandas', 'matplotlib', 'seaborn', 'wordcloud'
    ],
    author='Junsu Kim',
    description='Obsidian markdown Korean text mining toolkit.',
)
