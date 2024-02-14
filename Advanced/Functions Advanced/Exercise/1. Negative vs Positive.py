def f(*args):
    positives = []
    negatives = []
    for num in args:
        if num > 0:
            positives.append(num)
        else:
            negatives.append(num)
    neg_sm = sum(negatives)
    print(neg_sm)
    pos_sm = sum(positives)
    print(pos_sm)
    if pos_sm > abs(neg_sm):
        print('The positives are stronger than the negatives')
    else:
        print('The positives are stronger than the negatives')
f(1,2,-3,-4,65,-98,12,57,-84)