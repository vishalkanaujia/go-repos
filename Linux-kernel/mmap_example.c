#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include "assert.h"
#include <string.h> 

int main() {
    size_t pageSize = getpagesize();

    printf("system page size=%zu bytes\n", pageSize);
    int fd = open("/tmp/xx", O_RDONLY, 0);
    char *region = mmap(NULL, 4*pageSize, PROT_READ|PROT_EXEC, MAP_ANON|MAP_PRIVATE, fd, 0);
    assert(region != MAP_FAILED);

    printf("******");
    memset(region, 'y', pageSize);
    printf("-------------******");

    char read_buf[4096];
    memcpy(read_buf, region, pageSize);
    printf("char at 0 offset = %c\n", read_buf[0]);

    // cleanup
    int rc = munmap(region, 4*pageSize);
    assert(rc == 0);
    close(fd);
    return 0;
}