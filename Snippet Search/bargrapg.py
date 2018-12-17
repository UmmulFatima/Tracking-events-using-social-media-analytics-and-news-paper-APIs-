import matplotlib.pyplot as plt
normalization_score_list = [0.66,0.33,0.66,0.66,0.33]
no_snippets_list = [10,6,6,5,3]
wup_similarity = [0.8571428571428571, 0.5238095238095238, 0.8571428571428571,0.8571428571428571,0.7321428571428571]
plt.scatter(no_snippets_list,normalization_score_list)
plt.title('Relationship Between Temperature and Iced Coffee Sales')
plt.xlabel('snippets number')
plt.ylabel('normalization score')
plt.show()