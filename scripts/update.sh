#!/bin/bash
{ # Force shell to read entire script before executing it, thanks to compound command
  if [ $# -lt 2 ]; then
    echo "usage: ./update.sh PROJECT_PATH COOKIECUTTER_PATH [COMMIT_MESSAGE]" >&2
    exit 1
  fi

  # Initialize paths
  project=$1
  cookiecutter=$2
  message=${3:-Update cookiecutter branch}
  abs_project="$(cd "${project}"; pwd)"
  abs_cookiecutter="$(cd "${cookiecutter}"; pwd)"

  echo "Absolute path to project:      ${abs_project}"
  echo "Absolute path to cookiecutter: ${abs_cookiecutter}"
  echo "Commit message:                ${message}"
  echo

  # Git checkout cookiecutter branch
  cd "${abs_project}"
  echo "> git checkout cookiecutter"
  git checkout cookiecutter >/dev/null 2>&1 || exit 1

  # Regenerate project
  echo "> regenerate cookiecutter"
  if ! cookiecutter --overwrite-if-exists --no-input \
               --config-file ".cookiecutterrc" \
               --output-dir .. "${abs_cookiecutter}" >/dev/null; then
    echo
    echo "Problem during cookiecutter regeneration"
    exit 1
  fi

  # Git status, add, commit and push
  echo "> git status -sb"
  git status -sb | tail -n+2
  echo
  echo "> git add and commit"
  git add . -A
  if git commit -m "${message}"; then
    echo
    echo "Now checkout your main branch, merge cookiecutter one,"
    echo "fix conflicts if any then commit and push!"
  fi
  exit 0 # Force shell to exit here and not to read anything added after this compound command
}
