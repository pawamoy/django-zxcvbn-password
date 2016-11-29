#!/bin/bash
{ # Force shell to read entire script before executing it, thanks to compound command
  if [ $# -lt 2 ]; then
    echo "usage: ./update.sh PROJECT_PATH TEMPLATE_PATH [COMMIT_MESSAGE]" >&2
    exit 1
  fi

  # Initialize paths
  project=$1
  template=$2
  message=${3:-Update template branch}
  abs_project="$(cd "${project}"; pwd)"
  abs_template="$(cd "${template}"; pwd)"

  echo "Absolute path to project:  ${abs_project}"
  echo "Absolute path to template: ${abs_template}"
  echo "Commit message:            ${message}"
  echo

  # Git checkout template branch
  cd "${abs_project}"
  echo "> git checkout template"
  git checkout template >/dev/null 2>&1 || exit 1

  # Regenerate project
  echo "> regenerate cookiecutter"
  if ! cookiecutter --overwrite-if-exists --no-input \
               --config-file ".cookiecutterrc" \
               --output-dir .. "${abs_template}" >/dev/null; then
    echo
    echo "Problem during cookiecutter regeneration"
    exit 1
  fi

  # Git status, add, commit and push
  echo "> git status -sb"
  git status -sb | tail -n+2
  echo
  echo "> git add, commit and push"
  git add . -A
  if git commit -m "${message}"; then
    git push >/dev/null 2>&1
    echo
    echo "Now checkout your main branch, merge template one,"
    echo "fix conflicts if any then commit and push!"
  fi
  exit 0 # Force shell to exit here and not to read anything added after this compound command
}
