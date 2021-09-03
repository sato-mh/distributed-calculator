#!/bin/bash -eu

if [ $# = 0 ]; then
    echo "USAGE"
    echo "  ./init.sh PROJECT_PATH"
    exit 1
fi

rename_project () {
    a=(${1//// })
    ppath=$1 pname=${a[${#a[@]}-1]}

    find . -type f -path ./init.sh -prune -o -type d -name .git -prune -o -type f -exec sed -i "s#intern2021.jp-east-1.gitlab.devops.nifcloud.com/common/skeleton/skeletonpy#$ppath#g" {} \;
    find . -type f -path ./init.sh -prune -o -type d -name .git -prune -o -type f -exec sed -i "s#skeletonpy#$pname#g" {} \;
}

echo $1

rename_project $1
