# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("..")
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from numpy import *
from dataStructure import GeneralTool
import time

import random
def load_rating_data(file_path='data.txt'):

    prefer = []
    for line in open(file_path, 'r'):  
        (userid, itemid, rating, date) = line.split('\t')  
        uid = int(userid)
        iid = int(itemid)
        rat = float(rating)
        prefer.append([uid, iid, rat])
    data = array(prefer)
    return data
def spilt_rating_dat(data, size=0.2):
    train_data = []
    test_data = []
    for line in data:
        rand = random.random()
        if rand < size:
            test_data.append(line)
        else:
            train_data.append(line)
    train_data = array(train_data)
    test_data = array(test_data)
    return train_data, test_data

class PMF(object):
    def __init__(self, num_feat=50, epsilon=0.8, _lambda=0.5, momentum=0.8,
                 maxepoch=100, num_batches=100,
                 batch_size=1000):
        self.num_feat = num_feat  # Number of latent features,
        self.epsilon = epsilon  # learning rate,
        self._lambda = _lambda  # regularization,
        self.momentum = momentum  # momentum of the gradient,
        self.maxepoch = maxepoch  # Number of epoch before stop,
        self.num_batches = num_batches  # Number of batches in each epoch (for SGD optimization),
        self.batch_size = batch_size  # Number of training samples used in each batches (for SGD optimization)

        self.w_C = None  # Movie feature vectors
        self.w_I = None  # User feature vectors

        self.err_train = []
        self.err_val = []
        self.data = None
        self.train_data = None
        self.test_data = None
        self.train_rmse = []
        self.test_rmse = []


    def fit(self, train_vec, val_vec):
        # mean subtraction
        self.mean_inv = np.mean(train_vec[:, 2])  # mean rating

        pairs_tr = train_vec.shape[0]  # traindata length
        pairs_va = val_vec.shape[0]  # testdata length

        # 1-p-i, 2-m-c

        num_user = int(max(np.amax(train_vec[:, 0]), np.amax(val_vec[:, 0]))) + 1  
        num_item = int(max(np.amax(train_vec[:, 1]), np.amax(val_vec[:, 1]))) + 1  

        incremental = False
        if ((not incremental) or (self.w_C is None)):
            # initialize
            self.epoch = 0
            self.w_C = 0.1 * np.random.randn(num_item, self.num_feat)  
            self.w_I = 0.1 * np.random.randn(num_user, self.num_feat)  

            self.w_C_inc = np.zeros((num_item, self.num_feat))  #  M x D 0 matrix
            self.w_I_inc = np.zeros((num_user, self.num_feat))  # N x D 0 matrix

        while self.epoch < self.maxepoch:
            self.epoch += 1

            # Shuffle training truples
            shuffled_order = np.arange(train_vec.shape[0])  
            np.random.shuffle(shuffled_order)  # permutation

            # Batch update
            for batch in range(self.num_batches):
                # print "epoch %d batch %d" % (self.epoch, batch+1)
                batch_idx = np.mod(np.arange(self.batch_size * batch, self.batch_size * (batch + 1)),
                                   shuffled_order.shape[0])  # index for this epoch
                batch_invID = np.array(train_vec[shuffled_order[batch_idx], 0], dtype='int32')
                batch_comID = np.array(train_vec[shuffled_order[batch_idx], 1], dtype='int32')

                # Compute Objective Function(error）
                pred_out = np.sum(np.multiply(self.w_I[batch_invID, :], self.w_C[batch_comID, :]),
                                  axis=1)  # mean_inv subtracted
                rawErr = pred_out - train_vec[shuffled_order[batch_idx], 2] + self.mean_inv

                # Compute gradients
                Ix_C = 2 * np.multiply(rawErr[:, np.newaxis], self.w_I[batch_invID, :]) + self._lambda * self.w_C[
                                                                                                         batch_comID, :]
                Ix_I = 2 * np.multiply(rawErr[:, np.newaxis], self.w_C[batch_comID, :]) + self._lambda * self.w_I[
                                                                                                         batch_invID, :]

                dw_C = np.zeros((num_item, self.num_feat))
                dw_I = np.zeros((num_user, self.num_feat))

                # loop to aggreate the gradients of the same element
                for i in range(self.batch_size):
                    dw_C[batch_comID[i], :] += Ix_C[i, :]
                    dw_I[batch_invID[i], :] += Ix_I[i, :]

                # Update with momentum
                self.w_C_inc = self.momentum * self.w_C_inc + self.epsilon * dw_C / self.batch_size
                self.w_I_inc = self.momentum * self.w_I_inc + self.epsilon * dw_I / self.batch_size
                self.w_C = self.w_C - self.w_C_inc
                self.w_I = self.w_I - self.w_I_inc

                # Compute Objective Function after
                if batch == self.num_batches - 1:
                    pred_out = np.sum(np.multiply(self.w_I[np.array(train_vec[:, 0], dtype='int32'), :],
                                                  self.w_C[np.array(train_vec[:, 1], dtype='int32'), :]),
                                      axis=1)  # mean_inv subtracted
                    rawErr = pred_out - train_vec[:, 2] + self.mean_inv
                    obj = LA.norm(rawErr) ** 2 + 0.5 * self._lambda * (LA.norm(self.w_I) ** 2 + LA.norm(self.w_C) ** 2)
                    self.err_train.append(np.sqrt(obj / pairs_tr))

                # Compute validation error
                if batch == self.num_batches - 1:
                    pred_out = np.sum(np.multiply(self.w_I[np.array(val_vec[:, 0], dtype='int32'), :],
                                                  self.w_C[np.array(val_vec[:, 1], dtype='int32'), :]),
                                      axis=1)  # mean_inv subtracted
                    rawErr = pred_out - val_vec[:, 2] + self.mean_inv
                    self.err_val.append(LA.norm(rawErr) / np.sqrt(pairs_va))

                    # Print info
                if batch == self.num_batches - 1:
                    print(self.epoch)
                    localtime = time.asctime(time.localtime(time.time()))
                    print("Local time is :" + str(localtime))
                    print('Training RMSE: %f, Test RMSE %f' % (self.err_train[-1], self.err_val[-1]))
                    self.train_rmse.append(self.err_train[-1])
                    self.test_rmse.append(self.err_val[-1])
                    # ****************Predict rating of all movies for the given user. ***************#

    def predict(self, invID):
        return np.dot(self.w_C, self.w_I[int(invID), :]) + self.mean_inv  




