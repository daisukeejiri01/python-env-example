# python-env-example
## Python分析環境構築の例

このプロジェクトでは、`pyenv`、`poetry`、`tox`、`pytest`を用いたPython分析環境の構築方法例を示します。

## 環境構築手順

1. `pyenv`を用いてPythonのバージョンを管理します。以下のコマンドで特定のPythonバージョンをインストールできます。

```bash
pyenv install 3.8.6
pyenv global 3.8.6
```

2. `poetry`を用いてPythonのパッケージ依存関係を管理します。以下のコマンドで新しいプロジェクトを作成し、依存関係を追加します。
```bash
poetry new my_project
cd my_project
poetry add numpy pandas
```

3. `tox`を用いてテスト環境を自動化します。`tox.ini`ファイルをプロジェクトのルートディレクトリに作成し、以下のように設定します。
```bash
[tox]
envlist = py36,py37,py38

[testenv]
deps = pytest
commands = pytest
```

4. `pytest`を用いてユニットテストを行います。`tests`ディレクトリを作成し、その中にテストケースを記述したPythonファイルを作成します。

以上が、pyenv、poetry、tox、pytestを用いたPython分析環境の構築例です。各ツールの詳細な使用方法については、公式ドキュメンテーションを参照してください。