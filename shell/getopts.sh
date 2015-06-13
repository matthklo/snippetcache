#!/bin/sh

# http://wiki.bash-hackers.org/howto/getopts_tutorial
#
# Usage: getopts {optstring} {argument} 
#          [{custom input parameters instead of $@}]
# Note: getopts stops at the first parameter which does not seems to be
#       a option (not starting with '-').
GETOPTERR=0
while getopts "fi:" arg; do
  case ${arg} in
    f)
       ;;
    i)
       echo ${OPTARG}
       ;;
    \?)
       GETOPTERR=1
       ;;
  esac
done

echo '$GETOPTERR =' $GETOPTERR
if [ 1 -eq ${GETOPTERR} ]; then
  exit 1
fi

echo '$OPTIND =' $OPTIND
if [ $# -gt $OPTIND ]; then
  shift `echo $OPTIND - 1 | bc`
  echo '$1 =' $1
fi

