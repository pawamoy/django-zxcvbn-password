#!/bin/bash
rm -rf build
rm -rf dist
rm -rf src/*.egg-info
if tox -e check; then
  python setup.py clean --all sdist bdist_wheel
  success=true
  for d in dist/*; do
    twine register "$d" -r pypitest || success=false
  done
  if ${success}; then
    if twine upload --skip-existing dist/* -r pypitest; then
      for d in dist/*; do
        twine register "$d" -r pypi || success=false
      done
      if ${success}; then
        if ! twine upload --skip-existing dist/* -r pypi; then
          echo "Twine upload to PyPi failed" >&2
        fi; else echo "Twine register to PyPi failed" >&2
      fi; else echo "Twine upload to PyPiTest failed" >&2
    fi; else echo "Twine register to PyPiTest failed" >&2
  fi; else echo "Tox check failed" >&2
fi
