#include <stdio.h>
#include <string.h>
#include <unistd.h>

// NOTE: Name the output executable to be 'sample_cgi.cgi' and
//       place it under ~user/public_html/cgi-bin .

// To setup an Apache2 httpd on Ubuntu:
//   1. atp-get install apache2
//   2. sudo a2enmod userdir
//      sudo a2enmod cgi
//   3. vi /etc/apache2/mods-enabled/userdir.conf
//      add the following conf:
//        <Directory /home/*/public_html/cgi-bin>
//            Options ExecCGI
//            SetHandler cgi-script
//        </Directory>
//   4. ensure ~user/public_html/cgi-bin exists. 

int main(int argc, char *argv[], char *environ[])
{
  char **envp;
  int i;
  int isPost = 0;

  printf("Content-type: text/html\n\n"
         "<html><head></head><body>\n");

  printf("<pre>This is CGI talking.</pre><hr/>");

  // Output environment variable list:
  printf("<pre>List of environment variables:\n");
  for (envp = environ; *envp; ++envp)
  {
    printf("%s\n", *envp);
    if (0 == strcmp(*envp, "REQUEST_METHOD=POST"))
      isPost = 1;
  }
  printf("</pre><hr/>");

  // Output input arguments
  printf("<pre>Commandline input arguments:\nargc=%d\n", argc);
  for (i=0; i<argc; ++i)
    printf("argv[%d]:%s\n", i, argv[i]);
  printf("</pre><hr/>");

  // Output data passed from STDIN when REQUEST_METHOD is 'POST'...
  // NOTE: Do not try to poll on stdin to check whether there is data.
  //       available. Somehow poll always returns there is data readable
  //       in stdin...
  if (isPost)
  {
    char buf[10240];
    printf("<pre>Read post data from STDIN:\n");
    memset(buf, 0, 10240);
    read(fileno(stdin), buf, 10240);
    printf("%s\n", buf);
    printf("</pre><hr/>");
  }

  printf("</body></html>\n");
  return 0;
}

