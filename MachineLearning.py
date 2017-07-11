"""
iGemModel
Author: Angelo
File: MachineLearning.py
Date: 15/06/17
Environment: PyCharm Community Edition
"""

from sklearn.svm import LinearSVC
import numpy as np
from utils import *
from random import sample


class linearSVC():
    def __init__(self, sample_size):
        self.__mehtod = LinearSVC()
        self.__sample_size = sample_size
        self.__average_acc = 0

    def extract_features(self, data):
        """
        This will extract the features, from the spacers.
        Feature-wise:
        A -> 2
        C -> 3
        G -> 4
        T -> 5
        Then it will return two different lists inside a dictionary,
        these lists are the features
        :param data: [['AGG','+',45],['TGG','-',0],...]
        :return: {'l_a': [[[2,4,4],1],[[2,3,3],0],...], 'h_a': []}
        """
        low_activation = []
        high_activation = []
        counter = 0
        for d in data:
            features = []
            seq = d[0]
            for _ in seq:
                if _ == 'A':
                    features.append(2)
                elif _ == 'C':
                    features.append(3)
                elif _ == 'G':
                    features.append(4)
                elif _ == 'T':
                    features.append(5)
            if counter < 2016:
                low_activation.append([features, 0])
            else:
                high_activation.append([features, 1])
            counter += 1
        return {'h_a': high_activation, 'l_a': low_activation}

    def train_data(self, data):
        """
        This will train the SVM model.
        It will create two lists, one for the features and
        the classe where the features belong
        :param data: [[[2,4,4],1],[[2,3,3],0],...]
        :return: None
        """
        features = []
        classes = []
        for d in data:
            features.append(d[0])
            classes.append(d[1])
        self.__mehtod.fit(features, classes)

    def predict_data(self, features):
        """
        This will take some features and try to predict their classes class.
        :param features: [[2,4,4],[3,4,4],...]
        :return: None
        """
        features = np.asarray(features)
        for f in features:
            print self.__mehtod.predict(np.asarray(f[0]).reshape(1, -1))

    def get_sample(self, data, quantity):
        """
        Create random sample from the given population. Quantity is the size
        of the population. It will return unique random positions in the array.
        :param data: [[[2,3,3],0],[3,3,3],1],...]
        :param quantity: 300
        :return: [23,45,55,12]
        """
        return sample(range(len(data)), quantity)

    def get_accuracy(self, testing_data):
        """
        This will return the accuracy of the model. The input is again the features
        and the classes they belong into and it will return a float number,
        representing the percentage of correct classifications.
        :param testing_data: [[[4,4,4],1],[3,4,4],0],...]
        :return: 0.56
        """
        features = []
        classes = []
        for d in testing_data:
            features.append(d[0])
            classes.append(d[1])
        return self.__mehtod.score(features, classes)

    def execute(self, data, run_times=1):
        """
        This is the main function of the class. It will do all the work for you,
        sequentially. The run_times parameter is how many times you want to run
        the experiment.
        :param data: [['AGG','+',23],['TGG','-',44],...]
        :param run_times: 23
        :return: None
        """
        features = self.extract_features(data)
        print features
        for run in range(run_times):
            low_sample_features = lsvc.get_sample(features['l_a'], self.__sample_size)
            high_sample_features = lsvc.get_sample(features['h_a'], self.__sample_size)
            low_sample = [features['l_a'][i] for i in low_sample_features]
            high_sample = [features['h_a'][i] for i in high_sample_features]
            train_sample = low_sample[:self.__sample_size/2] + high_sample[:self.__sample_size/2]
            print low_sample
            print high_sample
            print train_sample
            self.train_data(train_sample)

            test_sample = low_sample[self.__sample_size/2:] + high_sample[self.__sample_size/2:]

            self.__average_acc += lsvc.get_accuracy(test_sample)
        print 'Average Accuracy {}'.format(self.__average_acc)
        self.__average_acc = 0

class spacer_cropper:
    def __init__(self):
        """
        This is used to crop the spacers in different ways.
        """
        self.__crop_method = None

    def crop(self, data):
        for _ in data:
            _[0] = self.__crop_method(_[0])
        return data

    def spacer(self, data):
        return data

    def pam_minus_10(self, seq):
        s = 10
        end = -3
        return seq[len(seq) - s + end : end]

    def pam_plus_10(self, seq):
        s = 10
        end = -3
        return seq[len(seq) - s + end:]

    def pam(self, seq):
        end = -3
        return seq[end:]

    def spacer_selection(self, selection='spacer'):
        if selection == 'spacer':
            self.__crop_method = self.spacer
        elif selection == '10-pam':
            self.__crop_method = self.pam_minus_10
        elif selection == '10+pam':
            self.__crop_method = self.pam_plus_10
        elif selection == 'pam':
            self.__crop_method = self.pam
        else:
            raise ValueError('wrong input!')


if __name__ == '__main__':

    for method in ['pam']: #,'spacer', '10-pam', '10+pam',
        print 'Method: ' + method
        d = read_csv('data_1499344220.18.csv')
        sc = spacer_cropper()
        sc.spacer_selection(method)
        cropped_data = sc.crop(d)
        lsvc = linearSVC(600)
        lsvc.execute(cropped_data)