if __name__ == "__main__":

#    file_path = GeneralTool.getDataPath("review_final.txt")
    file_path = GeneralTool.getDataPath("review_final_part(30000user30000business).txt")
    pmf = PMF(num_feat=75, epsilon=0.8, _lambda=0., momentum=0.5,
                 maxepoch=100, num_batches=10,
                 batch_size=1000)
    ratings = load_rating_data(file_path)
    print(len(np.unique(ratings[:, 0])), len(np.unique(ratings[:, 1])), pmf.num_feat)
    train, test = spilt_rating_dat(ratings, 0.05)
    pmf.fit(train, test)
    print("Len(pmf.w_C)"+str(len(pmf.w_C)))
    print("Len(pmf.w_I)"+str(len(pmf.w_I)))
#Output result
    out1_filename ="item_vector_all.txt"
    out1 = open(GeneralTool.getDataPath(out1_filename), 'w')
    buffer = 0
    for i in pmf.w_C:
        for j in i:
            out1.write(str(j))
            out1.write('\t')
        out1.write('\n')
        buffer += 1
        if buffer == 5000:
            out1.flush()
            buffer = 0
            #print('flush5000')
    out1.close()
    out2_filename ="user_vector_all.txt"
    out2 = open(GeneralTool.getDataPath(out2_filename), 'w')
    buffer = 0
    for i in pmf.w_I:
        for j in i:
            out2.write(str(j))
            out2.write('\t')
        out2.write('\n')
        buffer += 1
        if buffer == 5000:
            out2.flush()
            buffer = 0
            #print('flush5000')
    out2.close()
    out3_filename ="global_bias.txt"
    out3 = open(GeneralTool.getDataPath(out3_filename), 'w')
    out3.write(str(pmf.mean_inv))
    out3.close()

    # Check performance by plotting train and test errors
    plt.plot(range(pmf.maxepoch), pmf.train_rmse, marker='o', label='Training Data')
    #plt.plot(range(pmf.maxepoch), pmf.test_rmse, marker='v', label='Test Data')
    plt.title('Learning Curve')
    plt.xlabel('Number of Epochs')
    plt.ylabel('RMSE')
    plt.legend()
    plt.grid()
    plt.show()
