#!/bin/bash
rm -rf build
rm -rf dist
rm -rf src/*.egg-info

read -rp "Are you sure tox is ok? [yN]: " tox_ok

proceed=0
case $tox_ok in
  y|Y|yes) proceed=1 ;;
esac

if [ ${proceed} -eq 1 ]; then
  python setup.py clean --all sdist bdist_wheel
  if twine upload --skip-existing dist/* -r pypitest; then
    if ! twine upload --skip-existing dist/* -r pypi; then
      echo "Twine upload to PyPi failed" >&2
    fi; else echo "Twine upload to PyPiTest failed" >&2
  fi; else echo "Then make tox happy." >&2
fi
