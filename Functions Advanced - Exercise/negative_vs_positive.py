def negative_vs_positive(numbers):
    negatives = sum(filter(lambda x: x < 0, numbers))
    positives = sum(filter(lambda x: x > 0, numbers))
    print(negatives)
    print(positives)
    if abs(negatives) > positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

numbers = list(map(int, input().split()))
negative_vs_positive(numbers)
