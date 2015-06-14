#!/bin/sh

my_test()
{
  read LINE
  while [ ! -z "${LINE}" ]; do
    echo $LINE
    read LINE
  done
}


my_test <<EOF
this is a cat
this is a dog
#this is a comment
EOF

