#!/bin/bash
set -e

BASE_DIR="$(dirname "$0")"

echoerr() { echo "! $@" 1>&2; }

get_project_version() {
    poetry -C "$BASE_DIR" version -s
}

remote="${1:-"origin"}"
version=$(get_project_version)
version_tag="v${version}"

echo "> Current version: $version"

if [[ -n $(git tag -l "$version_tag") ]]; then
    echoerr "Version $version already exists"
    exit 1
fi

read -p "? Are you sure about publishing version $version? " -n 1 -r REPLY
echo
if [[ "$REPLY" != "y" ]]; then
    echo "> Aborted!"
    exit 1
fi

# Empty commits allow users to change the version and commit the change
#  anytime they want.
echo "> Submitting version $version"
git add "$BASE_DIR/pyproject.toml"
git commit --allow-empty -m "Version $version"

commit_sha=$(git rev-parse --short HEAD)
echo "> Tagging $commit_sha with $version_tag"
git tag "$version_tag"

read -p "? Do you want to push version $version with tag $version_tag to $remote? " -n 1 -r REPLY
echo
if [[ "$REPLY" == "y" ]]; then
    echo "> Pushing version $version to $remote"
    git push
    git push "$remote" "$version_tag"
fi
