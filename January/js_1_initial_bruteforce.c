#include <stdio.h>
#include <stdlib.h>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int f(int a, int b, int c, int d){
    int i = 1;
    while(a+b+c+d > 0){
        int new_a = abs(a - b);
        int new_b = abs(b - c);
        int new_c = abs(c - d);
        int new_d = abs(a - d);

        a = new_a;
        b = new_b;
        c = new_c;
        d = new_d;

        ++i;
    }
    return i;
};

int main(){
    int n = 201;
    int max_M = 1;
    //int answer_vals[4] = {0, 8904, 25281, 55403};
    //int best_sum = 89588;
    int answer_vals[4] = {0,0,0,0};
    int best_sum = 100;

    int a = answer_vals[0];
    int b = answer_vals[1];
    int c = answer_vals[2];
    int d = answer_vals[3];

    while(a < n){
        b = 0;
        while(b < n){
            c = 0;
            while(c < n){
                d = 0;
                while(d < n){

                    int M = f(a,b,c,d);

                    if((M == max_M && best_sum > (a+b+c+d)) || M > max_M){
                        answer_vals[0] = a;
                        answer_vals[1] = b;
                        answer_vals[2] = c;
                        answer_vals[3] = d;
                        best_sum = a+b+c+d;
                        max_M = M;
                        printf("M: %d | combination: (%d,%d,%d,%d) | sum: %d\n",M,a,b,c,d,best_sum);
                    }
                    ++d;
                    //if(c * 3 < d){break;}
                }
                ++c;
                //if(b * 4 < c){break;}
            }
            ++b;
        }
        ++a;
    }

    return 0;
}

    
    
    