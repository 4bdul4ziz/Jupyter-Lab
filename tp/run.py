import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def discriminant(data_point, class_0_centroid, class_1_centroid, class_2_centroid):
    dist_0 = np.linalg.norm(data_point - class_0_centroid)
    dist_1 = np.linalg.norm(data_point - class_1_centroid)
    dist_2 = np.linalg.norm(data_point - class_2_centroid)

    if dist_0 < dist_1 and dist_0 < dist_2: return 0
    elif dist_1 < dist_2: return 1
    else: return 2

def midpoint(class_0_centroid, class_1_centroid, class_2_centroid): 
    class_01_mid = [(class_0_centroid[i] + class_1_centroid[i])/2 for i in range(len(class_0_centroid))] 
    class_12_mid = [(class_1_centroid[i] + class_2_centroid[i])/2 for i in range(len(class_0_centroid))] 
    class_02_mid = [(class_0_centroid[i] + class_2_centroid[i])/2 for i in range(len(class_0_centroid))] 
    return class_01_mid, class_12_mid, class_02_mid

def run (train_input_dir,train_label_dir,test_input_dir,pclass_0_file):
    train_data = np.loadtxt(train_input_dir,skiprows=0)
    train_labels = np.loadtxt(train_label_dir,skiprows=0)

    num_features = len(train_data[0])

    class_0 = np.array([val for ind,val in enumerate(train_data) if train_labels[ind] == 0], dtype=object)
    class_1 = np.array([val for ind,val in enumerate(train_data) if train_labels[ind] == 1], dtype=object)
    class_2 = np.array([val for ind,val in enumerate(train_data) if train_labels[ind] == 2], dtype=object)

    class_0_centroid = np.array([np.average(class_0[:, i]) for i in range(num_features)])
    class_1_centroid = np.array([np.average(class_1[:, i]) for i in range(num_features)])
    class_2_centroid = np.array([np.average(class_2[:, i]) for i in range(num_features)])

    class_01_mid, class_12_mid, class_02_mid = midpoint(class_0_centroid, class_1_centroid, class_2_centroid)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # ax.scatter(class_0[:, 0], class_0[:, 1], class_0[:, 2], c = 'red', marker = 'o', s = 10)
    # ax.scatter(class_1[:, 0], class_1[:, 1], class_1[:, 2], c = 'green', marker = 'o', s = 10)
    # ax.scatter(class_2[:, 0], class_2[:, 1], class_2[:, 2], c = 'blue', marker = 'o', s = 10)

    ax.scatter3D(class_0_centroid[0], class_0_centroid[1], class_0_centroid[2], c = '#ff0000', marker = '*')
    ax.scatter3D(class_1_centroid[0], class_1_centroid[1], class_1_centroid[2], c = '#00ff00', marker = '*')
    # ax.scatter3D(class_2_centroid[0], class_2_centroid[1], class_2_centroid[2], c = '#0000ff', marker = '*')

    ax.scatter3D(class_01_mid[0], class_01_mid[1], class_01_mid[2], c = 'grey', marker = 'o')
    # ax.scatter3D(class_12_mid[0], class_12_mid[1], class_12_mid[2], c = 'grey', marker = 'o')
    # ax.scatter3D(class_02_mid[0], class_02_mid[1], class_02_mid[2], c = 'grey', marker = 'o')

    length = np.sqrt(np.power(class_0_centroid[0] - class_1_centroid[0], 2) + 
                     np.power(class_0_centroid[1] - class_1_centroid[1], 2) + 
                     np.power(class_0_centroid[2] - class_1_centroid[2], 2))
    xslope_01 = (class_0_centroid[0] - class_1_centroid[0]) / length
    yslope_01 = (class_0_centroid[1] - class_1_centroid[1]) / length
    zslope_01 = (class_0_centroid[2] - class_1_centroid[2]) / length

    space = np.linspace(-10, 10, 2000)
    xline = space * xslope_01 + class_01_mid[0]
    yline = space * yslope_01 + class_01_mid[1]
    zline = space * zslope_01 + class_01_mid[2]

    ax.plot3D(xline, yline, zline, 'gray')


    plt.show()

    # Reading data
    test_data = np.loadtxt(test_input_dir,skiprows=0)
    prediction = np.array([discriminant(data, class_0_centroid, class_1_centroid, class_2_centroid) for data in test_data], dtype=object)

    # Saving you prediction to pclass_0_file directory (Saving can't be changed)
    np.savetxt(pclass_0_file, prediction, fmt='%1d', delimiter=",")
    
if __name__ == "__main__":
    train_input_dir = 'training1.txt'
    train_label_dir = 'training1_label.txt'
    test_input_dir = 'testing1.txt'
    test_label_dir = 'testing1_label.txt'
    pclass_0_file = 'result1.txt'
    run(train_input_dir,train_label_dir,test_input_dir,pclass_0_file)

    predicted = np.loadtxt(pclass_0_file,skiprows=0)
    actual = np.loadtxt(test_label_dir,skiprows=0)

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for a,p in zip(actual, predicted): 
        if a == 1 and p == 1: tp += 1
        elif a == 1 and p == 0: fn += 1
        elif a == 0 and p == 1: fp += 1
        else: tn += 1
    
    accuracy = 100 * (tp + tn) / (tp + fp + tn + fn)
    f1_score = 100 * (2 * tp) / (tp + fn + tp + fp)

    print("Accuracy for dataset 1: %.4f" % accuracy)
    print("F1 score for dataset 1: %.4f" % f1_score)

    # train_input_dir = 'training2.txt'
    # train_label_dir = 'training2_label.txt'
    # test_input_dir = 'testing2.txt'
    # test_label_dir = 'testing2_label.txt'
    # pclass_0_file = 'result2.txt'
    # run(train_input_dir,train_label_dir,test_input_dir,pclass_0_file)

    # actual = np.loadtxt(pclass_0_file,skiprows=0)
    # predicted = np.loadtxt(test_label_dir,skiprows=0)

    # tp = 0
    # fp = 0
    # tn = 0
    # fn = 0

    # for a,p in zip(actual, predicted): 
    #     if a == 1 and p == 1: tp += 1
    #     elif a == 1 and p == 0: fn += 1
    #     elif a == 0 and p == 1: fp += 1
    #     else: tn += 1
    
    # accuracy = 100 * (tp + tn) / (tp + fp + tn + fn)
    # f1_score = 100 * (2 * tp) / (tp + fn + tp + fp)

    # print("Accuracy for dataset 2: %.4f" % accuracy)
    # print("F1 score for dataset 2: %.4f" % f1_score)

