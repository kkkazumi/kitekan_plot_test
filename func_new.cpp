#include <math.h>
#include <iostream>
#include <fstream>

//encourage, symp, teasing, unrelated, no action,

int func_num[10][4] = {{0,1,2,3},{4,5,6,7},{8,9,10,11},
  {12,13,14,15},{16,17,18,19},{20,21,22,23},
  {24,25,26,27},{28,29,30,31},{32,33,34,35},{36,37,38,39}};

double sig(double factor,double a,double b,double c){
  return 1.0/(1.0+exp(a*(b*factor-c)));
}

double gauss(double factor, double a, double b, double c){
  return exp(-1.0*pow((a*factor-b),2.0)/c);
}

double inv_down(double factor, double a, double b){
  double A = pow(2.0,a);
  double B = A - 1.0;
  double C = b * factor + 1;
  double D = pow(C,a);
  return A/(B*D) - 1.0/B;
}

double inv_up(double factor,double a,double b){
  double A = pow(2.0,a);
  double B = A - 1.0;
  double C = b * factor + 1;
  double D = pow(C,a);
  return (D-1.0)/B;
}

//1〜10種類ある予測関数番号をもらうと計算をする関数を作ります
double func(double factor, double mental, int func_num){
  double a,b,c;
  double ret;
  //time of trial ##
  switch(func_num){
    case 0:
      //time of trial happy
      a = 2.0*(mental+3.0);
      b = 1.0/80.0;
      c = 0.3;
      ret = sig(factor,a,b,c);
      break;
    case 1:
      //time of trial sup
      a = 2.0*(mental+5.0);
      b = 1.0/80.0;
      c = 0.5;
      ret = sig(factor,a,b,c);
      break;
    case 2:
      //time of trial ang
      a = -3.0*(mental + 3.0);
      b = 1.0 / 80.0;
      c = 0.3;
      ret = sig(factor,a,b,c);
      break;
    case 3:
      //time of trial sad
      a = 1.0/80.0;
      b = 0.3;
      c = 0.05/(mental+1.0);
      ret = gauss(factor,a,b,c);
      break;
    //### rate of wins
    case 4:
      // rate of wins happy
      a = 10.0/(mental+1.0);
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 5:
      // rate of wins sup
      a = 10.0/(mental+1.0);
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 6:
      //rate of wins ang
      a = 2.0*(mental + 5.0);
      b = 1.0;
      c = 0.5;
      ret = sig(factor,a,b,c);
      break;
    case 7:
      // rate of wins sad
      a = 2.0*(mental/2.0+4.0);
      b = 1.0;
      ret = inv_down(factor,a,b);
      break;

    case 8:
      //encourage hap
      a = 1.0;
      b = 0.7;
      c = mental/100.0;
      ret = gauss(factor,a,b,c);
      break;
    case 9:
      //encourage sup
      a = 1.0;
      b = 0.8;
      c = mental / 80.0;
      ret = gauss(factor,a,b,c);
      break;
    case 10:
      //encourage ang
      a = 0.9 * mental;
      b = 1.0;
      ret = inv_down(factor,a,b);
      break;
    case 11:
      //encourage sad
      a = mental;
      b = 1.0;
      ret = inv_down(factor,a,b);

      break;
    case 12:
      //symp hap
      a = 1.0;
      b = 0.4;
      c = mental / 300.0;
      ret = gauss(factor,a,b,c);
      break;
    case 13:
      //symp sup
      a = 1.0;
      b = 0.6;
      c = mental / 300.0;
      ret = gauss(factor,a,b,c);
      break;
    case 14:
      //symp ang
      a = 0.9 * mental;
      b = 1.0;
      ret = inv_down(factor,a,b);
      break;
    case 15:
      //symp sad
      a = mental;
      b = 1.0;
      ret = inv_down(factor,a,b);
      break;

    case 16:
      //teasing hap
      a = 1.0;
      b = 0.2;
      c = mental/300.0;
      ret = gauss(factor,a,b,c);
      break;
    case 17:
      //teasing sup
      a = 1.0;
      b = 0.5;
      c = mental/200.0;
      ret = gauss(factor,a,b,c);
      break;
    case 18:
      //teasing ang
      a = 0.8 * mental;
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 19:
      //teasing sad
      a = 0.8 * mental;
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;

    case 20:
      //unrelated hap
      a = 1.0;
      b = 0.6;
      c = mental/100.0;
      ret = gauss(factor,a,b,c);
      break;
    case 21:
      //unrelated sup
      a = 10.0/(mental+1.0);
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 22:
      //unrelated ang
      a = 0.9 * mental;
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 23:
      //unrelated sad
      a = 1.4 * mental;
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;

    case 24:
      //no action hap
      a = 10.0/(mental+1.0);
      b = 1.0;
      ret = inv_down(factor,a,b);
      break;
    case 25:
      //no action sup
      a = 10.0/(mental+1.0);
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 26:
      //no action ang
      a = 0.7 * (5.0*mental/2.0)+1.0;
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;
    case 27:
      //no action sasd
      a = 2.0 * mental + 1.0;
      b = 1.0;
      ret = inv_up(factor,a,b);
      break;

    case 28:
      //total point hap
      a = -14.0 * (mental + 1.0);
      b = 1.0 / 240.0;
      c = 0.3/(mental+1.0);
      ret = sig(factor,a,b,c);
      break;
    case 29:
      //total point sup
      a = -2.0 * (2.0 * mental + 5.0);
      b = 1.0 / 240.0;
      c = 0.4/(mental+1.0);
      ret = sig(factor,a,b,c);
      break;
    case 30:
      //total point ang
      a = -4.0 * (1.5 * mental + 4.0);
      b = 1.0 / 240.0;
      c = 0.4/(mental+1.0);
      ret = sig(factor,a,b,c);
      break;
    case 31:
      //total point sad
      a = 3.0 * (1.5 * mental + 4.0);
      b = 1.0 / 240.0;
      c = 0.5/(mental+1.0) - 0.2;
      ret = sig(factor,a,b,c);
      break;
    case 32:
      //consecutive wins hap
      a = -20.0 * (mental+1.0);
      b = 1.0 / 80.0;
      c = 0.5/(mental+1.0);
      ret = sig(factor,a,b,c);
      break;
    case 33:
      //consecutive wins sup
      a = -15.0 * (mental+2.0);
      b = 1.0 / 80.0;
      c = 0.5/(mental+1.0);
      ret = sig(factor,a,b,c);
      break;
    case 34:
      //consecutive wins ang
      a = 0.6 * mental;
      b = 1.0 / 80.0;
      ret = inv_down(factor,a,b);
      break;
    case 35:
      //consecutive wins sad
      a = 2.0 * mental;
      b = 1.0 / 80.0;
      ret = inv_down(factor,a,b);
      break;

    case 36:
      //consecutive losses hap
      a = 0.7 * mental;
      b = 1.0 / 80.0;
      ret = inv_down(factor,a,b);
      break;
    case 37:
      //consecutive losses sup
      a = 0.3 * mental;
      b = 1.0 / 80.0;
      ret = inv_down(factor,a,b);
      break;
    case 38:
      //consecutive losses ang
      a = -0.3 / (mental+1.0);
      b = 1.0 / 80.0;
      c = 0.03 *(mental + 1.0);
      ret = sig(factor,a,b,c);
      break;
    case 39:
      //consecutive losses sad
      a = -300.0 / (mental+1.0);
      b = 1.0 / 80.0;
      c = 0.02 * (mental+1.0);
      ret = sig(factor,a,b,c);
      break;

  return ret;
  }
}

double inv_norm(int num, double val){
  double norm_val[40] = {80,80,80,80,
            1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,
            320,320,320,320,
            80,80,80,80,
            80,80,80,80};

  if((num == 28)||(num == 29)||(num==30)||(num==31)){
    val = val * norm_val[num] - 80.0;
  }else{
    val = val*norm_val[num];
  }
  return val;
}
