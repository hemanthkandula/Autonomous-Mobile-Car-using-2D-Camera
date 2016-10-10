#include <Servo.h>
Servo myservo;
void setup()
{myservo.attach(9);
pinMode(10,OUTPUT);
pinMode(11,OUTPUT);
 // put your setup code here, to run once:
Serial.begin(9600);
}
void loop()
{myservo.write(90);
 // put your main code here, to run repeatedly:
 while (Serial.available())
 {if (Serial.available() >0)
{ char c = Serial.read();
 if(c=='5')
 {myservo.write(90);
 straight();
 Serial.println('stright');}
if(c=='6')
{left();
Serial.println('left');}
if(c='4')
 {right();
 Serial.println('right');}
if(c=='7')
{steepleft1();
Serial.println('steepleft1');}
if(c=='3')
{steepright1();
Serial.println('steepright1');}
if(c=='8')
{steepleft2();
Serial.println('steepleft2');}
i
f(c=='2')
{steepright2();
Serial.println('steepright2');}
if(c=='9')
{steepleft3();
Serial.println('steepleft3');}
if(c=='1')
{steepright3();
Serial.println('steepright3');}
if(c=='a')
{steepleft4();
Serial.println('steepleft4');}
if(c=='0')
{steepright4();
Serial.println('steepright4');}}}}
void left()
 {myservo.write(60);
 straight(); }
void right()
{myservo.write(120);
 straight();
 }
void steepleft1()
{myservo.write(65);
 straight();} 
void steepright1()
{myservo.write(115);
 straight();}
void steepleft2()
{myservo.write(70);
 straight();}
void steepright2()
{myservo.write(110);
 straight();}
 void steepleft3()
{myservo.write(75);
 straight();} 
void steepright3()
{myservo.write(105);
 straight();}
 void steepleft4()
{myservo.write(80);
 straight();}
void steepright4()
{myservo.write(100);
 straight();}
void straight()
{digitalWrite(9,150)
 digitalWrite(10,LOW)}