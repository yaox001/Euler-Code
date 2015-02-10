{\rtf1\ansi\ansicpg1252\cocoartf1343\cocoasubrtf160
{\fonttbl\f0\fnil\fcharset0 TrebuchetMS;\f1\froman\fcharset0 TimesNewRomanPSMT;\f2\fnil\fcharset134 STHeitiSC-Light;
}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720

\f0\fs32 \cf0 \expnd0\expndtw0\kerning0
\'93\'94\'94A Pythagorean triplet is a set of three natural numbers, 
\f1\i\fs38 \expnd0\expndtw0\kerning0
a
\f0\i0\fs32 \expnd0\expndtw0\kerning0
 < 
\f1\i\fs38 \expnd0\expndtw0\kerning0
b
\f0\i0\fs32 \expnd0\expndtw0\kerning0
 < 
\f1\i\fs38 \expnd0\expndtw0\kerning0
c
\f0\i0\fs32 \expnd0\expndtw0\kerning0
, for which,\
\pard\pardeftab720\qc

\f1\i\fs38 \cf0 \expnd0\expndtw0\kerning0
a
\f0\i0\fs26 \expnd0\expndtw0\kerning0
\super 2
\fs32 \expnd0\expndtw0\kerning0
\nosupersub  + 
\f1\i\fs38 \expnd0\expndtw0\kerning0
b
\f0\i0\fs26 \expnd0\expndtw0\kerning0
\super 2
\fs32 \expnd0\expndtw0\kerning0
\nosupersub  = 
\f1\i\fs38 \expnd0\expndtw0\kerning0
c
\f0\i0\fs26 \expnd0\expndtw0\kerning0
\super 2
\fs32 \expnd0\expndtw0\kerning0
\nosupersub \
\pard\pardeftab720
\cf0 \expnd0\expndtw0\kerning0
For example, 3
\fs26 \expnd0\expndtw0\kerning0
\super 2
\fs32 \expnd0\expndtw0\kerning0
\nosupersub  + 4
\fs26 \expnd0\expndtw0\kerning0
\super 2
\fs32 \expnd0\expndtw0\kerning0
\nosupersub  = 9 + 16 = 25 = 5
\fs26 \expnd0\expndtw0\kerning0
\super 2
\fs32 \expnd0\expndtw0\kerning0
\nosupersub .\
There exists exactly one Pythagorean triplet for which 
\f1\i\fs38 \expnd0\expndtw0\kerning0
a
\f0\i0\fs32 \expnd0\expndtw0\kerning0
 + 
\f1\i\fs38 \expnd0\expndtw0\kerning0
b
\f0\i0\fs32 \expnd0\expndtw0\kerning0
 + 
\f1\i\fs38 \expnd0\expndtw0\kerning0
c
\f0\i0\fs32 \expnd0\expndtw0\kerning0
 = 1000.\
Find the product 
\f1\i\fs38 \expnd0\expndtw0\kerning0
abc
\f0\i0\fs32 \expnd0\expndtw0\kerning0
.\'94\'94\'94\
c=0\
prod=0\
for a in range (0,1001
\f2 ):\
	for b in range (0,1001-a):\
		if a<b:\
			c=1000-a-b\
			if a**2+b**2=c**2:\
				prod=a*b*c\
				break\
print prod}