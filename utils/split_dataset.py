"""Split the hdf5 dataset into train and test.
"""

####################################################################################################################################
dir = '/home/user/ledri/vqgtest/'

"""
dir = '/Users/ledrithaqi/Desktop/UZH/Master Thesis/vqgtest/'
"""
####################################################################################################################################

import argparse
import h5py
import numpy as np

def split_dataset(args):

    # load the full dataset
    annos = h5py.File(args.dataset, 'r')
    questions = annos.get('questions')[:]
    answers = annos.get('answers')[:]
    captions = annos.get('captions')[:]
    answer_types = annos.get('answer_types')[:]
    image_indices = annos.get('image_indices')[:]
    images = annos.get('images')[:]
    
    # randomly split the dataset between training and test
    np.random.seed(42)
    idx = np.random.permutation(np.arange(len(questions)))
    train_idx = idx[:int(args.train_size * len(idx))]
    test_idx = idx[int(args.train_size * len(idx)):]

    # save the training dataset
    train_annos = h5py.File(args.train_dataset, 'w')
    train_annos.create_dataset('questions', data=questions[train_idx])
    train_annos.create_dataset('answers', data=answers[train_idx])
    train_annos.create_dataset('captions', data=captions[train_idx])
    train_annos.create_dataset('answer_types', data=answer_types[train_idx])
    train_annos.create_dataset('image_indices', data=image_indices[train_idx])
    train_annos.create_dataset('images', data=images)
    train_annos.close()
    print(f"Training dataset saved to {args.train_dataset}")
    print(f"Number of QAs in training dataset: {len(train_idx)}")

    # save the test dataset
    test_annos = h5py.File(args.test_dataset, 'w')
    test_annos.create_dataset('questions', data=questions[test_idx])
    test_annos.create_dataset('answers', data=answers[test_idx])
    test_annos.create_dataset('captions', data=captions[test_idx])
    test_annos.create_dataset('answer_types', data=answer_types[test_idx])
    test_annos.create_dataset('image_indices', data=image_indices[test_idx])
    test_annos.create_dataset('images', data=images)
    test_annos.close()
    print(f"Test dataset saved to {args.test_dataset}")
    print(f"Number of QAs in test dataset: {len(test_idx)}")


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dataset', type=str,
                        default=dir + 'Dataset/vqgrad_dataset.hdf5',
                        help='Path for full dataset built with `store_dataset.py`')
    
    parser.add_argument('--train-size', type=float,
                        default=0.7,
                        help='Size of train dataset.')
    
    parser.add_argument('--train-dataset', type=str,
                        default=dir + 'Dataset/vqgrad_train_dataset.hdf5',
                        help='Path for train dataset.')
    
    parser.add_argument('--test-dataset', type=str,
                        default=dir + 'Dataset/vqgrad_test_dataset.hdf5',
                        help='Path for test dataset')

    args = parser.parse_args()
    
    split_dataset(args)