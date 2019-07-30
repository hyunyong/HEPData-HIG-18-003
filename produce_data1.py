#!/usr/bin/python3.7m

## the data
x_data = [
   0.25,
   0.29125,
   0.3325,
   0.37375,
   0.415,
   0.45625,
   0.4975,
   0.53875,
   0.58,
   0.62125,
   0.6625,
   0.70375,
   0.745,
   0.78625,
   0.8275,
   0.86875,
   0.91,
   0.95125,
   0.9925,
   1.03375,
   1.075,
   1.11625,
   1.1575,
   1.19875,
   1.24,
   1.28125,
   1.3225,
   1.36375,
   1.405,
   1.44625,
   1.4875,
   1.52875,
   1.57,
   1.61125,
   1.6525,
   1.69375,
   1.735,
   1.77625,
   1.8175,
   1.85875,
   1.9,
   1.94125,
   1.9825,
   2.02375,
   2.065,
   2.10625,
   2.1475,
   2.18875,
   2.23,
   2.27125,
   2.3125,
   2.35375,
   2.395,
   2.43625,
   2.4775,
   2.51875,
   2.56,
   2.60125,
   2.6425,
   2.68375,
   2.725,
   2.76625,
   2.8075,
   2.84875,
   2.89,
   2.93125,
   2.9725,
   3.01375,
   3.055,
   3.09625,
   3.1375,
   3.17875,
   3.22,
   3.26125,
   3.3025,
   3.34375,
   3.385,
   3.42625,
   3.4675,
   3.50875,
   3.55,
   3.59125,
   3.6325,
   3.67375,
   3.715,
   3.75625,
   3.7975,
   3.83875,
   3.88,
   3.92125,
   3.9625,
   4.00375,
   4.045,
   4.08625,
   4.1275,
   4.16875,
   4.21,
   4.25125,
   4.2925,
   4.33375,
   4.375,
   4.41625,
   4.4575,
   4.49875,
   4.54,
   4.58125,
   4.6225,
   4.66375,
   4.705,
   4.74625,
   4.7875,
   4.82875,
   4.87,
   4.91125,
   4.9525,
   4.99375,
   5.035,
   5.07625,
   5.1175,
   5.15875,
   5.2,
   5.24125,
   5.2825,
   5.32375,
   5.365,
   5.40625,
   5.4475,
   5.48875,
   5.53,
   5.57125,
   5.6125,
   5.65375,
   5.695,
   5.73625,
   5.7775,
   5.81875,
   5.86,
   5.90125,
   5.9425,
   5.98375,
   6.025,
   6.06625,
   6.1075,
   6.14875,
   6.19,
   6.23125,
   6.2725,
   6.31375,
   6.355,
   6.39625,
   6.4375,
   6.47875,
   6.52,
   6.56125,
   6.6025,
   6.64375,
   6.685,
   6.72625,
   6.7675,
   6.80875,
   6.85,
   6.89125,
   6.9325,
   6.97375,
   7.015,
   7.05625,
   7.0975,
   7.13875,
   7.18,
   7.22125,
   7.2625,
   7.30375,
   7.345,
   7.38625,
   7.4275,
   7.46875,
   7.51,
   7.55125,
   7.5925,
   7.63375,
   7.675,
   7.71625,
   7.7575,
   7.79875,
   7.84,
   7.88125,
   7.9225,
   7.96375,
   8.005,
   8.04625,
   8.0875,
   8.12875,
   8.17,
   8.21125,
   8.2525,
   8.29375,
   8.335,
   8.37625,
   8.4175,
   8.45875,
   8.5
]

y_data = [
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477055,
   0.1477891,
   0.1495,
   0.1609716,
   0.1819809,
   0.1788923,
   0.1604383,
   0.1669427,
   0.2040618,
   0.236125,
   0.217992,
   0.175993,
   0.1534686,
   0.1482988,
   0.1477363,
   0.1477216,
   0.1478631,
   0.1487133,
   0.151977,
   0.1597714,
   0.1704365,
   0.1762692,
   0.1716471,
   0.1610909,
   0.1526967,
   0.1489461,
   0.1479117,
   0.1477581,
   0.1480954,
   0.1506623,
   0.1613796,
   0.1862078,
   0.2137258,
   0.2166481,
   0.1915504,
   0.1646885,
   0.1517382,
   0.1485341,
   0.1493688,
   0.1549432,
   0.1706462,
   0.1992497,
   0.2303393,
   0.2447048,
   0.2395022,
   0.2385396,
   0.266459,
   0.3206852,
   0.3721049,
   0.3880273,
   0.3569187,
   0.2953855,
   0.2322022,
   0.1868908,
   0.1624339,
   0.1521918,
   0.1488123,
   0.1479259,
   0.1477401,
   0.1477088,
   0.1477046,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041,
   0.1477041
    ]

## print functions
prev_entry = 1
first = True
iCount = 0

for entry in x_data:
    low = prev_entry
    high = entry
    if not first:
        iCount += 1
        #print(iCount)
        print("  - {{low: {0}, high: {1}}}".format(low, high))
    prev_entry = entry
    first = False

iCount = 0
for entry in y_data:
    iCount += 1
    #print(iCount)
    print("  - value: {0}".format(entry))


