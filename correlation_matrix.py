#! /usr/bin/env python

import math
import numpy as np
import sys
import io




def mean(l_Z):
    Z_tot = 0
    N = len(l_Z)
    for i in range(N):
        Z_tot += l_Z[i] / N
    return Z_tot

def s_XY(l_X,l_Y):
    XY_tot = 0
    if  len(l_X) != len(l_Y):
        return NAN
    else:
        X_mean = mean(l_X)
        Y_mean = mean(l_Y)
        N = len(l_X)
        for i in range(N):
            XY_tot += (l_X[i] - X_mean)*(l_Y[i]-Y_mean)/N
    return XY_tot

def s_Z(l_Z):
    Z_tot = 0
    Z_mean = mean(l_Z)
    N = len(l_Z)
    for i in range(N):
        Z_tot += (l_Z[i] - Z_mean)*(l_Z[i] - Z_mean)/N
    return math.sqrt(Z_tot)

def correl_factor(l_X,l_Y):
    c_XY = s_XY(l_X,l_Y) / ( s_Z(l_X) * s_Z(l_Y) )
    return c_XY

def correlation_matrix(data):
    data_dim = data.shape
    M_correlation = np.matrix( np.zeros((data_dim[1],data_dim[1])) )
    for u in range(data_dim[1]):
        for v in range(data_dim[1]):
            M_correlation[u,v] = correl_factor(data[:,u],data[:,v])
    np.set_printoptions(precision=2,linewidth=100)
    print(M_correlation)


def main():
    data_file = open(sys.argv[1], 'r')
    correlation_matrix(np.loadtxt(data_file))



if __name__ == "__main__":
    main()
