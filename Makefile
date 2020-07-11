{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red14\green32\blue46;\red245\green245\blue246;\red14\green114\blue164;
}
{\*\expandedcolortbl;;\cssrgb\c5882\c16863\c23922;\cssrgb\c96863\c96863\c97255;\cssrgb\c0\c52549\c70196;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\uc0\u8237 install:\uc0\u8236 \
    pip install --upgrade pip &&\\\
        pip install -r requirements.txt\
\
\pard\pardeftab720\partightenfactor0
\cf4 test\cf2 :\
    python -m pytest -vv \cf4 test\cf2 _hello.py\
\
\
lint:\
    pylint --disable=R,C hello.py\
\
all: install lint \cf4 test}