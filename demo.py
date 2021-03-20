import masksemi as msk
from sklearn import datasets

def main():

    #IMPORT DATASETS
    iris = datasets.load_iris()
    data = iris.data
    labels = iris.target

    #GENERATE UNLABELED DATA
    masked_labels = msk.mask(labels, 0.1)
    
    print(masked_labels)
    
    
if __name__ == "__main__":
    main()