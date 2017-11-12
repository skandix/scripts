#include <Arduino.h>
#include "LedControl.h"

LedControl lc=LedControl(12,11,10,1);

void setup() {
  /*
  SHITTY LED CALCULATOR
  https://docs.google.com/spreadsheets/d/1qyp2JUK8UJE1qv_ri-mwP-QXXSorS0BZ7_uifsf6pwA/edit?usp=sharing
  */
  Serial.begin(9600);
  /*
   The MAX72XX is in power-saving mode on startup,
   we have to do a wakeup call
   */
  lc.shutdown(0,false);
  lc.setIntensity(0,9);
  lc.clearDisplay(0);
}

// SquareMiddle
void topR(int startRow, int endRow, int startCol, int endCol, bool pew, int speed, bool delayS, bool visable){
  for (int row=startRow;row<endRow;row++) {
      for(int col=startCol;col<endCol;col++) {
        lc.setLed(0,col,row,visable);
        lc.setIntensity(0,col);
        if(delayS == true){
          delay(speed);
        }
      }   
    }
  }

void topL(int startRow, int endRow, int startCol, int endCol, bool pew, int speed, bool delayS, bool visable){
  for (int row=startRow;row<endRow;row++) {
      for(int col=startCol;col<endCol;col++) {
        lc.setLed(0,col,row,visable);
        lc.setIntensity(0,col);
        if(delayS == true){
          delay(speed);
        }
      }   
    }
  }

void botR(int startRow, int endRow, int startCol, int endCol, bool pew, int speed, bool delayS, bool visable){
  for (int row=startRow;row<endRow;row++) {
      for(int col=startCol;col<endCol;col++) {
        lc.setLed(0,col,row,visable);
        lc.setIntensity(0,col);
        if(delayS == true){
          delay(speed);
        }
      }   
    }
  }

void botL(int startRow, int endRow, int startCol, int endCol, bool pew, int speed, bool delayS, bool visable){
  for (int row=startRow;row<endRow;row++) {
      for(int col=startCol;col<endCol;col++) {
        lc.setLed(0,col,row,visable);
        lc.setIntensity(0,col);
        if(delayS == true){
          delay(speed);
        }
      }   
    }
  }

void mid(int startRow, int endRow, int startCol, int endCol, bool pew, int speed, bool delayS, bool visable){
  for (int row=startRow;row<endRow;row++) {
      for(int col=startCol;col<endCol;col++) {
        lc.setLed(0,col,row,visable);
        lc.setIntensity(0,col);
        if(delayS == true){
          delay(speed);
        }
      }   
    }
  }


void fullOn(bool strobe){
  for(int k=0;k<8;k++){
      lc.setLed(0, k, k,true);
      delay(81);
  }
    for(int k=8;k>0;k--){
      lc.setLed(0, k, k,false);
      delay(81);
  }
  lc.clearDisplay(0);
}

void scanning(){
  for(int k=0;k<8;k++){
    for(int i=0;i<8;i++){
      lc.setLed(0,k,i,true);
      delay(5);
      lc.clearDisplay(0);
      //delay(5);
    }
  } 
}
void rng(){
 for(int k=0;k<8;k++){
  for(int i=0;i<8;i++){ 
    delay(5);
    lc.setLed(0,k*i,k,true);
    lc.setLed(0,k,k*2,true);
    delay(10);
    delay(10);
    }
  }
  lc.clearDisplay(0);
}

void seq(int speed, bool invertedOut){ 
  topR(0,4,4,8, false, speed, true, true);
  //###########################
  topL(4,8,4,8, false, speed, true, true);
  //###########################
  botR(0,4,0,4, false, speed, true, true);
  //###########################
  botL(4,8,0,4, false, speed, true, true);
  //###########################
  mid(2,6,2,6, false, speed, true, false);
  delay(600);

  if(invertedOut == true){
    delay(600);
    mid(2,6,2,6, false, speed, true, true);
    //###########################
    botL(4,8,0,4, false, speed, true, false);
    //###########################
    botR(0,4,0,4, false, speed, true, false);
    //###########################
    topL(4,8,4,8, false, speed, true, false);
    //###########################
    topR(0,4,4,8, false, speed, true, false);
    delay(1000);

  } else {
    lc.clearDisplay(0);
  }

}

  
void loop(){ 
  seq(3, true);
  delay(5);
  rng();
  delay(5);
  scanning();
  delay(5);
  fullOn(false);
  delay(5);
  fullOn(true);
  delay(5);
}
