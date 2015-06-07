#include <stdio.h>

#define USE_EXTERN_DECL

// To get the pointer to the evironment variable array,
// you can either use 'extern' declaration or use the one
// passed in with main().

#ifdef USE_EXTERN_DECL

extern char **environ;
int main (int argc, char *argv[])

#else

int main(int argc, char *argv[], char *environ[])

#endif

{
  char **em;
  for ( em = environ; *em ; em++ )
    printf("%s\n", *em);

  return 0;
}

