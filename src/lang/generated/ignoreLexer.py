# Generated from src/grammar/ignoreLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,48,430,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,
        7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
        2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,
        7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,
        2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,
        7,32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,
        2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,
        7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,1,0,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,5,
        14,197,8,14,10,14,12,14,200,9,14,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,5,15,211,8,15,10,15,12,15,214,9,15,1,15,1,15,1,16,1,
        16,5,16,220,8,16,10,16,12,16,223,9,16,1,16,3,16,226,8,16,1,17,4,
        17,229,8,17,11,17,12,17,230,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,
        28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,4,30,313,8,30,11,30,12,30,
        314,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,
        328,8,31,1,32,1,32,1,33,1,33,5,33,334,8,33,10,33,12,33,337,9,33,
        1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,3,37,348,8,37,1,37,
        4,37,351,8,37,11,37,12,37,352,1,38,3,38,356,8,38,1,38,4,38,359,8,
        38,11,38,12,38,360,1,38,1,38,5,38,365,8,38,10,38,12,38,368,9,38,
        1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,
        1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,394,
        8,46,1,47,1,47,1,47,1,47,3,47,400,8,47,1,48,1,48,1,48,1,48,5,48,
        406,8,48,10,48,12,48,409,9,48,1,48,1,48,1,48,1,48,1,48,1,49,1,49,
        1,49,1,49,1,50,1,50,1,50,1,50,5,50,424,8,50,10,50,12,50,427,9,50,
        1,50,1,50,3,198,335,407,0,51,2,0,4,0,6,1,8,2,10,3,12,4,14,5,16,6,
        18,7,20,8,22,9,24,10,26,11,28,12,30,13,32,14,34,0,36,15,38,16,40,
        17,42,18,44,19,46,20,48,21,50,22,52,23,54,24,56,25,58,26,60,27,62,
        28,64,29,66,30,68,31,70,32,72,33,74,34,76,35,78,36,80,37,82,38,84,
        39,86,40,88,41,90,42,92,43,94,44,96,45,98,46,100,47,102,48,2,0,1,
        7,1,0,48,57,2,0,10,10,13,13,2,0,65,90,97,122,4,0,48,57,65,90,95,
        95,97,122,82,0,32,32,8986,8987,9193,9196,9200,9200,9203,9203,9725,
        9726,9748,9749,9800,9811,9855,9855,9875,9875,9889,9889,9898,9899,
        9917,9918,9924,9925,9934,9934,9940,9940,9962,9962,9970,9971,9973,
        9973,9978,9978,9981,9981,9989,9989,9994,9995,10024,10024,10060,10060,
        10062,10062,10067,10069,10071,10071,10133,10135,10160,10160,10175,
        10175,11035,11036,11088,11088,11093,11093,126980,126980,127183,127183,
        127374,127374,127377,127386,127462,127487,127489,127489,127514,127514,
        127535,127535,127538,127542,127544,127546,127568,127569,127744,127776,
        127789,127797,127799,127868,127870,127891,127904,127946,127951,127955,
        127968,127984,127988,127988,127992,128062,128064,128064,128066,128252,
        128255,128317,128331,128334,128336,128359,128378,128378,128405,128406,
        128420,128420,128507,128591,128640,128709,128716,128716,128720,128722,
        128725,128727,128732,128735,128747,128748,128756,128764,128992,129003,
        129008,129008,129292,129338,129340,129349,129351,129535,129648,129660,
        129664,129672,129680,129725,129727,129733,129742,129755,129760,129768,
        129776,129784,3,0,9,10,13,13,32,32,2,0,60,60,62,62,445,0,6,1,0,0,
        0,0,8,1,0,0,0,0,10,1,0,0,0,0,12,1,0,0,0,0,14,1,0,0,0,0,16,1,0,0,
        0,0,18,1,0,0,0,0,20,1,0,0,0,0,22,1,0,0,0,0,24,1,0,0,0,0,26,1,0,0,
        0,0,28,1,0,0,0,0,30,1,0,0,0,0,32,1,0,0,0,0,36,1,0,0,0,0,38,1,0,0,
        0,0,40,1,0,0,0,0,42,1,0,0,0,0,44,1,0,0,0,0,46,1,0,0,0,0,48,1,0,0,
        0,0,50,1,0,0,0,0,52,1,0,0,0,0,54,1,0,0,0,0,56,1,0,0,0,0,58,1,0,0,
        0,0,60,1,0,0,0,1,62,1,0,0,0,1,64,1,0,0,0,1,66,1,0,0,0,1,68,1,0,0,
        0,1,70,1,0,0,0,1,72,1,0,0,0,1,74,1,0,0,0,1,76,1,0,0,0,1,78,1,0,0,
        0,1,80,1,0,0,0,1,82,1,0,0,0,1,84,1,0,0,0,1,86,1,0,0,0,1,88,1,0,0,
        0,1,90,1,0,0,0,1,92,1,0,0,0,1,94,1,0,0,0,1,96,1,0,0,0,1,98,1,0,0,
        0,1,100,1,0,0,0,1,102,1,0,0,0,2,104,1,0,0,0,4,106,1,0,0,0,6,108,
        1,0,0,0,8,118,1,0,0,0,10,130,1,0,0,0,12,134,1,0,0,0,14,140,1,0,0,
        0,16,148,1,0,0,0,18,154,1,0,0,0,20,161,1,0,0,0,22,169,1,0,0,0,24,
        174,1,0,0,0,26,181,1,0,0,0,28,189,1,0,0,0,30,192,1,0,0,0,32,206,
        1,0,0,0,34,225,1,0,0,0,36,228,1,0,0,0,38,234,1,0,0,0,40,244,1,0,
        0,0,42,255,1,0,0,0,44,260,1,0,0,0,46,263,1,0,0,0,48,265,1,0,0,0,
        50,273,1,0,0,0,52,287,1,0,0,0,54,291,1,0,0,0,56,302,1,0,0,0,58,304,
        1,0,0,0,60,307,1,0,0,0,62,312,1,0,0,0,64,327,1,0,0,0,66,329,1,0,
        0,0,68,331,1,0,0,0,70,340,1,0,0,0,72,342,1,0,0,0,74,344,1,0,0,0,
        76,347,1,0,0,0,78,355,1,0,0,0,80,369,1,0,0,0,82,371,1,0,0,0,84,373,
        1,0,0,0,86,375,1,0,0,0,88,377,1,0,0,0,90,379,1,0,0,0,92,381,1,0,
        0,0,94,393,1,0,0,0,96,399,1,0,0,0,98,401,1,0,0,0,100,415,1,0,0,0,
        102,419,1,0,0,0,104,105,7,0,0,0,105,3,1,0,0,0,106,107,5,45,0,0,107,
        5,1,0,0,0,108,109,5,60,0,0,109,110,5,102,0,0,110,111,5,117,0,0,111,
        112,5,110,0,0,112,113,5,99,0,0,113,114,5,116,0,0,114,115,5,105,0,
        0,115,116,5,111,0,0,116,117,5,110,0,0,117,7,1,0,0,0,118,119,5,60,
        0,0,119,120,5,47,0,0,120,121,5,102,0,0,121,122,5,117,0,0,122,123,
        5,110,0,0,123,124,5,99,0,0,124,125,5,116,0,0,125,126,5,105,0,0,126,
        127,5,111,0,0,127,128,5,110,0,0,128,129,5,62,0,0,129,9,1,0,0,0,130,
        131,5,60,0,0,131,132,5,105,0,0,132,133,5,102,0,0,133,11,1,0,0,0,
        134,135,5,60,0,0,135,136,5,47,0,0,136,137,5,105,0,0,137,138,5,102,
        0,0,138,139,5,62,0,0,139,13,1,0,0,0,140,141,5,60,0,0,141,142,5,47,
        0,0,142,143,5,101,0,0,143,144,5,108,0,0,144,145,5,105,0,0,145,146,
        5,102,0,0,146,147,5,62,0,0,147,15,1,0,0,0,148,149,5,60,0,0,149,150,
        5,101,0,0,150,151,5,108,0,0,151,152,5,105,0,0,152,153,5,102,0,0,
        153,17,1,0,0,0,154,155,5,60,0,0,155,156,5,101,0,0,156,157,5,108,
        0,0,157,158,5,115,0,0,158,159,5,101,0,0,159,160,5,62,0,0,160,19,
        1,0,0,0,161,162,5,60,0,0,162,163,5,47,0,0,163,164,5,101,0,0,164,
        165,5,108,0,0,165,166,5,115,0,0,166,167,5,101,0,0,167,168,5,62,0,
        0,168,21,1,0,0,0,169,170,5,60,0,0,170,171,5,118,0,0,171,172,5,97,
        0,0,172,173,5,114,0,0,173,23,1,0,0,0,174,175,5,60,0,0,175,176,5,
        47,0,0,176,177,5,118,0,0,177,178,5,97,0,0,178,179,5,114,0,0,179,
        180,5,62,0,0,180,25,1,0,0,0,181,182,5,116,0,0,182,183,5,121,0,0,
        183,184,5,112,0,0,184,185,5,101,0,0,185,186,5,61,0,0,186,187,1,0,
        0,0,187,188,3,34,16,0,188,27,1,0,0,0,189,190,3,22,10,0,190,191,3,
        34,16,0,191,29,1,0,0,0,192,193,5,47,0,0,193,194,5,42,0,0,194,198,
        1,0,0,0,195,197,9,0,0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,199,
        1,0,0,0,198,196,1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,
        5,42,0,0,202,203,5,47,0,0,203,204,1,0,0,0,204,205,6,14,0,0,205,31,
        1,0,0,0,206,207,5,47,0,0,207,208,5,47,0,0,208,212,1,0,0,0,209,211,
        8,1,0,0,210,209,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,215,1,0,0,0,214,212,1,0,0,0,215,216,6,15,0,0,216,33,
        1,0,0,0,217,221,7,2,0,0,218,220,7,3,0,0,219,218,1,0,0,0,220,223,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,226,1,0,0,0,223,221,
        1,0,0,0,224,226,7,4,0,0,225,217,1,0,0,0,225,224,1,0,0,0,226,35,1,
        0,0,0,227,229,7,5,0,0,228,227,1,0,0,0,229,230,1,0,0,0,230,228,1,
        0,0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,233,6,17,0,0,233,37,1,
        0,0,0,234,235,5,60,0,0,235,236,5,112,0,0,236,237,5,114,0,0,237,238,
        5,111,0,0,238,239,5,103,0,0,239,240,5,114,0,0,240,241,5,97,0,0,241,
        242,5,109,0,0,242,243,5,62,0,0,243,39,1,0,0,0,244,245,5,60,0,0,245,
        246,5,47,0,0,246,247,5,112,0,0,247,248,5,114,0,0,248,249,5,111,0,
        0,249,250,5,103,0,0,250,251,5,114,0,0,251,252,5,97,0,0,252,253,5,
        109,0,0,253,254,5,62,0,0,254,41,1,0,0,0,255,256,5,60,0,0,256,257,
        5,47,0,0,257,258,1,0,0,0,258,259,3,34,16,0,259,43,1,0,0,0,260,261,
        5,60,0,0,261,262,3,34,16,0,262,45,1,0,0,0,263,264,3,34,16,0,264,
        47,1,0,0,0,265,266,5,110,0,0,266,267,5,97,0,0,267,268,5,109,0,0,
        268,269,5,101,0,0,269,270,5,61,0,0,270,271,1,0,0,0,271,272,3,34,
        16,0,272,49,1,0,0,0,273,274,5,114,0,0,274,275,5,101,0,0,275,276,
        5,116,0,0,276,277,5,117,0,0,277,278,5,114,0,0,278,279,5,110,0,0,
        279,280,5,84,0,0,280,281,5,121,0,0,281,282,5,112,0,0,282,283,5,101,
        0,0,283,284,5,61,0,0,284,285,1,0,0,0,285,286,3,34,16,0,286,51,1,
        0,0,0,287,288,3,34,16,0,288,289,5,58,0,0,289,290,3,34,16,0,290,53,
        1,0,0,0,291,292,5,99,0,0,292,293,5,111,0,0,293,294,5,110,0,0,294,
        295,5,100,0,0,295,296,5,105,0,0,296,297,5,116,0,0,297,298,5,105,
        0,0,298,299,5,111,0,0,299,300,5,110,0,0,300,301,5,61,0,0,301,55,
        1,0,0,0,302,303,5,62,0,0,303,57,1,0,0,0,304,305,3,34,16,0,305,306,
        5,61,0,0,306,59,1,0,0,0,307,308,5,123,0,0,308,309,1,0,0,0,309,310,
        6,29,1,0,310,61,1,0,0,0,311,313,7,5,0,0,312,311,1,0,0,0,313,314,
        1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,316,1,0,0,0,316,317,
        6,30,0,0,317,63,1,0,0,0,318,319,5,70,0,0,319,320,5,97,0,0,320,321,
        5,108,0,0,321,322,5,115,0,0,322,328,5,101,0,0,323,324,5,84,0,0,324,
        325,5,114,0,0,325,326,5,117,0,0,326,328,5,101,0,0,327,318,1,0,0,
        0,327,323,1,0,0,0,328,65,1,0,0,0,329,330,3,34,16,0,330,67,1,0,0,
        0,331,335,5,34,0,0,332,334,9,0,0,0,333,332,1,0,0,0,334,337,1,0,0,
        0,335,336,1,0,0,0,335,333,1,0,0,0,336,338,1,0,0,0,337,335,1,0,0,
        0,338,339,5,34,0,0,339,69,1,0,0,0,340,341,5,58,0,0,341,71,1,0,0,
        0,342,343,5,40,0,0,343,73,1,0,0,0,344,345,5,41,0,0,345,75,1,0,0,
        0,346,348,3,4,1,0,347,346,1,0,0,0,347,348,1,0,0,0,348,350,1,0,0,
        0,349,351,3,2,0,0,350,349,1,0,0,0,351,352,1,0,0,0,352,350,1,0,0,
        0,352,353,1,0,0,0,353,77,1,0,0,0,354,356,3,4,1,0,355,354,1,0,0,0,
        355,356,1,0,0,0,356,358,1,0,0,0,357,359,3,2,0,0,358,357,1,0,0,0,
        359,360,1,0,0,0,360,358,1,0,0,0,360,361,1,0,0,0,361,362,1,0,0,0,
        362,366,5,46,0,0,363,365,3,2,0,0,364,363,1,0,0,0,365,368,1,0,0,0,
        366,364,1,0,0,0,366,367,1,0,0,0,367,79,1,0,0,0,368,366,1,0,0,0,369,
        370,5,61,0,0,370,81,1,0,0,0,371,372,5,42,0,0,372,83,1,0,0,0,373,
        374,5,47,0,0,374,85,1,0,0,0,375,376,5,43,0,0,376,87,1,0,0,0,377,
        378,5,45,0,0,378,89,1,0,0,0,379,380,5,37,0,0,380,91,1,0,0,0,381,
        382,5,47,0,0,382,383,5,47,0,0,383,93,1,0,0,0,384,385,5,61,0,0,385,
        394,5,61,0,0,386,387,5,33,0,0,387,394,5,61,0,0,388,389,5,62,0,0,
        389,394,5,61,0,0,390,394,7,6,0,0,391,392,5,60,0,0,392,394,5,61,0,
        0,393,384,1,0,0,0,393,386,1,0,0,0,393,388,1,0,0,0,393,390,1,0,0,
        0,393,391,1,0,0,0,394,95,1,0,0,0,395,396,5,38,0,0,396,400,5,38,0,
        0,397,398,5,124,0,0,398,400,5,124,0,0,399,395,1,0,0,0,399,397,1,
        0,0,0,400,97,1,0,0,0,401,402,5,47,0,0,402,403,5,42,0,0,403,407,1,
        0,0,0,404,406,9,0,0,0,405,404,1,0,0,0,406,409,1,0,0,0,407,408,1,
        0,0,0,407,405,1,0,0,0,408,410,1,0,0,0,409,407,1,0,0,0,410,411,5,
        42,0,0,411,412,5,47,0,0,412,413,1,0,0,0,413,414,6,48,0,0,414,99,
        1,0,0,0,415,416,5,125,0,0,416,417,1,0,0,0,417,418,6,49,2,0,418,101,
        1,0,0,0,419,420,5,47,0,0,420,421,5,47,0,0,421,425,1,0,0,0,422,424,
        8,1,0,0,423,422,1,0,0,0,424,427,1,0,0,0,425,423,1,0,0,0,425,426,
        1,0,0,0,426,428,1,0,0,0,427,425,1,0,0,0,428,429,6,50,0,0,429,103,
        1,0,0,0,19,0,1,198,212,221,225,230,314,327,335,347,352,355,360,366,
        393,399,407,425,3,6,0,0,5,1,0,5,0,0
    ]

class ignoreLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    expr = 1

    FUNCTION_TAG_OPEN = 1
    FUNCTION_TAG_END = 2
    IF_TAG = 3
    IF_END = 4
    ELIF_END = 5
    ELIF_TAG = 6
    ELSE = 7
    ELSE_END = 8
    VAR_DECL_START = 9
    VAR_DECL_END = 10
    VAR_DECL_TYPE = 11
    VAR_DECL = 12
    COMMENT = 13
    LINE_COMMENT = 14
    WS = 15
    OPEN_PROGRAM = 16
    CLOSE_PROGRAM = 17
    CLOSE_TAG = 18
    OPEN_TAG = 19
    TAG_REFERENCE = 20
    FUNCTION_NAME = 21
    FUNCTION_RET_TYPE = 22
    FUNCTION_PARAM = 23
    CONDITION_EQ = 24
    END_TAG = 25
    PROPERTY_NAME = 26
    OPEN_CURLY = 27
    EXPR_WS = 28
    LITERAL_BOOL = 29
    NAME = 30
    LITERAL_STRING = 31
    COLON = 32
    OPEN_PAREN = 33
    CLOSE_PAREN = 34
    LITERAL_INT = 35
    LITERAL_FLOAT = 36
    EQUALS = 37
    MUL = 38
    DIV = 39
    ADD = 40
    SUB = 41
    MOD = 42
    INT_DIV = 43
    OPERATOR_COMPARE = 44
    OPERATOR_LOGIC = 45
    EXPR_COMMENT = 46
    CLOSE_CURLY = 47
    EXPR_LINE_COMMENT = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "expr" ]

    literalNames = [ "<INVALID>",
            "'<function'", "'</function>'", "'<if'", "'</if>'", "'</elif>'", 
            "'<elif'", "'<else>'", "'</else>'", "'<var'", "'</var>'", "'<program>'", 
            "'</program>'", "'condition='", "'>'", "'{'", "':'", "'('", 
            "')'", "'='", "'*'", "'/'", "'+'", "'-'", "'%'", "'//'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", "IF_TAG", "IF_END", 
            "ELIF_END", "ELIF_TAG", "ELSE", "ELSE_END", "VAR_DECL_START", 
            "VAR_DECL_END", "VAR_DECL_TYPE", "VAR_DECL", "COMMENT", "LINE_COMMENT", 
            "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", 
            "TAG_REFERENCE", "FUNCTION_NAME", "FUNCTION_RET_TYPE", "FUNCTION_PARAM", 
            "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", "EXPR_WS", 
            "LITERAL_BOOL", "NAME", "LITERAL_STRING", "COLON", "OPEN_PAREN", 
            "CLOSE_PAREN", "LITERAL_INT", "LITERAL_FLOAT", "EQUALS", "MUL", 
            "DIV", "ADD", "SUB", "MOD", "INT_DIV", "OPERATOR_COMPARE", "OPERATOR_LOGIC", 
            "EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    ruleNames = [ "DIGIT", "NEGATIVE_SIGN", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", 
                  "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", "ELSE", "ELSE_END", 
                  "VAR_DECL_START", "VAR_DECL_END", "VAR_DECL_TYPE", "VAR_DECL", 
                  "COMMENT", "LINE_COMMENT", "ID", "WS", "OPEN_PROGRAM", 
                  "CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", 
                  "FUNCTION_NAME", "FUNCTION_RET_TYPE", "FUNCTION_PARAM", 
                  "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", 
                  "EXPR_WS", "LITERAL_BOOL", "NAME", "LITERAL_STRING", "COLON", 
                  "OPEN_PAREN", "CLOSE_PAREN", "LITERAL_INT", "LITERAL_FLOAT", 
                  "EQUALS", "MUL", "DIV", "ADD", "SUB", "MOD", "INT_DIV", 
                  "OPERATOR_COMPARE", "OPERATOR_LOGIC", "EXPR_COMMENT", 
                  "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    grammarFileName = "ignoreLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


