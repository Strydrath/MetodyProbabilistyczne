#include <stdio.h>
#include <xmmintrin.h>
#include <math.h>

int generator(int liczba);


int main()
{
	
	int przedzialy[10] = { 0 };
	
	int p = 7;
	int q = 3;
	int m = 31;
	long long x = 0x00000096;
	for (int i = 0; i < 100000; i++) {
		x = generator(x);
		long long j = (x * 10) / (pow(2, m));
		przedzialy[j] += 1; 
		//printf("%d\n", x);
	}
	for (int a = 0; a < 10; a+=1) {
		printf("%d\n", przedzialy[a]);
	}
	return 0;
}