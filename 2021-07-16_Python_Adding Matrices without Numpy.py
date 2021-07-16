#Adding Matrices without Numpy
"Computer Programming Tutor, July16th,2021"

Mat1 = [[4,10,-6],
        [6,2,2],
        [4,3,3]
    ]

Mat2 = [[1,12,-6],
        [4,-3,3],
        [-1,3,3]
    ]

Mat3 = [[0,0,0],
        [0,0,0],
        [0,0,0]
    ]

#To Add Matrix 1 and Matrix 2 Matrices

for i in range(len(Mat1)):
    for k in range(len(Mat2)):
        Mat3[i][k] = Mat1[i][k] + Mat2[i][k]

#To Print The Matrix

print("Sum of Matrices: Mat1 and Mat2=",Mat3)
