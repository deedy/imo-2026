// Brute force for imo-2026-03.
// Model: LB chooses multiset b_1>=...>=b_{n+1}>=0 of integers summing to N
// (grid of resolution 1/N; b_i=0 means fewer marked points).
// XY refines: distributes at most n cuts among the pieces, each piece with c
// cuts is split into c+1 nonnegative integer parts (parts of size 0 emulate
// unused cuts / limits of tiny cuts). Payoff to LB: V=(N+D)/(2N) where D =
// alternating sum of all final parts sorted descending.
// XY minimizes D; LB maximizes the min. Program finds max-min D over grid.
//
// Usage:
//   ./brute n N            -> full search (two passes; prints all optimal configs)
//   ./brute n N b1 b2 ...  -> evaluate single LB config, print min D + witness
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int n, N, M; // M = n+1 pieces max
static int b[16];
static int parts[64];
static int nparts;
static long long curmin;
static long long pruneval;
static int aborted;
static long long best = -1;
static int witness[64], nwitness;
static int recordwitness = 0;

static void evalD(void){
  int tmp[64];
  for(int i=0;i<nparts;i++){
    int v=parts[i]; int j=i;
    while(j>0 && tmp[j-1]<v){tmp[j]=tmp[j-1]; j--;}
    tmp[j]=v;
  }
  long long d=0; int s=1;
  for(int i=0;i<nparts;i++){d+=(long long)s*tmp[i]; s=-s;}
  if(d<curmin){
    curmin=d;
    if(recordwitness){memcpy(witness,tmp,sizeof(int)*nparts); nwitness=nparts;}
    if(curmin<=pruneval) aborted=1;
  }
}

static void xy(int idx,int cuts);

static void gen(int idx,int cuts,int rem,int maxp){
  if(aborted) return;
  int hi = rem<maxp?rem:maxp;
  for(int p=hi;p>=1;p--){
    if((long long)p*(cuts+1)<rem) break; // cannot finish with parts <= p
    parts[nparts++]=p;
    if(p==rem) xy(idx+1,cuts);
    else gen(idx,cuts-1,rem-p,p); // guaranteed cuts>0 here by the break above
    nparts--;
  }
}

static void xy(int idx,int cuts){
  if(aborted) return;
  if(idx==M){ evalD(); return; }
  if(b[idx]==0){ xy(idx+1,cuts); return; }
  gen(idx,cuts,b[idx],b[idx]);
}

static long long minD(void){
  curmin=LLONG_MAX; aborted=0; nparts=0;
  xy(0,n);
  return curmin;
}

static void printconf(long long d){
  printf("minD = %lld / %d  : config (", d, N);
  for(int i=0;i<M;i++) printf("%d%s", b[i], i<M-1?", ":")");
  printf("  V = (N+D)/(2N) = %.6f\n", (double)(N+d)/(2.0*N));
}

static int pass; // 1 or 2

static void lb(int i,int rem,int maxp){
  if(i==M){
    if(rem!=0) return;
    pruneval = (pass==1)? best : best-1;
    long long d = minD();
    if(aborted) return;
    if(pass==1){
      if(d>best){ best=d; printconf(d); fflush(stdout); }
    } else {
      if(d==best){
        printconf(d);
        if(recordwitness){
          printf("   XY witness parts:");
          for(int k=0;k<nwitness;k++) printf(" %d", witness[k]);
          printf("\n");
        }
      }
    }
    return;
  }
  int hi = rem<maxp?rem:maxp;
  for(int v=hi;v>=0;v--){
    if((long long)v*(M-i)<rem) break;
    b[i]=v;
    lb(i+1,rem-v,v);
  }
  b[i]=0;
}

int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: brute n N [b1 b2 ...]\n");return 1;}
  n=atoi(argv[1]); N=atoi(argv[2]); M=n+1;
  if(argc>3){
    int sum=0;
    for(int i=0;i<M;i++){ b[i]= (3+i<argc)? atoi(argv[3+i]) : 0; sum+=b[i]; }
    if(sum!=N){fprintf(stderr,"config must sum to N\n");return 1;}
    pruneval=LLONG_MIN; recordwitness=1;
    long long d=minD();
    printconf(d);
    printf("   XY witness parts:");
    for(int k=0;k<nwitness;k++) printf(" %d", witness[k]);
    printf("\n");
    return 0;
  }
  pass=1; lb(0,N,N);
  printf("---- pass1 best D = %lld / %d ----\n", best, N);
  pass=2; recordwitness=1; lb(0,N,N);
  return 0;
}
