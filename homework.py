




def split_sample(sample,train_size,permute):
    if permute==True:
        sample=sample.sample(frac=1).reset_index(drop=True)
    cut=train_size*len(sample)
    cut=int(round(cut))
    train_sample=sample.iloc[:cut,:]
    test_sample=sample.iloc[cut:,:]
    return train_sample, test_sample

if __name__ == '__main__':
    split_sample()